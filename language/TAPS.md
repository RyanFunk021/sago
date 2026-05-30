# PrimaTap Canonical Tap Definitions — v1.0

**This is the basis document for the full tap system.**
All implementations reference this version.

**Author:** Ryan Funk  
**Date:** May 2026  
**Total taps:** 90 (64 primes + 26 molecules)  
**Embedding basis:** `sentence-transformers/all-MiniLM-L6-v2`  
**Validation:** geometric verification 14/15 (93%), LLM composition 11/20 (55%)

---

## Architecture

| Level | Count | Total | What it adds |
|---|---|---|---|
| L1 · Core | 8 | 8 | Social skeleton: identity, negation, desire, valence, time, place |
| L2 · Physical | 8 | 16 | Life, action, mind, the four elements |
| L3 · Grammar | 16 | 32 | Time sequence, causation, degree, space, senses, speech |
| L4 · Wierzbicka | 32 | 64 | Completes the NSM 65-prime set |
| L5 · Molecules | 26 | 90 | Widespread composites with no single-tap equivalent in L1–L4 |

**Special modes:**
- Name mode: `we` opens · `we` closes · interior taps spell a name phonetically
- Number mode: CVC syllables — phonologically distinct from all 90 semantic CV taps

**Why CVC for numbers:** All 90 CV syllables (18 consonants × 5 vowels) are exhausted by the semantic system. Number digits must use a different phonological class. CVC (closed) syllables end in a consonant; every semantic CV tap ends in a vowel. A listener always knows: open syllable = meaning, closed syllable = digit. No bracket needed.

**Number digit assignments (base-16):**

| Value | Digit | Pronunciation | | Value | Digit | Pronunciation |
|---|---|---|---|---|---|---|
| 0 | `nun` | like "noun" | | 8 | `dim` | short i |
| 1 | `win` | like "win" | | 9 | `pin` | like "pin" |
| 2 | `tim` | like "Tim" | | A | `zun` | z+oo+n |
| 3 | `ron` | like "Ron" | | B | `gem` | like "gem" |
| 4 | `kan` | k+ah+n | | C | `van` | like "van" |
| 5 | `fen` | f+eh+n | | D | `hin` | h+ih+n |
| 6 | `sim` | like "sim" | | E | `lon` | like "lon" |
| 7 | `bon` | like "bon" | | F | `mem` | like "mem" |

**Nasal-coda rule:** All digits end in a nasal (n or m) — the most universally distinct syllable-final sounds. This maximizes cross-linguistic distinguishability even at speed.

**Number examples:**
- 7 → `bon`
- 16 → `win nun` (1·0 in base-16 = 16₁₀)
- 255 → `mem mem` (FF₁₆)
- 3.14 → `ron · win kan` (decimal point = `·` spoken as a pause)
- Large numbers use place groups: `win nun nun` = 256, `win nun nun nun` = 4096

**For haptic delivery:** Number mode is signaled by a distinct tap rhythm (double-beat), not phonology. The CVC distinction is for the spoken/voice channel only.

---

## L1 · Core 8

The minimum viable communication set. Learnable in days.

| # | Name | Syllable | Meaning | Key |
|---|---|---|---|---|
| 1 | SELF | sa | I, me, the speaker | F |
| 2 | OTHER | to | you, they, any non-self | D |
| 3 | NOT | na | negation, absence, opposite | J |
| 4 | WANT | wu | desire, need, intention | K |
| 5 | GOOD | go | positive, correct, safe | S |
| 6 | BAD | bi | negative, wrong, harmful | L |
| 7 | NOW | ne | present, immediate | G |
| 8 | HERE | hi | this place, proximal | H |

**Base-8 digit map:** na=0  sa=1  to=2  wu=3  go=4  bi=5  ne=6  hi=7

---

## L2 · Physical 16

Adds the living world, action, mind, and elements. Weeks to learn.

| # | Name | Syllable | Meaning | Key |
|---|---|---|---|---|
| 9 | ALIVE | li | living, conscious, animate | E |
| 10 | MOVE | mo | motion, action, change | R |
| 11 | THINK | te | know, understand, believe | U |
| 12 | WATER | du | liquid, fluid | I |
| 13 | HEAT | fu | temperature, thermal energy | W |
| 14 | AIR | re | gas, breath, wind, sky | O |
| 15 | SOLID | ko | matter, hard, tangible, earth | V |
| 16 | LIGHT | lu | visible energy, brightness, color | N |

---

## L3 · Grammar 32

Closes the largest gaps: time sequence, causation, degree, space, senses. Months to learn.

| # | Name | Syllable | Meaning |
|---|---|---|---|
| 17 | BEFORE | pa | prior in time, past |
| 18 | AFTER | ya | subsequent, future |
| 19 | BECAUSE | da | reason, cause, therefore |
| 20 | IF | di | conditional, hypothetical |
| 21 | CAN | pi | ability, possibility |
| 22 | MORE | ma | greater degree, very, much |
| 23 | SAME | si | identical, equal, matching |
| 24 | FAR | la | distant, away from here |
| 25 | ABOVE | va | higher than, over |
| 26 | INSIDE | ja | contained within, interior |
| 27 | FEEL | ba | emotion, sensation — not cognitive |
| 28 | HEAR | ra | auditory sense |
| 29 | SAY | we | speak, express, communicate |
| 30 | MANY | ka | plural, numerous |
| 31 | BODY | bo | physical form, flesh |
| 32 | KIND | pe | type, category, sort |

---

## L4 · Wierzbicka 64

Completes the NSM 65-prime research set. Near full expressive range.

| # | Name | Syllable | Meaning |
|---|---|---|---|
| 33 | SOMEONE | zo | an unspecified person |
| 34 | SOMETHING | ze | an unspecified thing |
| 35 | PEOPLE | pu | humans collectively |
| 36 | ONE | ta | single instance, unit |
| 37 | TWO | ti | a pair |
| 38 | SOME | so | an indefinite quantity |
| 39 | ALL | zu | every instance, universal |
| 40 | FEW | fi | a small number |
| 41 | BIG | ga | large in scale |
| 42 | SMALL | gi | small in scale |
| 43 | KNOW | no | certain knowledge, fact |
| 44 | SEE | vi | visual perception |
| 45 | TOUCH | tu | physical contact |
| 46 | DO | de | intentional action |
| 47 | HAPPEN | ha | event without agent, occur |
| 48 | HAVE | ho | possession, contain |
| 49 | EXIST | za | there is, presence |
| 50 | DIE | gu | cease living |
| 51 | TRUE | su | factual, real, actual |
| 52 | WORD | ro | linguistic unit, name |
| 53 | MAYBE | mi | uncertain, possible |
| 54 | LIKE | lo | similar to, as, in the manner of |
| 55 | VERY | ve | intensifier, to a great degree |
| 56 | NEAR | ni | close to, proximate |
| 57 | BELOW | be | lower than, under |
| 58 | SIDE | ri | lateral, beside |
| 59 | WHEN | wi | at which time |
| 60 | WHERE | wa | at which place |
| 61 | MOMENT | mu | an instant, a point in time |
| 62 | PART | po | a component, piece of a whole |
| 63 | ANOTHER | nu | a different one |
| 64 | THIS | yo | the proximal referent |

---

## L5 · Molecules 26

Concepts that are geometrically novel (< 0.50 similarity to any L4 prime),
empirically widespread across languages, and not cleanly composable from L1–L4.
Ranked by novelty (most novel first).

| # | Name | Syllable | Meaning | Novelty score |
|---|---|---|---|---|
| 65 | TREE | le | woody plant, standing plant | 0.380 |
| 66 | MOON | ge | Earth's satellite, night light | 0.411 |
| 67 | FOOT | fo | lowest part of leg, base | 0.427 |
| 68 | BIRD | bu | flying vertebrate, feathered animal | 0.432 |
| 69 | ROAD | ru | path for travel, route | 0.437 |
| 70 | STAR | se | distant sun, point of night light | 0.439 |
| 71 | DAY | do | period of sunlight, solar cycle | 0.444 |
| 72 | PLANT | fa | rooted living thing, vegetation | 0.451 |
| 73 | MAN | me | adult male human | 0.455 |
| 74 | MOTHER | ku | female parent | 0.456 |
| 75 | TOGETHER | je | in mutual company, jointly | 0.460 |
| 76 | ANIMAL | ki | non-plant living thing, creature | 0.461 |
| 77 | FATHER | hu | male parent | 0.463 |
| 78 | EYE | ye | visual organ | 0.468 |
| 79 | EARTH | he | soil, ground material, the planet | 0.469 |
| 80 | HARD | ji | resistant to deformation, solid surface | 0.473 |
| 81 | SHARP | vo | pointed, cutting edge | 0.475 |
| 82 | MOUTH | vu | oral opening, speaking organ | 0.476 |
| 83 | EAR | jo | auditory organ | 0.478 |
| 84 | ROUND | ju | circular, spherical | 0.481 |
| 85 | TASTE | fe | flavor, gustatory sense | 0.481 |
| 86 | BACK | yi | posterior surface, rear | 0.484 |
| 87 | NIGHT | yu | period of darkness | 0.485 |
| 88 | GROUND | zi | surface underfoot, floor | 0.488 |
| 89 | CLOTH | ke | woven fabric, textile | 0.493 |
| 90 | NOSE | wo | olfactory organ | 0.496 |

---

## Composition Examples

| Tap sequence | Primitives | Meaning |
|---|---|---|
| sa wu du | SELF WANT WATER | thirsty |
| na fu | NOT HEAT | cold |
| du re | WATER AIR | cloud / mist |
| li ko lu hi to | ALIVE SOLID LIGHT HERE OTHER | house sparrow (living solid, bright, near people) |
| li ko lu re | ALIVE AIR LIGHT SOLID | photosynthesis |
| ba go | FEEL GOOD | joy |
| ba bi | FEEL BAD | pain |
| na li | NOT ALIVE | dead |
| sa mo hi | SELF MOVE HERE | I'm coming |
| ka li va ko | MANY ALIVE ABOVE SOLID | birds in a tree |
| sa te to | SELF THINK OTHER | I understand you |

---

## What Is Not In This System

These require companion mechanisms, not more taps:

| Category | Examples | Solution |
|---|---|---|
| Institutional vocabulary | salary, fiscal, database, bureau | Dictionary lookup (Claude API) |
| Proper nouns | Paris, Beethoven, Ryan | Name bracket `we...we` |
| Species names | house sparrow vs. starling | Compositional description + context |
| Numbers | 12,030,455,021 | CVC nasal-coda digits (base-16): `nun win tim ron...` — see number system above |
| Technical terms | algorithm, mitochondria | Dictionary + composition |

---

## Molecules Excluded as Redundant

These 19 molecules were tested but are already geometrically covered by L1–L4 primes (similarity ≥ 0.50). They do not need their own taps.

sound (0.500), smell (0.506), fish (0.509), name (0.517), child (0.523),
between (0.523), house (0.531), heavy (0.533), sun (0.540), pain (0.551),
woman (0.555), again (0.564), food (0.574), sky (0.579), face (0.592),
color (0.595), fire (0.606), long (0.645), hand (0.651)

Note: head (0.499) excluded — composable as `bo va` (BODY ABOVE).

---

## Validation Summary

| Test | Result |
|---|---|
| Mean pairwise similarity (L4, 64 taps) | 0.328 (lower = more orthogonal) |
| Single-tap vocabulary coverage (L5, 90 taps, threshold 0.45) | ~56% of top-5000 English words |
| Pair-composition coverage (L3, 32 taps) | 56.6% — matches L5 singles |
| Vector verification (concept near its primitives) | 14/15 (93%) |
| LLM composition hit rate | 11/20 (55%) |

---

*PrimaTap Canonical Taps v1.0 — Ryan Funk, May 2026*
