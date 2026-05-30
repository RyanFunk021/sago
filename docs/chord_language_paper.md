# PrimaTap: A Universal Semantic Primitive Communication System for Sensory-Impaired Populations

**Ryan Funk**
Independent Research, May 2026
funk.ryan@gmail.com

---

## Abstract

We propose PrimaTap, a bidirectional communication system grounded in semantic primitive theory and information-theoretic encoding, designed for deaf, blind, and deaf-blind individuals. Rather than encoding phoneme-based written language (as in Braille), PrimaTap encodes meaning directly via a compact set of semantic primitives drawn from embedding space analysis of natural language. Primitives are mapped to simultaneous finger chord patterns on a wearable input device, with output delivered via modality-appropriate channels: tactile vibration (deaf-blind), visual glyphs (deaf), or audio tones (blind). Chord assignments follow a Huffman-inspired frequency ordering, minimizing the physical cost of high-frequency concepts. We present a theoretical framework, an NLP-based primitive selection methodology, a proposed chord encoding scheme, and a phased experimental design for human subjects validation. The system is language-agnostic at the primitive layer, suggesting potential applications in cross-linguistic communication.

---

## 1. Introduction

Current assistive communication technology for deaf-blind individuals relies primarily on refreshable Braille displays and tactile fingerspelling. These systems share a fundamental limitation: they encode text — which is itself a representation of spoken phonemes — rather than meaning directly. A deaf-blind person reading Braille must traverse the chain: tactile pattern → letter → phoneme → word → meaning. Each step introduces cognitive overhead and presupposes familiarity with a spoken language.

Augmentative and Alternative Communication (AAC) devices for non-verbal individuals face similar constraints, typically offering grids of pictographic symbols or text prediction — systems that are slow, visually dependent, or tied to a specific natural language.

We propose a different approach: **encode meaning at the primitive level**, bypassing phonological and orthographic representation entirely. The system operates on the hypothesis that a small vocabulary of universal semantic primitives, arranged into compositional sequences, can express a rich range of communicative content more efficiently than character-based encoding — and that such primitives can be mapped to learnable, ergonomically optimized finger chord patterns.

### 1.1 Contributions

1. A methodology for selecting semantic primitives using NLP embedding space analysis
2. A Huffman-frequency-ordered 4-bit finger chord encoding scheme
3. A compositional grammar enabling complex meaning from primitive sequences
4. A phased experimental protocol for validating primitive learnability
5. A unified bidirectional interface applicable across deaf, blind, and deaf-blind populations

---

## 2. Background and Related Work

### 2.1 Braille and Tactile Communication

Standard Braille uses a 6-bit encoding (2×3 dot cell, 64 combinations) to represent letters, numbers, and punctuation. Grade 2 Braille introduces contractions that partially compress frequent words, but the system remains fundamentally phoneme-dependent. Refreshable Braille displays update electronically and allow real-time text consumption at rates of approximately 100 words per minute for expert readers [CITATION].

Tactile communication methods for deaf-blind individuals also include Lorm (palm touch patterns), Malossi (hand position alphabet), and Tadoma (feeling laryngeal vibrations). Each encodes at the phoneme or letter level.

### 2.2 Natural Semantic Metalanguage

Wierzbicka (1972, 1996) proposed that all human languages share a set of semantic primitives — concepts expressible in every language and reducible to no simpler terms. Her Natural Semantic Metalanguage (NSM) identifies approximately 65 such primitives, including: I/YOU, SOMEONE, SOMETHING, THINK, KNOW, WANT, FEEL, SEE, HEAR, GOOD, BAD, BIG, SMALL, NOW, BEFORE, AFTER, HERE, ABOVE, BELOW, ALIVE, DIE [CITATION]. This work suggests that a primitive-based communication layer could be genuinely language-universal.

### 2.3 Constructed Languages and Compositional Minimalism

Toki Pona (Lang, 2001) is a constructed language with approximately 120 root words, designed so that all concepts are expressed compositionally. "Rain" is expressed as *telo sewi* (water-sky); "ice" as *telo lete* (water-cold). Native speakers report that the constraint forces conceptual clarity. This validates the cognitive plausibility of compositional primitive-based communication [CITATION].

### 2.4 Chord Keyboards and Stenography

Stenographic chord keyboards have been used in court reporting since the 19th century. A modern steno machine features ~22 keys; operators press simultaneous chords representing syllables or whole words, achieving speeds exceeding 225 words per minute [CITATION]. The chord input paradigm demonstrates that simultaneous multi-key input is learnable and can dramatically exceed sequential key input in throughput.

### 2.5 NLP Embedding Spaces

Word embedding models (Mikolov et al., 2013; Devlin et al., 2019) represent lexical items as dense vectors in high-dimensional space, where geometric relationships encode semantic relationships. Sentence Transformers (Reimers & Gurevych, 2019) extend this to sentence-level representations. Crucially, compositional operations in embedding space preserve semantic relationships: vec(WATER) + vec(AIR) approximates concepts in the semantic neighborhood of *cloud*, *mist*, and *steam* [CITATION].

### 2.6 Information-Theoretic Encoding

Huffman coding (Huffman, 1952) assigns shorter codewords to more frequent symbols, minimizing expected codeword length. Shannon's source coding theorem bounds the theoretical minimum. Applied to a chord keyboard, this principle dictates that primitives appearing most frequently in natural communication should be assigned to the physically simplest (fewest simultaneous fingers) chord patterns.

---

## 3. System Design

### 3.1 Semantic Primitive Selection

We propose selecting primitives via the following procedure:

1. Encode a candidate set of ~100 fundamental concepts using a sentence transformer model (e.g., `all-MiniLM-L6-v2`)
2. Compute pairwise cosine similarity across all candidates
3. Apply greedy maximum-coverage selection: iteratively select the concept whose embedding is furthest from all already-selected concepts
4. Validate that the selected set spans the major axes of the embedding space (via PCA explained variance)
5. Cross-reference against Wierzbicka's NSM primitives for linguistic grounding

**Preliminary results** (N=16 candidates, 384-dimensional embeddings): The 16-word candidate set achieves a mean pairwise cosine similarity of 0.47, indicating moderate orthogonality. Compositional vector averaging correctly identifies semantic neighbors for 3 of 5 tested combinations when searched against the full primitive vocabulary. Expansion to a full English vocabulary is expected to improve composition accuracy substantially.

**Proposed 15-primitive vocabulary:**

| # | Primitive | Semantic domain |
|---|---|---|
| 1 | SELF | Identity |
| 2 | OTHER | Identity |
| 3 | NOT | Logic |
| 4 | WANT | Intention |
| 5 | GOOD | Valence |
| 6 | BAD | Valence |
| 7 | NOW | Time |
| 8 | HERE | Space |
| 9 | ALIVE | Biology |
| 10 | MOVE | Action |
| 11 | WATER | Element |
| 12 | AIR | Element |
| 13 | HEAT | Element |
| 14 | SOLID | Element |
| 15 | LIGHT | Perception |

### 3.2 Chord Encoding

The input device consists of four primary sensors corresponding to: Left Index (LI), Left Ring (LR), Right Index (RI), Right Ring (RR). Each sensor is binary (pressed / not pressed), yielding 2⁴ = 16 combinations. Excluding the null chord (0000, used as a delimiter/space), 15 combinations are available — exactly matching our primitive vocabulary.

Chords are assigned to primitives in inverse frequency order: the most common primitives in natural communication receive the physically easiest chords.

**Ergonomic comfort ranking:**

| Tier | Pattern | Description | Count |
|---|---|---|---|
| 1 | `1000` `0100` `0010` `0001` | Single finger | 4 |
| 2 | `1100` `0011` | Two fingers, same hand | 2 |
| 3 | `1010` `0101` | Both index / both ring | 2 |
| 4 | `1001` `0110` | Diagonal cross-hand | 2 |
| 5 | `1110` `1101` `1011` `0111` | Three fingers | 4 |
| 6 | `1111` | All four fingers | 1 |

**Frequency-ordered assignment:**

| Chord | Primitive | Frequency rationale |
|---|---|---|
| `1000` | SELF | Appears in nearly every utterance |
| `0001` | OTHER | Appears in nearly every utterance |
| `0100` | NOT | Negation is universal |
| `0010` | WANT | Core communicative intent |
| `1100` | GOOD | Constant feedback signal |
| `0011` | BAD | Constant feedback signal |
| `1010` | NOW | Temporal reference |
| `0101` | HERE | Spatial reference |
| `1001` | ALIVE | Body/health state |
| `0110` | MOVE | Action primitive |
| `1110` | WATER | Elemental |
| `0111` | AIR | Elemental |
| `1101` | HEAT | Elemental |
| `1011` | SOLID | Elemental |
| `1111` | LIGHT | Elemental |

### 3.3 Compositional Grammar

Meaning is expressed as sequences of primitives separated by the null chord delimiter. The system is initially agnostic to word order, treating primitive sequences as unordered semantic sets. As users advance, a simple positional grammar may be introduced:

- **Subject position** (first chord): agent of action
- **Predicate position** (second chord): action or state
- **Object position** (third chord): patient or destination

**Example utterances:**

| Chord sequence | Semantic content | Natural language approximate |
|---|---|---|
| SELF + WANT + WATER | {agent=SELF, intent=WANT, object=WATER} | I'm thirsty |
| NOT + GOOD | {valence=NOT-GOOD} | Bad / pain / discomfort |
| SELF + MOVE + HERE | {agent=SELF, action=MOVE, destination=HERE} | I'm coming |
| WATER + AIR | {elements=WATER,AIR} | Cloud / rain / mist |
| NOT + ALIVE | {state=NOT-ALIVE} | Dead / sleeping / unconscious |

### 3.4 Full System Pipeline

A critical design principle: **the speaking partner requires no training and no special input device.** They speak naturally. The system handles all translation.

**Hearing-to-PrimaTap (inbound):**
```
Speaker utters natural language
    → Speech-to-text (existing ASR, e.g. Whisper)
    → NLP model maps utterance to primitive sequence
    → Device actuates corresponding finger patterns on recipient
```

**PrimaTap-to-hearing (outbound):**
```
User taps finger chord sequence
    → Chord decoder maps to primitive sequence
    → Language model reconstructs natural language utterance
    → Text-to-speech delivers spoken output to hearing partner
```

This pipeline requires no behavioral change from the hearing partner. The AI is the interpreter, operating bidirectionally in real time. The PrimaTap user is the only person who interacts with the chord interface.

**Peer-to-peer (PrimaTap-to-PrimaTap):**

When both communicators are PrimaTap users, the translation layers are bypassed entirely. Chords map directly to primitives on the receiving device. This is the highest-bandwidth mode: no natural language encoding or decoding, no ambiguity introduced by lexical choice, no phonological noise. Two users operating natively at the primitive layer communicate with a fidelity unavailable in any natural language channel.

### 3.5 Output Modalities

The same primitive vocabulary is delivered via different output channels depending on population:

| Population | Inbound (receiving) | Outbound (sending) |
|---|---|---|
| Deaf-blind | Vibration motors on fingertips | Finger chord taps |
| Deaf | Visual glyph display | Finger chord taps |
| Blind | Audio tones or spoken primitive names | Finger chord taps |
| Hearing partner | Spoken natural language (TTS) | Natural speech (ASR) |
| PrimaTap-to-PrimaTap | Direct vibration/glyph, no translation | Direct chord, no translation |

---

## 4. Experimental Design

We propose a three-phase experimental protocol.

### Phase 1: Primitive Discrimination

**Participants:** Sighted, hearing adults (n=20). Deaf-blind subjects require IRB approval and institutional partnership; sighted adults provide an initial learnability bound.

**Protocol:** Participants wear a 4-motor vibrotactile glove. The system delivers one of 15 patterns. Participants select the corresponding primitive from a visual reference card. Trials proceed in spaced repetition order (Leitner box schedule). Reward (positive feedback, small snack reward) is delivered on correct identification.

**Measures:** Accuracy over trials, learning curve slope, per-primitive confusion matrix, time-to-criterion (≥90% accuracy on all 15 primitives).

**Hypothesis:** Participants will reach criterion within 3 hours of practice, distributed over multiple sessions.

### Phase 2: Compositional Learning

**Protocol:** Participants who reach Phase 1 criterion are introduced to 2-chord sequences. They are shown a picture or concept (e.g., a cloud) and must produce the correct 2-chord sequence (WATER + AIR). Feedback is provided.

**Measures:** Accuracy on novel compositions not seen during training; transfer to 3-chord sequences.

**Hypothesis:** If semantic composition transfers, participants will correctly produce novel combinations at above-chance rates without explicit training.

### Phase 3: Bidirectional Communication

**Protocol:** Pairs of participants communicate exclusively via the PrimaTap system to complete referential communication tasks (e.g., describe an image to a partner who must select it from an array).

**Measures:** Task completion rate, communication speed (primitives per minute), subjective workload (NASA-TLX).

---

## 5. Discussion

### 5.1 Cognitive Plausibility

The primitive-first approach aligns with evidence that human conceptual structure is organized around a small set of basic-level categories (Rosch, 1978) and that language production involves selection from pre-linguistic conceptual representations before lexicalization. PrimaTap may interface more directly with pre-linguistic thought than phoneme-based systems.

### 5.2 Information Density

A 4-bit chord with Huffman assignment achieves an expected code length approaching the entropy of primitive usage frequencies. If the top 4 primitives (SELF, OTHER, NOT, WANT) account for 40% of communicative content — plausible given their role as grammatical and intentional operators — then the average message is transmitted in 2-3 chords, comparable in density to syllable-level steno.

### 5.3 Limitations

The primitive vocabulary proposed here is preliminary and requires empirical validation of coverage (can subjects express their intended meaning?) and distinctiveness (are chords reliably discriminated?). The compositional semantics are intentionally underspecified; a richer grammar will likely be necessary for complex propositions.

Deaf-blind human subjects research requires significant institutional infrastructure: IRB approval, partnership with schools for the deaf-blind, and trained interventionists.

### 5.4 Extension to 6-bit Encoding

Adding thumb sensors (LT, RT) extends the system to 6 bits = 64 combinations, matching Braille's expressive capacity while remaining language-agnostic. This would allow encoding of common composite concepts as single chords (e.g., a dedicated chord for THIRSTY = WANT+WATER, once learned), trading physical complexity for communicative speed.

### 5.5 Cognitive Development Hypothesis: The Primitive-Native Advantage

We propose an additional hypothesis with significant implications beyond assistive technology: **children raised on PrimaTap as a primary communication system may develop enhanced compositional reasoning relative to controls.**

Natural languages are historically accumulated systems full of redundancy, ambiguity, irregular exceptions, and phonological artifacts that carry no semantic content. A child acquiring English learns that "bad" and "not good" are near-synonyms, that tense is marked inconsistently, and that thousands of words encode concepts that could be composed from smaller parts. This richness is generative but also introduces cognitive noise.

A child whose primary language is PrimaTap operates under different constraints. Every concept must be explicitly constructed from primitives. Ambiguity is structurally reduced — there is no word for "bank" that conflates financial institution with riverbank; each meaning requires a distinct primitive combination. Grammatical relations are encoded positionally, not morphologically, eliminating irregular verb conjugations and gendered agreement.

This is consistent with the **Sapir-Whorf hypothesis** in its weak form: the structure of a communication system influences, though does not determine, the cognitive patterns of its users. Evidence from related domains supports this direction. Users of Toki Pona (a 120-root constructed language) report that its constraints force conceptual precision [CITATION]. Mathematicians routinely note that a well-chosen notation makes previously intractable problems tractable — Leibniz's calculus notation accelerated the adoption and extension of calculus across Europe, while Newton's notation retarded it in England for over a century [CITATION]. Programmers trained in typed functional languages demonstrate measurable differences in reasoning about program correctness [CITATION].

The PrimaTap child who communicates with hearing parents through an interpreter today is not disadvantaged — they are training on a system with a higher signal-to-noise ratio. The interpreter bridges the gap in the near term. In the long term, the native PrimaTap thinker may possess a compositional reasoning advantage that compounds over a lifetime.

This hypothesis is testable via longitudinal cognitive assessment of PrimaTap-using children compared to matched controls on tasks measuring compositional reasoning, analogy, and abstract problem-solving. We flag it here as a direction warranting dedicated investigation.

A further and more striking prediction follows: **two PrimaTap-native users communicating with each other** operate at a qualitatively different level than any natural language exchange. The translation layers — ASR, NLP mapping, TTS — are bypassed entirely. Both parties share the same primitive vocabulary and chord encoding. The result is a communication channel with no lexical ambiguity, no phonological noise, no grammatical irregularity, and no meaning lost to translation. Whether this peer-to-peer primitive channel enables faster, more precise, or cognitively richer communication than natural language is an open empirical question — and one that did not exist before this system.

---

## 6. Future Work

- Large-vocabulary composition search: evaluate whether NLP vector arithmetic in a 50,000-word vocabulary reliably recovers target concepts from primitive combinations
- AI-assisted primitive optimization: use a language model to propose a primitive set that maximizes coverage of the most common communicative intents
- Hardware prototype: Raspberry Pi + 8 vibration motors (~$200 BOM) for Phase 1 experiments
- Glyph system design: develop a visual symbol set for the deaf population output modality
- Cross-linguistic validation: test whether the primitive layer is interpreted consistently across speakers of typologically distinct languages

---

## 7. Conclusion

PrimaTap proposes a fundamental rethinking of assistive communication: rather than encoding phoneme-based text, encode pre-linguistic meaning via a compact, learnable set of semantic primitives. The system is bidirectional, modality-flexible, language-agnostic, and grounded in both linguistic theory (NSM) and information theory (Huffman coding). Preliminary NLP experiments support the geometric separability of the proposed primitive vocabulary. A phased experimental protocol provides a path from theoretical proposal to empirical validation.

If human subjects can learn to discriminate 15 tactile patterns and extend them compositionally — a hypothesis supported by the learnability of Braille (6-bit) and steno (22-key chords) — PrimaTap could provide a faster, more cognitively natural communication channel for millions of people worldwide.

---

## References

*(To be completed with full citations)*

- Huffman, D.A. (1952). A method for the construction of minimum-redundancy codes. *Proceedings of the IRE*.
- Lang, S. (2001). *Toki Pona: The Language of Good*. Publisher.
- Mikolov, T. et al. (2013). Efficient estimation of word representations in vector space. *ICLR*.
- Reimers, N. & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-networks. *EMNLP*.
- Rosch, E. (1978). Principles of categorization. In *Cognition and Categorization*.
- Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal*.
- Wierzbicka, A. (1972). *Semantic Primitives*. Athenäum.
- Wierzbicka, A. (1996). *Semantics: Primes and Universals*. Oxford University Press.
