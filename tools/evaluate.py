#!/usr/bin/env python3
"""
PrimaTap Language System Evaluation
====================================
Tests the 5-level semantic tap system (8 → 16 → 32 → 64 → 64+molecules)
against common English vocabulary using NLP word vectors.

Analyses:
  1. Orthogonality  — are taps genuinely spread across semantic space?
  2. Coverage       — what % of common words does each level cover?
  3. Composition    — does pair-averaging improve coverage? by how much?
  4. Gap analysis   — which common words are hardest to cover, and why?
  5. Molecule audit — which molecules are genuinely new vs. redundant?
  6. Composition test — does TAP_A + TAP_B land near the expected concept?

Run:
  cd primatap/notebooks
  python3 primatap_evaluate.py

Outputs:
  eval_pca_levels.png
  eval_coverage_curves.png
  eval_molecule_novelty.png
  eval_heatmap_l1.png  /  eval_heatmap_l2.png
  eval_results.json
"""

import json
import warnings
from itertools import combinations
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
from wordfreq import top_n_list

warnings.filterwarnings('ignore')
OUT = Path(__file__).parent

# ══════════════════════════════════════════════════════════════════════════════
# TAP VOCABULARY  — 5 levels, cumulative
# ══════════════════════════════════════════════════════════════════════════════

# Each level name → the NEW taps added at that level (not cumulative)
LEVELS = {

    'L1 · Core 8': [
        # The relational / social skeleton
        'I', 'you', 'not', 'want',
        'good', 'bad', 'now', 'here',
    ],

    'L2 · Physical 16': [
        # The body and physical world
        'alive', 'move', 'think', 'water',
        'heat', 'air', 'solid', 'light',
    ],

    'L3 · Grammar 32': [
        # Time, space, causation, degree — the grammar layer
        'before', 'after',
        'because', 'if', 'can',
        'more', 'same',
        'far', 'above', 'inside',
        'feel', 'hear',
        'say', 'many', 'body', 'kind',
    ],

    'L4 · Wierzbicka 64': [
        # Completing the NSM 65-prime set
        'someone', 'something', 'people',
        'one', 'two', 'some', 'all', 'few',
        'big', 'small',
        'know', 'see', 'touch',
        'do', 'happen',
        'have', 'exist', 'die',
        'true', 'word', 'maybe', 'like', 'very',
        'near', 'below', 'side',
        'when', 'where', 'moment',
        'part', 'another', 'this',
    ],

    'L5 · Molecules ~50': [
        # Widespread but not primitive — the molecule layer
        # Body parts
        'hand', 'eye', 'head', 'mouth', 'ear', 'nose', 'face', 'back', 'foot',
        # Biosocial
        'man', 'woman', 'child', 'mother', 'father',
        # Living things
        'animal', 'plant', 'bird', 'fish', 'tree',
        # Physical world
        'fire', 'earth', 'sky', 'sun', 'moon', 'star', 'night', 'day', 'ground',
        # Properties
        'long', 'round', 'hard', 'sharp', 'heavy',
        # Objects and settings
        'house', 'food', 'road', 'cloth',
        # Missing senses and candidates for L4 debate
        'sound', 'smell', 'taste', 'pain',
        # Structural gaps
        'between', 'together', 'again', 'color', 'name',
    ],
}

LEVEL_COLORS = ['#4CAF50', '#2196F3', '#FF9800', '#E91E63', '#9C27B0']
LEVEL_NAMES  = list(LEVELS.keys())

# Build cumulative lists
CUMULATIVE: dict[str, list[str]] = {}
_acc: list[str] = []
for _name, _words in LEVELS.items():
    _acc = _acc + _words
    CUMULATIVE[_name] = _acc.copy()

# ── Composition test cases ────────────────────────────────────────────────────
# (tap_a, tap_b, expected_concept)
COMPOSITION_TESTS = [
    ('water', 'air',   'cloud'),
    ('water', 'heat',  'steam'),
    ('water', 'solid', 'ice'),
    ('alive', 'solid', 'plant'),
    ('alive', 'air',   'bird'),
    ('heat',  'light', 'fire'),
    ('not',   'alive', 'dead'),
    ('not',   'heat',  'cold'),
    ('not',   'good',  'wrong'),
    ('think', 'good',  'wisdom'),
    ('want',  'water', 'thirsty'),
    ('I',     'move',  'walking'),
    ('feel',  'bad',   'pain'),
    ('alive', 'think', 'conscious'),
    ('move',  'here',  'arrive'),
    ('I',     'want',  'goal'),
    ('many',  'alive', 'crowd'),
    ('above', 'solid', 'mountain'),
    ('water', 'above', 'rain'),
    ('feel',  'good',  'joy'),
]

# ══════════════════════════════════════════════════════════════════════════════
# CORE FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def load_model() -> SentenceTransformer:
    print('Loading sentence-transformers/all-MiniLM-L6-v2 ...')
    return SentenceTransformer('all-MiniLM-L6-v2')


def encode(model: SentenceTransformer, words: list[str]) -> np.ndarray:
    """Encode and L2-normalise so dot product == cosine similarity."""
    emb = model.encode(words, show_progress_bar=False, normalize_embeddings=True)
    return emb.astype(np.float32)


def mean_pairwise_sim(emb: np.ndarray) -> float:
    n = len(emb)
    sims = emb @ emb.T
    return float((sims.sum() - n) / (n * (n - 1)))


def single_coverage(tap_emb: np.ndarray, word_emb: np.ndarray,
                    threshold: float = 0.45) -> float:
    """% of words with at least one tap within cosine threshold."""
    best = (word_emb @ tap_emb.T).max(axis=1)
    return float((best >= threshold).mean() * 100)


def pair_coverage(tap_emb: np.ndarray, word_emb: np.ndarray,
                  threshold: float = 0.45) -> float:
    """% of words covered by best single tap OR pair-average."""
    n = len(tap_emb)
    # All pair averages — shape (n_pairs, dim)
    idx_pairs = list(combinations(range(n), 2))
    pair_vecs = np.array([
        tap_emb[i] + tap_emb[j] for i, j in idx_pairs
    ], dtype=np.float32)
    norms = np.linalg.norm(pair_vecs, axis=1, keepdims=True).clip(1e-8)
    pair_vecs /= norms
    # Combine singles + pairs
    all_vecs = np.vstack([tap_emb, pair_vecs])
    best = (word_emb @ all_vecs.T).max(axis=1)
    return float((best >= threshold).mean() * 100)


def find_gaps(tap_emb: np.ndarray, word_list: list[str],
              word_emb: np.ndarray, n: int = 40) -> list[tuple[str, float]]:
    """Words furthest from any tap — semantic gaps."""
    best = (word_emb @ tap_emb.T).max(axis=1)
    worst_idx = np.argsort(best)[:n]
    return [(word_list[i], float(best[i])) for i in worst_idx]


def molecule_audit(l4_emb: np.ndarray, mol_emb: np.ndarray,
                   mol_names: list[str],
                   threshold: float = 0.50) -> list[dict]:
    """Score each molecule: how novel is it vs. the L4 prime set?"""
    sims = (mol_emb @ l4_emb.T).max(axis=1)
    results = []
    for name, sim in zip(mol_names, sims):
        results.append({
            'molecule': name,
            'max_sim_to_l4': round(float(sim), 4),
            'novel': bool(sim < threshold),
        })
    return sorted(results, key=lambda r: r['max_sim_to_l4'])


def run_composition_tests(model: SentenceTransformer,
                          tap_emb: np.ndarray, tap_names: list[str],
                          vocab_list: list[str], vocab_emb: np.ndarray
                          ) -> list[dict]:
    """
    For each (A, B) → expected test:
      - Compute averaged & normalised vector of A and B
      - Find top-5 nearest neighbours in full vocabulary
      - Report whether expected concept appears in top-5
    """
    results = []
    tap_map = {w: tap_emb[i] for i, w in enumerate(tap_names)}

    for a, b, expected in COMPOSITION_TESTS:
        if a not in tap_map or b not in tap_map:
            continue
        combo = tap_map[a] + tap_map[b]
        norm = np.linalg.norm(combo)
        if norm < 1e-8:
            continue
        combo = combo / norm

        sims = vocab_emb @ combo
        top5_idx = np.argsort(sims)[-5:][::-1]
        top5 = [(vocab_list[i], round(float(sims[i]), 3)) for i in top5_idx]

        hit = any(expected in w or w in expected for w, _ in top5)
        results.append({
            'a': a, 'b': b, 'expected': expected,
            'top5': top5, 'hit': hit,
            'best_sim': top5[0][1],
        })
    return results

# ══════════════════════════════════════════════════════════════════════════════
# VISUALISATIONS
# ══════════════════════════════════════════════════════════════════════════════

DARK_BG  = '#0e1117'
DARK_AX  = '#1a1d23'
DARK_GRID = '#2a2d33'


def style_ax(ax):
    ax.set_facecolor(DARK_AX)
    ax.tick_params(colors='#aaa', labelsize=8)
    for sp in ax.spines.values():
        sp.set_color(DARK_GRID)
    ax.grid(True, alpha=0.15, color=DARK_GRID)


def plot_pca_levels(model: SentenceTransformer):
    all_words, all_colors, all_sizes = [], [], []
    for (name, words), color in zip(LEVELS.items(), LEVEL_COLORS):
        all_words += words
        all_colors += [color] * len(words)
        all_sizes  += [80] * len(words)

    emb    = encode(model, all_words)
    pca    = PCA(n_components=2)
    coords = pca.fit_transform(emb)

    fig, ax = plt.subplots(figsize=(16, 10), facecolor=DARK_BG)
    style_ax(ax)

    offset = 0
    for (name, words), color in zip(LEVELS.items(), LEVEL_COLORS):
        n = len(words)
        xs, ys = coords[offset:offset+n, 0], coords[offset:offset+n, 1]
        ax.scatter(xs, ys, c=color, s=85, label=name, zorder=3, alpha=0.88)
        offset += n

    for i, word in enumerate(all_words):
        ax.annotate(word, coords[i], fontsize=6, color='#bbb',
                    textcoords='offset points', xytext=(4, 3))

    ax.set_title('PrimaTap — All Levels in Semantic Space (PCA of 384-dim)',
                 color='white', fontsize=13, pad=10)
    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)',
                  color='#aaa')
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)',
                  color='#aaa')
    ax.legend(facecolor=DARK_AX, edgecolor=DARK_GRID, labelcolor='white',
              fontsize=8, loc='upper right')

    path = OUT / 'eval_pca_levels.png'
    plt.tight_layout()
    plt.savefig(path, dpi=150, facecolor=DARK_BG)
    plt.close()
    print(f'  Saved {path.name}')


def plot_coverage_curves(model: SentenceTransformer,
                         word_list: list[str], word_emb: np.ndarray):
    thresholds = np.arange(0.20, 0.72, 0.04)
    fig, ax = plt.subplots(figsize=(12, 7), facecolor=DARK_BG)
    style_ax(ax)

    for (name, taps), color in zip(CUMULATIVE.items(), LEVEL_COLORS):
        tap_emb = encode(model, taps)
        covs = [single_coverage(tap_emb, word_emb, t) for t in thresholds]
        ax.plot(thresholds, covs, color=color, linewidth=2.5,
                label=f'{name}  ({len(taps)} taps)',
                marker='o', markersize=4)

    ax.axvline(0.45, color='#666', linestyle='--', linewidth=1,
               label='default threshold (0.45)')
    ax.set_xlabel('Cosine similarity threshold', color='#aaa', fontsize=11)
    ax.set_ylabel('Top-5000 English words covered (%)', color='#aaa', fontsize=11)
    ax.set_title('Vocabulary Coverage by Level — Single Tap Nearest Neighbour',
                 color='white', fontsize=12, pad=10)
    ax.set_ylim(0, 100)
    ax.legend(facecolor=DARK_AX, edgecolor=DARK_GRID, labelcolor='white', fontsize=8)

    path = OUT / 'eval_coverage_curves.png'
    plt.tight_layout()
    plt.savefig(path, dpi=150, facecolor=DARK_BG)
    plt.close()
    print(f'  Saved {path.name}')


def plot_molecule_novelty(audit: list[dict]):
    names = [r['molecule'] for r in audit]
    sims  = [r['max_sim_to_l4'] for r in audit]
    colors = ['#4CAF50' if r['novel'] else '#F44336' for r in audit]

    fig, ax = plt.subplots(figsize=(10, max(6, len(names) * 0.25)),
                           facecolor=DARK_BG)
    style_ax(ax)
    ax.barh(names, sims, color=colors, alpha=0.85)
    ax.axvline(0.50, color='#FF9800', linestyle='--', linewidth=1.5,
               label='novelty threshold (0.50)')
    ax.set_xlabel('Similarity to nearest L4 prime', color='#aaa', fontsize=10)
    ax.set_title('Molecule Novelty Audit\n'
                 'Green = genuinely new semantic territory  ·  '
                 'Red = already covered by L4 primes',
                 color='white', fontsize=11, pad=8)
    ax.set_xlim(0, 1)
    ax.invert_yaxis()
    ax.legend(facecolor=DARK_AX, edgecolor=DARK_GRID, labelcolor='white', fontsize=8)

    path = OUT / 'eval_molecule_novelty.png'
    plt.tight_layout()
    plt.savefig(path, dpi=150, facecolor=DARK_BG)
    plt.close()
    print(f'  Saved {path.name}')


def plot_heatmap(emb: np.ndarray, names: list[str],
                 title: str, filename: str):
    sim = emb @ emb.T
    mean_sim = (sim.sum() - len(names)) / (len(names) * (len(names) - 1))

    sz = max(8, len(names) * 0.45)
    fig, ax = plt.subplots(figsize=(sz, sz * 0.85), facecolor=DARK_BG)
    ax.set_facecolor(DARK_AX)
    im = ax.imshow(sim, cmap='RdYlGn', vmin=0, vmax=1)
    plt.colorbar(im, ax=ax, label='Cosine similarity')
    ax.set_xticks(range(len(names)))
    ax.set_yticks(range(len(names)))
    ax.set_xticklabels(names, rotation=45, ha='right', fontsize=8, color='#ccc')
    ax.set_yticklabels(names, fontsize=8, color='#ccc')
    for i in range(len(names)):
        for j in range(len(names)):
            ax.text(j, i, f'{sim[i,j]:.2f}', ha='center', va='center',
                    fontsize=6.5,
                    color='white' if sim[i, j] > 0.75 else '#222')
    ax.set_title(f'{title}\nMean pairwise similarity: {mean_sim:.3f}'
                 '  (lower = more orthogonal)',
                 color='white', fontsize=10, pad=8)

    path = OUT / filename
    plt.tight_layout()
    plt.savefig(path, dpi=130, facecolor=DARK_BG)
    plt.close()
    print(f'  Saved {path.name}  |  mean sim: {mean_sim:.3f}')
    return mean_sim


def plot_composition_results(results: list[dict]):
    hits   = [r for r in results if r['hit']]
    misses = [r for r in results if not r['hit']]

    fig, axes = plt.subplots(1, 2, figsize=(16, max(5, len(results) * 0.45)),
                             facecolor=DARK_BG)

    for ax, subset, color, label in [
        (axes[0], hits,   '#4CAF50', f'Hits ({len(hits)})'),
        (axes[1], misses, '#F44336', f'Misses ({len(misses)})'),
    ]:
        style_ax(ax)
        if not subset:
            ax.text(0.5, 0.5, 'none', ha='center', va='center',
                    color='#666', transform=ax.transAxes)
            ax.set_title(label, color='white', fontsize=11)
            continue

        labels = [f'{r["a"]} + {r["b"]} → {r["expected"]}' for r in subset]
        sims   = [r['best_sim'] for r in subset]
        ax.barh(labels, sims, color=color, alpha=0.80)
        ax.set_xlim(0, 1)
        ax.invert_yaxis()
        ax.set_xlabel('Similarity of top result', color='#aaa', fontsize=9)
        ax.set_title(label, color='white', fontsize=11)
        # Annotate with top word
        for i, r in enumerate(subset):
            top_word = r['top5'][0][0]
            ax.text(r['best_sim'] + 0.01, i, top_word,
                    va='center', color='#ccc', fontsize=7)

    fig.suptitle('Composition Test — TAP_A + TAP_B → expected concept',
                 color='white', fontsize=12)
    path = OUT / 'eval_composition.png'
    plt.tight_layout()
    plt.savefig(path, dpi=150, facecolor=DARK_BG)
    plt.close()
    print(f'  Saved {path.name}')

# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

def main():
    print('\n' + '═' * 60)
    print('  PrimaTap Evaluation Engine')
    print('═' * 60 + '\n')

    model = load_model()

    # ── Vocabulary ─────────────────────────────────────────────────────────
    print('Loading top-5000 English words ...')
    raw = top_n_list('en', 6000)
    word_list = [w for w in raw if len(w) > 1 and not w.isdigit()][:5000]
    print(f'Test vocabulary: {len(word_list)} words\n')
    word_emb = encode(model, word_list)

    # Pre-encode all levels
    level_embs = {name: encode(model, taps)
                  for name, taps in CUMULATIVE.items()}

    results = {}

    # ── 1. Orthogonality ───────────────────────────────────────────────────
    print('── 1. Orthogonality (lower = more spread out) ' + '─' * 15)
    ortho = {}
    for name, emb in level_embs.items():
        ms = mean_pairwise_sim(emb)
        ortho[name] = round(ms, 4)
        print(f'  {name:<30}  mean pairwise sim: {ms:.4f}')
    results['orthogonality'] = ortho
    print()

    # ── 2. Single-tap coverage ─────────────────────────────────────────────
    print('── 2. Coverage at threshold 0.45 ' + '─' * 26)
    cov_single = {}
    for name, emb in level_embs.items():
        cov = single_coverage(emb, word_emb)
        cov_single[name] = round(cov, 2)
        print(f'  {name:<30}  {cov:5.1f}%  ({len(CUMULATIVE[name])} taps)')
    results['coverage_single'] = cov_single
    print()

    # ── 3. Composition boost ───────────────────────────────────────────────
    print('── 3. Pair-composition boost ' + '─' * 29)
    cov_pair = {}
    for name in list(CUMULATIVE.keys())[:3]:   # pairs only for L1–L3 (speed)
        emb  = level_embs[name]
        cs   = single_coverage(emb, word_emb)
        cp   = pair_coverage(emb, word_emb)
        gain = cp - cs
        cov_pair[name] = {'single': round(cs, 2), 'pair': round(cp, 2),
                          'gain': round(gain, 2)}
        print(f'  {name:<30}  single {cs:5.1f}%  →  pairs {cp:5.1f}%'
              f'  (+{gain:.1f}%)')
    results['coverage_pair'] = cov_pair
    print()

    # ── 4. Gap analysis at L4 ──────────────────────────────────────────────
    print('── 4. Top-40 vocabulary gaps at L4 (64 taps) ' + '─' * 13)
    l4_emb   = level_embs['L4 · Wierzbicka 64']
    l5_emb   = level_embs['L5 · Molecules ~50']
    gaps_l4  = find_gaps(l4_emb, word_list, word_emb, n=40)
    print(f'  {"word":<20}  {"L4 sim":>7}  {"L5 sim":>7}  rescued')
    gap_results = []
    for word, sim4 in gaps_l4:
        wi    = word_list.index(word)
        sim5  = float((word_emb[wi:wi+1] @ l5_emb.T).max())
        resc  = '✓' if sim5 - sim4 > 0.04 else ' '
        print(f'  {word:<20}  {sim4:7.3f}  {sim5:7.3f}  {resc}')
        gap_results.append({'word': word, 'l4_sim': round(sim4, 4),
                            'l5_sim': round(sim5, 4),
                            'rescued': sim5 - sim4 > 0.04})
    results['gaps'] = gap_results
    print()

    # ── 5. Molecule audit ──────────────────────────────────────────────────
    print('── 5. Molecule novelty audit ' + '─' * 30)
    mol_names = LEVELS['L5 · Molecules ~50']
    mol_emb   = encode(model, mol_names)
    audit     = molecule_audit(l4_emb, mol_emb, mol_names)
    novel     = [r for r in audit if r['novel']]
    redundant = [r for r in audit if not r['novel']]
    print(f'  Novel (< 0.50 from any L4 prime): {len(novel)}/{len(mol_names)}')
    print(f'  Redundant (≥ 0.50):              {len(redundant)}/{len(mol_names)}')
    print()
    print(f'  {"molecule":<15}  {"L4 sim":>7}  status')
    for r in audit:
        flag = '✓ novel     ' if r['novel'] else '✗ redundant'
        print(f'  {r["molecule"]:<15}  {r["max_sim_to_l4"]:7.3f}  {flag}')
    results['molecule_audit'] = audit
    print()

    # ── 6. Composition tests ───────────────────────────────────────────────
    print('── 6. Composition tests (TAP_A + TAP_B → target) ' + '─' * 9)
    all_l5_taps = CUMULATIVE['L5 · Molecules ~50']
    all_l5_emb  = level_embs['L5 · Molecules ~50']
    comp_results = run_composition_tests(
        model, all_l5_emb, all_l5_taps, word_list, word_emb
    )
    hits   = sum(1 for r in comp_results if r['hit'])
    misses = len(comp_results) - hits
    print(f'  Hit rate: {hits}/{len(comp_results)} ({hits/len(comp_results)*100:.0f}%)\n')
    print(f'  {"a + b → expected":<35}  {"top result":<15}  {"sim":>5}  ok?')
    for r in comp_results:
        top_word, top_sim = r['top5'][0]
        ok = '✓' if r['hit'] else '✗'
        label = f'{r["a"]} + {r["b"]} → {r["expected"]}'
        print(f'  {label:<35}  {top_word:<15}  {top_sim:5.3f}  {ok}')
    results['composition'] = comp_results
    print()

    # ── 7. Summary ─────────────────────────────────────────────────────────
    print('── Summary ' + '─' * 47)
    print(f'  L1 orthogonality (8 taps):        {ortho[LEVEL_NAMES[0]]:.3f}')
    print(f'  L4 orthogonality (64 taps):       {ortho[LEVEL_NAMES[3]]:.3f}')
    print(f'  Coverage gain L1→L5:              '
          f'{cov_single[LEVEL_NAMES[0]]:.1f}% → '
          f'{cov_single[LEVEL_NAMES[4]]:.1f}%')
    print(f'  Novel molecules:                  {len(novel)}/{len(mol_names)}')
    print(f'  Gap words rescued by molecules:   '
          f'{sum(1 for g in gap_results if g["rescued"])}/{len(gap_results)}')
    print(f'  Composition hit rate:             {hits}/{len(comp_results)}')
    print()

    # ── Save JSON ──────────────────────────────────────────────────────────
    json_path = OUT / 'eval_results.json'
    # Serialise numpy booleans
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f'  Results saved to {json_path.name}')
    print()

    # ── Visualisations ─────────────────────────────────────────────────────
    print('── Generating visualisations ' + '─' * 30)

    plot_pca_levels(model)
    plot_coverage_curves(model, word_list, word_emb)
    plot_molecule_novelty(audit)
    plot_composition_results(comp_results)

    l1_emb = level_embs['L1 · Core 8']
    plot_heatmap(l1_emb, CUMULATIVE['L1 · Core 8'],
                 'L1 — Core 8 Taps', 'eval_heatmap_l1.png')

    l2_words = CUMULATIVE['L2 · Physical 16']
    l2_emb   = level_embs['L2 · Physical 16']
    plot_heatmap(l2_emb, l2_words,
                 'L2 — 16 Taps', 'eval_heatmap_l2.png')

    print('\n' + '═' * 60)
    print('  Done.')
    print('═' * 60 + '\n')


if __name__ == '__main__':
    main()
