#!/usr/bin/env python3
"""
PrimaTap Bidirectional Translator + Back-Translation Test
=========================================================
Translates English ↔ PrimaTap using Claude.
Tests semantic preservation by translating 10 book paragraphs
English → PrimaTap → English and measuring meaning loss.

Run:
  python3 primatap_translate.py
"""

import json
import os
import sys
import textwrap
import warnings
from pathlib import Path

import anthropic

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))
from primatap_taps import TAPS, tap_inventory_string, GRAMMAR_RULES, COMPOSITION_EXAMPLES

OUT = Path(__file__).parent
DICT_FILE = OUT / "primatap_dictionary.json"
RESULTS_FILE = OUT / "translate_results.json"


# ── API ───────────────────────────────────────────────────────────────────────

def load_api_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key:
        creds = Path("/Users/ryanfunk/projects/wordlens/creds.json")
        if creds.exists():
            with open(creds) as f:
                key = json.load(f).get("ANTHROPIC_API_KEY", "")
    if not key:
        import getpass
        key = getpass.getpass("ANTHROPIC_API_KEY: ").strip()
    return key


# ── System prompts ────────────────────────────────────────────────────────────

def make_e2p_prompt() -> str:
    return f"""You are a PrimaTap translator. PrimaTap is a meaning-based language with 90 semantic primitive taps.
Your task: translate English text into PrimaTap tap sequences.

TAP INVENTORY:
{tap_inventory_string()}

{GRAMMAR_RULES}

{COMPOSITION_EXAMPLES}

TRANSLATION RULES:
- Output tap SYLLABLES only (sa, to, na, du, ...) separated by spaces
- One sequence per sentence, separated by newlines
- Capture MEANING, not surface words — PrimaTap encodes semantics, not syntax
- For proper names: use  we [phonetic syllables] we  (name bracket)
- For institutional/untranslatable concepts: use [WORD] in brackets
- Keep it as compact as possible — fewer taps is better if meaning is preserved
- Multiple English sentences = multiple PrimaTap lines

Output ONLY the PrimaTap tap sequence(s). No explanation, no labels, no English."""


def make_p2e_prompt() -> str:
    return f"""You are a PrimaTap interpreter. PrimaTap is a meaning-based language with 90 semantic primitive taps.
Your task: translate PrimaTap tap sequences back into natural English.

TAP INVENTORY:
{tap_inventory_string()}

{GRAMMAR_RULES}

{COMPOSITION_EXAMPLES}

TRANSLATION RULES:
- Interpret the MEANING of each tap and their combination
- Produce natural, fluent English — not a word-for-word gloss
- Reconstruct the full intended meaning, including implied context
- If a tap sequence is ambiguous, pick the most natural reading
- [WORD] in brackets = untranslatable concept, keep as-is
- Multiple lines = multiple sentences

Output ONLY the English translation. No explanation, no tap labels, no PrimaTap."""


# ── Translation functions ─────────────────────────────────────────────────────

def translate_to_primatap(client: anthropic.Anthropic, text: str, system_prompt: str) -> str:
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=[{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text.strip()


def translate_from_primatap(client: anthropic.Anthropic, taps: str, system_prompt: str) -> str:
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=[{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": taps}],
    )
    return response.content[0].text.strip()


def semantic_similarity(text_a: str, text_b: str, model) -> float:
    embeddings = model.encode([text_a, text_b])
    a, b = embeddings[0], embeddings[1]
    dot = float(sum(x * y for x, y in zip(a, b)))
    norm_a = float(sum(x * x for x in a) ** 0.5)
    norm_b = float(sum(x * x for x in b) ** 0.5)
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0


# ── Test corpus ───────────────────────────────────────────────────────────────

BOOKS = [
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "domain": "social/romantic",
        "text": (
            "It is a truth universally acknowledged, that a single man in possession of a good fortune, "
            "must be in want of a wife. However little known the feelings or views of such a man may be "
            "on his first entering a neighbourhood, this truth is so well fixed in the minds of the "
            "surrounding families, that he is considered the rightful property of some one or other of "
            "their daughters."
        ),
    },
    {
        "title": "Hamlet",
        "author": "William Shakespeare",
        "domain": "existential/philosophical",
        "text": (
            "To be, or not to be, that is the question: whether 'tis nobler in the mind to suffer "
            "the slings and arrows of outrageous fortune, or to take arms against a sea of troubles "
            "and by opposing end them. To die — to sleep, no more; and by a sleep to say we end "
            "the heart-ache and the thousand natural shocks that flesh is heir to."
        ),
    },
    {
        "title": "A Tale of Two Cities",
        "author": "Charles Dickens",
        "domain": "historical/lyrical",
        "text": (
            "It was the best of times, it was the worst of times, it was the age of wisdom, "
            "it was the age of foolishness, it was the epoch of belief, it was the epoch of "
            "incredulity, it was the season of Light, it was the season of Darkness, it was "
            "the spring of hope, it was the winter of despair."
        ),
    },
    {
        "title": "The Metamorphosis",
        "author": "Franz Kafka",
        "domain": "surreal/psychological",
        "text": (
            "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed "
            "in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his "
            "head a little he could see his brown belly, slightly domed and divided by arches into "
            "stiff sections."
        ),
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "domain": "dystopian/political",
        "text": (
            "It was a bright cold day in April, and the clocks were striking thirteen. "
            "Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, "
            "slipped quickly through the glass doors of Victory Mansions, though not quickly enough "
            "to prevent a swirl of gritty dust from entering along with him."
        ),
    },
    {
        "title": "Alice in Wonderland",
        "author": "Lewis Carroll",
        "domain": "whimsical/children's",
        "text": (
            "Alice was beginning to get very tired of sitting by her sister on the bank, and of "
            "having nothing to do. Once or twice she had peeped into the book her sister was reading, "
            "but it had no pictures or conversations in it, and what is the use of a book, thought "
            "Alice, without pictures or conversations?"
        ),
    },
    {
        "title": "Moby Dick",
        "author": "Herman Melville",
        "domain": "adventure/philosophical",
        "text": (
            "Call me Ishmael. Some years ago — never mind how long precisely — having little money "
            "in my purse, and nothing particular to interest me on shore, I thought I would sail about "
            "a little and see the watery part of the world. It is a way I have of driving off the "
            "spleen and regulating the circulation."
        ),
    },
    {
        "title": "The Old Man and the Sea",
        "author": "Ernest Hemingway",
        "domain": "simple/powerful",
        "text": (
            "He was an old man who fished alone in a skiff in the Gulf Stream and he had gone "
            "eighty-four days now without taking a fish. In the first forty days a boy had been "
            "with him. But after forty days without a fish the boy's parents had told the boy "
            "that the old man was now definitely and finally salao, which is the worst form of "
            "unlucky."
        ),
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "domain": "introspective/social",
        "text": (
            "In my younger and more vulnerable years my father gave me some advice that I've been "
            "turning over in my mind ever since. 'Whenever you feel like criticizing anyone,' he "
            "told me, 'just remember that all the people in this world haven't had the advantages "
            "that you've had.'"
        ),
    },
    {
        "title": "On the Origin of Species",
        "author": "Charles Darwin",
        "domain": "scientific/empirical",
        "text": (
            "When we look at the individuals of the same variety or sub-variety of our older "
            "cultivated plants and animals, one of the first things which strikes us, is that "
            "they generally differ much more from each other than do the individuals of any one "
            "species or variety in a state of nature."
        ),
    },
]


# ── Main test ─────────────────────────────────────────────────────────────────

def wrap(text: str, width: int = 72, indent: str = "  ") -> str:
    return textwrap.fill(text, width=width, initial_indent=indent, subsequent_indent=indent)


def run_back_translation_test(client: anthropic.Anthropic):
    print("\nLoading sentence-transformers for similarity scoring...")
    from sentence_transformers import SentenceTransformer
    st_model = SentenceTransformer("all-MiniLM-L6-v2")

    e2p_system = make_e2p_prompt()
    p2e_system = make_p2e_prompt()

    results = []
    print(f"\nRunning back-translation test on {len(BOOKS)} books...\n")
    print("=" * 80)

    for i, book in enumerate(BOOKS):
        print(f"\n[{i+1}/{len(BOOKS)}] {book['title']} — {book['author']} ({book['domain']})")
        print("-" * 72)

        original = book["text"]
        print("ORIGINAL:")
        print(wrap(original))

        print("\nTranslating English → PrimaTap...", end=" ", flush=True)
        primatap = translate_to_primatap(client, original, e2p_system)
        print("done")
        print("\nPRIMATAP:")
        print(wrap(primatap))

        print("\nTranslating PrimaTap → English...", end=" ", flush=True)
        back_translated = translate_from_primatap(client, primatap, p2e_system)
        print("done")
        print("\nBACK-TRANSLATED:")
        print(wrap(back_translated))

        sim = semantic_similarity(original, back_translated, st_model)
        print(f"\nSEMANTIC SIMILARITY: {sim:.3f}", end="")
        if sim >= 0.85:
            print("  ★★★ Excellent")
        elif sim >= 0.70:
            print("  ★★  Good")
        elif sim >= 0.55:
            print("  ★   Partial")
        else:
            print("  ✗   Significant loss")

        # Count tap tokens
        tap_tokens = len([t for t in primatap.split() if t in TAPS])
        total_tokens = len(primatap.split())
        english_words = len(original.split())
        compression = tap_tokens / english_words if english_words else 0

        print(f"  English words: {english_words}  |  PrimaTap tokens: {total_tokens}  |  Compression: {compression:.2f}x")

        results.append({
            "title": book["title"],
            "author": book["author"],
            "domain": book["domain"],
            "original": original,
            "primatap": primatap,
            "back_translated": back_translated,
            "similarity": round(sim, 4),
            "english_words": english_words,
            "primatap_tokens": total_tokens,
            "compression_ratio": round(compression, 3),
        })

    # Summary table
    print("\n" + "=" * 80)
    print("\nSUMMARY TABLE")
    print("-" * 80)
    header = f"{'Book':<32} {'Domain':<22} {'Sim':>5} {'ENG':>4} {'PT':>4} {'Ratio':>6}"
    print(header)
    print("-" * 80)
    for r in results:
        sim_star = "★★★" if r["similarity"] >= 0.85 else ("★★ " if r["similarity"] >= 0.70 else ("★  " if r["similarity"] >= 0.55 else "✗  "))
        print(
            f"{r['title']:<32} {r['domain']:<22} "
            f"{r['similarity']:>5.3f} {r['english_words']:>4} "
            f"{r['primatap_tokens']:>4} {r['compression_ratio']:>6.2f}x  {sim_star}"
        )

    avg_sim = sum(r["similarity"] for r in results) / len(results)
    avg_comp = sum(r["compression_ratio"] for r in results) / len(results)
    print("-" * 80)
    print(f"{'AVERAGE':<56} {avg_sim:>5.3f}              {avg_comp:>5.2f}x")
    print()

    # Analysis
    print("ANALYSIS:")
    high = [r for r in results if r["similarity"] >= 0.70]
    low = [r for r in results if r["similarity"] < 0.55]
    print(f"  Good preservation (≥0.70): {len(high)}/10 — {', '.join(r['title'] for r in high)}")
    if low:
        print(f"  Significant loss (<0.55):  {len(low)}/10 — {', '.join(r['title'] for r in low)}")

    avg_comp_pct = (1 - avg_comp) * 100
    if avg_comp < 1.0:
        print(f"  PrimaTap averages {avg_comp:.2f}x compression ({abs(avg_comp_pct):.0f}% {'shorter' if avg_comp_pct > 0 else 'longer'})")
    else:
        print(f"  PrimaTap averages {avg_comp:.2f}x expansion (more verbose than source)")

    print(f"\n  Overall semantic preservation: {avg_sim:.1%}")

    # Save results
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to: {RESULTS_FILE}")

    return results


def translate_interactive(client: anthropic.Anthropic):
    """Simple interactive translation loop."""
    e2p = make_e2p_prompt()
    p2e = make_p2e_prompt()

    print("\nInteractive PrimaTap Translator")
    print("Commands: 'e' = English→PrimaTap, 'p' = PrimaTap→English, 'q' = quit\n")

    while True:
        direction = input("Direction [e/p/q]: ").strip().lower()
        if direction == "q":
            break
        elif direction == "e":
            text = input("English: ").strip()
            if text:
                result = translate_to_primatap(client, text, e2p)
                print(f"PrimaTap: {result}\n")
        elif direction == "p":
            taps = input("PrimaTap: ").strip()
            if taps:
                result = translate_from_primatap(client, taps, p2e)
                print(f"English: {result}\n")


def main():
    print("PrimaTap Bidirectional Translator")
    print("=" * 50)

    api_key = load_api_key()
    client = anthropic.Anthropic(api_key=api_key)

    print("\nWhat would you like to do?")
    print("  1. Run back-translation test (10 books)")
    print("  2. Interactive translation")
    print("  3. Both")

    choice = input("\nChoice [1/2/3, default=1]: ").strip() or "1"

    if choice in ("1", "3"):
        run_back_translation_test(client)

    if choice in ("2", "3"):
        translate_interactive(client)


if __name__ == "__main__":
    main()
