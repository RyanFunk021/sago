# Sago — *sa go* — "I am well"

**A language built entirely from universal semantic primitives.**

```
sa go ne hi          →   Hello. I am here and well.
sa wu du             →   I want water.
ba go ma to          →   I love you.
na de na             →   Freedom.
te su na vi          →   Faith.
```

Sago is a constructed language whose entire vocabulary derives from the 65 semantic primes identified by Wierzbicka's [Natural Semantic Metalanguage](https://intranet.secure.griffith.edu.au/schools-departments/natural-semantic-metalanguage) — the smallest set of concepts found in every human language studied over 50 years of cross-linguistic research. Every word in Sago is either a semantic primitive or a composition of primitives. Nothing is borrowed from any natural language.

The language's name is its greeting: **sago** = `sa` (SELF) + `go` (GOOD) = *I am well.*

---

## Why Sago

Natural languages carry enormous cultural cargo. "Democracy," "justice," "love" mean different things to different speakers. Sago is built from the semantic floor — concepts so fundamental they exist in every language humans have ever developed. Two speakers who know Sago's primitives share all meaning without translation.

Sago is not designed to replace natural languages. It is designed to be the *layer beneath them* — a shared semantic foundation where meaning can be verified, not just assumed.

---

## The 90 Phonics

Sago has 90 primitive phonics — semantic units, each a single CV syllable (consonant + vowel: *sa, to, na, wu...*). The phoneme inventory is 18 consonants × 5 vowels = exactly 90 syllables. Every syllable encodes exactly one meaning. No syllable is wasted; no syllable is ambiguous.

Phonics combine into **words**: *nafu* (NOT·HEAT = cold), *fumo* (HEAT·MOVE = fire), *bago* (FEEL·GOOD = joy). Words flow — phonic boundaries are just syllable boundaries, never consonant clusters. The language sounds like speech, not a list.

| Tier | Count | What it adds |
|---|---|---|
| L1 · Core | 8 | Identity, negation, desire, valence, time, place |
| L2 · Physical | 8 | Life, mind, the physical world |
| L3 · Grammar | 16 | Causation, sequence, degree, space, senses |
| L4 · Wierzbicka | 32 | Completes the NSM prime set |
| L5 · Molecules | 26 | Widespread concepts with no single-phonic equivalent |

The full phonic inventory and phonological rules are in [`language/PHONICS.md`](language/PHONICS.md) and [`language/PHONOLOGY.md`](language/PHONOLOGY.md).

---

## Grammar

Sago grammar follows cognitive order: *when → who → what → to what → how.*

```
pa  sa  mo  hi       →   I came here.  (BEFORE SELF MOVE HERE)
ya  to  mo  la  mi   →   Will you leave?  (AFTER OTHER MOVE FAR ?)
sa  ba  lo  du  ga   →   I feel overwhelmed.  (SELF FEEL LIKE WATER BIG)
```

The complete grammar (22 rules, tense/aspect, emotion system, comparatives, modality, discourse) is in [`language/GRAMMAR.md`](language/GRAMMAR.md).

---

## Creating New Words

Sago is an open semantic system. Any concept can be expressed by composing primitives. The [`word_builder.py`](tools/word_builder.py) tool helps you find or create the canonical composition for any concept.

```bash
cd tools
python3 word_builder.py "photosynthesis"
# → lu fa  (LIGHT · PLANT)
#   the process by which plants use light to live and grow

python3 word_builder.py "democracy"
# → ka pu de ro  (MANY · PEOPLE · DO · WORD)
#   governance by the word of many people

python3 word_builder.py "nostalgia"
# → ba go da pa  (FEEL · GOOD · BECAUSE · BEFORE)
#   good feeling caused by the past
```

New words are proposed by opening a pull request adding an entry to [`language/concepts.json`](language/concepts.json).

---

## Concept Dictionary

[`language/concepts.json`](language/concepts.json) is a language-neutral concept browser. Entries are Sago words — not English translations. Any language speaker can look up a concept by domain and find the Sago word and its phonic structure.

```json
{
  "nafu": {
    "word": "nafu",
    "phonics": ["na", "fu"],
    "chord_names": ["NOT", "HEAT"],
    "concept": "absence of heat; low temperature",
    "domain": "physical",
    "level": 2
  },
  "fumo": {
    "word": "fumo",
    "phonics": ["fu", "mo"],
    "chord_names": ["HEAT", "MOVE"],
    "concept": "heat in motion; combustion; fire",
    "domain": "physical",
    "level": 2
  }
}
```

---

## Academic Paper

["Hello World: Sago and the Construction of a Language from Universal Semantic Primitives"](language/sago_paper.md) — Ryan Funk, May 2026.

---

## Repository Structure

```
language/
  PHONICS.md        The 90 primitive phonics (the alphabet)
  GRAMMAR.md       Complete grammar (22 rules)
  PHONOLOGY.md     How phonics flow together into words
  concepts.json    Concept-based dictionary (language-neutral)
  dictionary.json  English lookup table (legacy, 5,001 words)
  sago_paper.md    Academic paper (submission version)

tools/
  word_builder.py  Build or look up any concept
  translate.py     Bidirectional translation
  evaluate.py      Coverage and orthogonality analysis
  phonics.py        Shared phonic definitions module (import this)
  requirements.txt Python dependencies
```

---

## Contributing

Sago needs a speaker community to stabilize its conventions. Three ways to contribute:

1. **Propose a word** — open a PR adding to `language/dictionary.json`
2. **Report a collision** — two compositions for the same concept, or the same composition for two concepts
3. **Translate something** — open an issue with your source text and the Sago output

Word proposals require: the Sago word, its phonic sequence, phonic names, a concept description (language-neutral), and confidence (0.0–1.0).

---

## License

Language specification (PHONICS.md, GRAMMAR.md, PHONOLOGY.md, paper): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — use freely, credit Sago  
Code (tools/): [MIT](LICENSE)  
Dictionary: [CC0](https://creativecommons.org/publicdomain/zero/1.0/) — public domain, no restrictions

---

*sa go — I am well.*  
*Ryan Funk, May 2026*
