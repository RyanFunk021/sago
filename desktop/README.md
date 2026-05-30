# PrimaTap

A universal semantic primitive communication system.

**Author:** Ryan Funk  
**Started:** May 2026  
**Version:** 0.1 (proof of concept)

---

## What It Is

PrimaTap replaces letters and words with 16 semantic primitives — fundamental units of meaning that underlie all human language. Communication is sequences of primitives rather than sequences of letters. The system works across modalities: spoken syllables, a 16-key keyboard, or tactile finger patterns for deaf-blind users.

See [PRIMITIVES.md](PRIMITIVES.md) for the canonical primitive definitions (the basis document).

---

## Quick Start

```bash
cd primatap
pip3 install streamlit sentence-transformers openai-whisper pyaudio pynput anthropic wordfreq
./start.sh
```

Open http://localhost:8501

---

## The Three Tabs

**Learn** — Click primitives to hear their syllables. Quiz mode tracks your acquisition.

**Speak** — Record yourself saying syllables or English words. Whisper transcribes, the system maps to primitives. Adaptive — only shows what you currently know, teaches the next primitive after each session.

**Type** — Use the 16-key keyboard layout. Type on the home row and see primitives decoded in real time.

---

## Keyboard Layout

```
  [W]   [E]   [R]              [U]   [I]   [O]
 HEAT  ALIVE MOVE             THINK WATER  AIR
  fu    li    mo                te    du    re

  [S]   [D]   [F]  [G]  [H]  [J]   [K]   [L]
 GOOD  OTHER SELF  NOW  HERE  NOT  WANT   BAD
  go    to    sa   ne   hi    na    wu    bi

        [V]                    [N]
       SOLID                  LIGHT
        ko                     lu

                    [SPACE]
```

Pinkies unused. Thumbs = space.

---

## Files

| File | Purpose |
|---|---|
| `PRIMITIVES.md` | **Canonical basis document** — defines all 16 primitives |
| `primitives.py` | Python primitive definitions, key/syllable maps |
| `app.py` | Streamlit app (Learn + Speak + Type tabs) |
| `audio.py` | macOS `say` wrapper, pyaudio recording |
| `recognizer.py` | Whisper-based syllable recognition |
| `learner.py` | Adaptive learner model — tracks acquisition, filters to known primitives |
| `start.sh` | Launch script |
| `../primatap_canonical_embeddings.json` | Frozen embedding geometry for 16 primitives |
| `../primatap_dictionary.ipynb` | Builds full English→primitive dictionary via Claude API |
| `../semantic_primitives.ipynb` | Experiment 0 — visualizes primitive geometry |

---

## The Acquisition Order

Primitives are introduced in tiers. The system never shows you what you haven't learned yet.

| Tier | Primitives |
|---|---|
| 1 | SELF, OTHER, NOT, WANT |
| 2 | GOOD, BAD, NOW, HERE |
| 3 | ALIVE, MOVE, THINK, WATER |
| 4 | AIR, HEAT, SOLID, LIGHT |

---

## Hello World

```
hi to li hi
HERE · OTHER · ALIVE · HERE
```

*I am here. You are there. Something alive is reaching across.*

---

## Research Documents

| Document | Location |
|---|---|
| Blog post 1 — the concept | `~/chord_language_blog.md` |
| Blog post 2 — peer-to-peer | `~/peer_to_peer_blog.md` |
| LinkedIn posts (6) | `~/linkedin_posts.md` |
| Technical paper | `~/chord_language_paper.md` |
| Acquisition engine spec | `~/acquisition_engine_spec.md` |
| Language design (syllables + keyboard) | `~/primatap_language_design.md` |
