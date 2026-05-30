# PrimaTap Canonical Primitive Definitions — v1.0

**This is the basis document.**
All implementations, papers, experiments, and derivative works reference this version.
Do not change primitive definitions without incrementing the version and documenting the reason.

**Version:** 1.0  
**Date:** May 2026  
**Author:** Ryan Funk  
**Embedding basis:** `sentence-transformers/all-MiniLM-L6-v2` (384 dimensions)  
**Geometry file:** `primatap_canonical_embeddings.json`  
**Mean pairwise cosine similarity:** 0.321 (good separation — lower is more orthogonal)

---

## The 16 Primitives

| # | Name | Syllable | Key | Emoji | Core Meaning | Excludes |
|---|---|---|---|---|---|---|
| 1 | **SELF** | sa | F | 👤 | The communicating agent. I, me, my, mine. | Other entities |
| 2 | **OTHER** | to | D | 👥 | Any entity that is not SELF. You, they, it, he, she. | The speaker |
| 3 | **NOT** | na | J | ❌ | Negation. Absence. Opposite. The null of any concept. | Assertion |
| 4 | **WANT** | wu | K | 🤲 | Desire, need, intention, wish directed toward something. | Satisfaction |
| 5 | **GOOD** | go | S | ✅ | Positive valence. Correct, safe, pleasant, beneficial. | Harm |
| 6 | **BAD** | bi | L | ⚠️ | Negative valence. Wrong, dangerous, unpleasant, harmful. | Benefit |
| 7 | **NOW** | ne | G | ⚡ | Present time. Immediate. Current. This moment. | Past, future |
| 8 | **HERE** | hi | H | 📍 | This place. Proximal location. Where I am. | Distal space |
| 9 | **ALIVE** | li | E | 💚 | Living, active, conscious, functioning, animate. | Inert |
| 10 | **MOVE** | mo | R | ➡️ | Motion, action, change of state or position. | Stasis |
| 11 | **WATER** | du | I | 💧 | Liquid, fluid, wet. The element water in all forms. | Solid/Gas |
| 12 | **AIR** | re | O | 🌬️ | Gas, breath, wind, sky. The element air in all forms. | Liquid/Solid |
| 13 | **HEAT** | fu | W | 🔥 | Temperature, thermal energy, warmth, fire. | Cold |
| 14 | **SOLID** | ko | V | 🪨 | Physical object, matter, earth, hard, tangible. | Fluid/Gas |
| 15 | **LIGHT** | lu | N | ☀️ | Visible energy, brightness, color, the sense of sight. | Dark |
| 16 | **THINK** | te | U | 💭 | Know, understand, believe, imagine, remember. | Physical action |

---

## Design Decisions (Record of Intent)

**Why 16 and not 15 or 65?**
16 fits a 4-bit binary encoding (2⁴ = 16), maps cleanly to a keyboard quadrant, and covers the first tier of Wierzbicka's Natural Semantic Metalanguage while remaining learnable in weeks. Wierzbicka's full 65-primitive NSM is the long-term target; 16 is the minimum viable expressive set.

**Why THINK as the 16th?**
The original 15 primitives covered physical and relational concepts but had no cognitive primitive. THINK covers: know, understand, believe, imagine, remember — all essential for meta-communication ("I don't understand," "I think so"). It completes the set.

**Why these syllables?**
CV (consonant-vowel) structure — the most universal syllable shape across human languages. Each syllable is 2 characters, maximally short, with distinct consonants within each vowel group to minimize auditory confusion when strung together. Mnemonics where possible (sa→Self, hi→Here, go→Good, na→No, mo→Move, li→Life).

**Why this keyboard layout?**
Home row (SDFGHJKL) holds the 8 most frequent primitives. Top row (WERTYUIO subset) holds medium-frequency. Bottom row (V, N) holds the rarest elemental primitives. Pinkies unused. Thumbs = space. Frequency ordering follows Huffman coding principle — common concepts cost least physical effort.

**Why this embedding model?**
`all-MiniLM-L6-v2` is fast, widely available, well-documented, and produces 384-dimensional embeddings with strong semantic separation. Mean pairwise cosine similarity of 0.321 across the 16 primitives indicates good orthogonality — the primitives are genuinely spread across the semantic space, not clustered.

---

## Composition Examples

The grammar is sequence + position. Subject first, then predicate, then object.

| Sequence | Primitive chain | Natural language |
|---|---|---|
| sa wu du | SELF WANT WATER | I'm thirsty |
| na fu | NOT HEAT | Cold |
| du re | WATER AIR | Cloud / rain / mist |
| sa mo hi | SELF MOVE HERE | I'm coming |
| to na go | OTHER NOT GOOD | You're wrong / that's bad |
| sa te to | SELF THINK OTHER | I understand you |
| na li | NOT ALIVE | Dead / asleep / broken |
| sa wu go ne | SELF WANT GOOD NOW | I need this now |
| hi to li hi | HERE OTHER ALIVE HERE | Hello world |

---

## What Must Not Change Without Versioning

- Primitive names
- Syllable assignments
- Key assignments
- The embedding model used as geometric basis
- The canonical geometry file (`primatap_canonical_embeddings.json`)

Changes to any of the above require a new version number and a migration document explaining what changed and why.

---

*PrimaTap Canonical Primitives v1.0 — Ryan Funk, May 2026*
