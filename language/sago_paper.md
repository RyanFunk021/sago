# Hello World: Sago and the Construction of a Language from Universal Semantic Primitives

**Ryan Funk**  
Independent Researcher  
funk.ryan@gmail.com

*May 2026*

---

## Abstract

We present Sago, a constructed language built entirely from the semantic primes identified by Wierzbicka's Natural Semantic Metalanguage (NSM) research program. Where NSM treats primes as a *metalanguage* for semantic analysis, Sago promotes them to an *object language* — a complete system for human communication grounded in meaning rather than phonemes. The vocabulary comprises 90 semantic units: approximately 59 taps corresponding directly to NSM's 65 primes, 5 physically-grounded additions in L2 not present in the strict prime list, and 26 geometrically novel semantic molecules. A defining constraint of the design is phonological completeness: the full inventory of consonant-vowel (CV) syllables producible under an 18-consonant, 5-vowel phoneme set yields exactly 90 forms, providing a one-to-one mapping between phonological space and semantic content with no residual ambiguity. We document the grammar in full and evaluate the system computationally using sentence-transformer embeddings (all-MiniLM-L6-v2) and large-language-model semantic judgment. Vocabulary evaluation shows that 90 single taps cover 54.7% of the top-5,000 English words by frequency, rising to 56.6% with two-tap compositions using only 32 taps — a finding consistent with Zipf's law predictions about the expressive efficiency of a small primitive set. A 5,000-word English-to-Sago dictionary reveals that 70.8% of common English words are compositionally expressible, 20.0% are institutional (requiring proper-noun treatment or dictionary lookup), and 9.2% are single-tap primitives. Back-translation experiments using Claude-as-judge yield 3.69/5 (74%) meaning preservation for direct communication and 1.00/5 for literary texts — a result we argue is correct and expected: literary content depends on metaphor, irony, and cultural register that are explicitly outside the scope of semantic primitive encoding. The grammar reveals unexpected compositional insights: *freedom* encodes as NOT·DO·NOT (the absence of the prevention of action), *faith* as THINK·TRUE·NOT·SEE (believing truly without seeing), and *courage* as DO·TOGETHER·FEEL·BAD (acting while afraid). These emergent structures suggest that the NSM prime set has semantic depth beyond its metalinguistic purpose.

**Keywords:** semantic primitives, Natural Semantic Metalanguage, constructed language, universal semantics, semantic composition, back-translation evaluation

---

## 1. Introduction

The search for a universal human language has occupied philosophers and linguists for centuries. Leibniz envisioned a *characteristica universalis* — a symbolic calculus of concepts from which all human thought could be derived (1666/1989). Wilkins constructed an elaborate conceptual taxonomy in *An Essay Towards a Real Character* (1668). Esperanto and Interlingua sought universality through phonological regularity applied to the European lexicon (Okrent, 2009). Each approach treated universality as a property of *form* — standardized grammar, international vocabulary, logical symbols — rather than a property of *meaning*.

The Natural Semantic Metalanguage (NSM) research program, developed by Wierzbicka beginning in 1972 and elaborated across five decades with Goddard and others, takes the opposite approach. NSM identifies a small set of semantic primes — concepts that are indefinable, universal across all human languages, and lexicalized in every natural language studied (Wierzbicka, 1996; Goddard, 2008). The current NSM inventory stands at 65 primes, including concepts such as I, YOU, KNOW, FEEL, WANT, HAPPEN, KIND, and BEFORE. These primes are not English words — they are universal semantic atoms that English words *express*, and every human language has words expressing the same atoms (Goddard & Wierzbicka, 2002).

NSM is designed as a metalanguage: a tool for analyzing other languages' semantics, not a language in itself. No one speaks NSM natively. Utterances in NSM are deliberately stilted because the goal is transparency, not fluency.

Sago asks a different question: what happens if we treat NSM primes not as an analytical tool but as a *foundation for communication*? Can a language built entirely from semantic primitives function as a medium for human expression? And what does the structure of such a language reveal about the nature of meaning?

This paper documents Sago v1.0 — its vocabulary design, phonological system, tiered acquisition model, grammar, and computational evaluation. We report two primary empirical findings: (1) vocabulary coverage and compositional expressibility across 5,000 common English words, and (2) back-translation performance across two registers — simple direct communication and literary text — evaluated by both distributional similarity and LLM-based semantic judgment. We discuss the philosophical implications of emergent compositions and identify the genuine limits of the approach.

---

## 2. Theoretical Background

### 2.1 The Natural Semantic Metalanguage

The NSM hypothesis holds that all lexical meanings in all human languages can be analyzed using a small set of semantically primitive concepts. These primes have three defining properties: they are *indefinable* (cannot be explained without circularity), *universal* (found in every language studied), and *innate* (present in all languages including those without documented contact).

Wierzbicka's original 1972 proposal identified 14 primes. Successive cross-linguistic research, including detailed studies of Polish, Japanese, Mandarin, Yankunytjatjara, Koromu, Amharic, Lao, and approximately 90 other languages, expanded and refined the set to its current 65 (Goddard, 2011). The primes are typically given in English orthography but represent universal semantic atoms: I, YOU, SOMEONE, SOMETHING, PEOPLE, BODY, KIND, PART, THIS, THE SAME, OTHER/ELSE, ONE, TWO, SOME, ALL, MUCH/MANY, LITTLE/FEW, GOOD, BAD, BIG, SMALL, KNOW, THINK, WANT, FEEL, SEE, HEAR, SAY, WORDS, TRUE, HAPPEN, DO, MOVE, THERE IS, LIVE, DIE, WHEN/TIME, NOW, BEFORE, AFTER, A LONG TIME, A SHORT TIME, FOR SOME TIME, MOMENT, WHERE/PLACE, HERE, ABOVE, BELOW, FAR, NEAR, SIDE, INSIDE, NOT, MAYBE, CAN, BECAUSE, IF, VERY, MORE, LIKE/AS/WAY.

Critical to our design, Goddard (2011) also identifies *semantic molecules*: concepts that are not primitively universal but are cross-linguistically widespread and semantically stable — TREE, BIRD, MOTHER, FOOT, HAND, EYE, WATER, FIRE, and approximately 50 others. Molecules differ from primes in that they can be *defined* using primes, but their cross-linguistic ubiquity makes them practical lexical atoms.

### 2.2 Challenges to NSM Universality

The strongest empirical challenge to NSM universality comes from Everett's (2005) analysis of Pirahã, an Amazonian language claimed to lack recursion, number terms, color terms, and several proposed primes. Wierzbicka (2007) and Levinson & Evans (2010) dispute the Pirahã findings on methodological grounds, noting that surface absence of a prime's *expression* does not imply conceptual absence. The debate remains open. Sago's position is pragmatic: NSM's 50-year cross-linguistic research record, spanning languages from Lao to Arrernte to Wolof, constitutes the strongest empirical foundation available for universal semantic structure. We treat the prime set as a working assumption while acknowledging genuine uncertainty at the margins.

### 2.3 Constructed Languages and Semantic Grounding

Prior constructed language projects have not been grounded in empirical semantic universals. Esperanto regularizes European morphosyntax but inherits European vocabulary with all its cultural specificity (Sapir, 1931). Lojban (Cowan, 1997) pursues logical unambiguity through predicate calculus but makes no claim about semantic universality. Toki Pona (Lang, 2014) uses approximately 120 words derived from natural language roots, sacrificing universality for simplicity. None of these systems grounds vocabulary selection in cross-linguistic empirical research.

Sago's distinguishing feature is that every content tap corresponds to a semantic prime or molecule with documented cross-linguistic validity — not a word borrowed from a natural language, and not a concept stipulated by a designer.

---

## 3. Vocabulary System Design

### 3.1 The 90-Tap Inventory

Sago organizes 90 semantic units into five acquisition tiers. The tiered structure allows productive use from the first eight taps while ensuring full semantic range requires the complete inventory.

**L1 · Core 8** (learnable in days): SELF, OTHER, NOT, WANT, GOOD, BAD, NOW, HERE. These eight taps cover identity, negation, desire, valence, time, and location — the minimum viable set for expressing needs, states, and basic social communication.

**L2 · Physical 16**: ALIVE, MOVE, THINK, WATER, HEAT, AIR, SOLID, LIGHT. Adds the physical world and mental states to L1.

**A note on NSM alignment:** L1, L3, and L4 map directly to Wierzbicka's 65 primes, with two terminological adjustments. First, NSM distinguishes I (speaker) and YOU (addressee) as separate primes; Sago collapses these into SELF (speaker) and OTHER (all non-speakers), a deliberate simplification that trades second/third-person precision for a cleaner pronoun system. Second, NSM's three temporal duration primes — A LONG TIME, A SHORT TIME, and FOR SOME TIME — are handled compositionally: BIG·MOMENT, SMALL·MOMENT, and MORE·MOMENT respectively, rather than assigned dedicated taps.

L2 is the one tier that extends beyond the strict NSM prime list. WATER appears in NSM as a *semantic molecule* (Goddard, 2011), not a prime; HEAT, AIR, SOLID, and LIGHT do not appear in NSM at all. These five taps were added as physically-grounded prerequisites for any communicative system operating in the natural world. They are pre-theoretically necessary — a language that cannot distinguish water from air from heat cannot describe even the most basic environment — and their inclusion is a deliberate design extension, not a claim of NSM primeness. The honest accounting: approximately 59 of Sago's 64 L1–L4 taps correspond directly to NSM primes; 5 are practical additions; and the 26 L5 molecules follow Goddard's (2011) molecule framework.

**L3 · Grammar 32**: BEFORE, AFTER, BECAUSE, IF, CAN, MORE, SAME, FAR, ABOVE, INSIDE, FEEL, HEAR, SAY, MANY, BODY, KIND. These taps are primarily grammatical — they provide the logical and syntactic connectives needed for complex expression.

**L4 · Wierzbicka 64**: 32 additional NSM primes, substantially completing the empirically validated prime set. Includes SOMEONE, SOMETHING, PEOPLE, ONE, TWO, SOME, ALL, FEW, BIG, SMALL, KNOW, SEE, TOUCH, DO, HAPPEN, HAVE, EXIST, DIE, TRUE, WORD, MAYBE, LIKE, VERY, NEAR, BELOW, SIDE, WHEN, WHERE, MOMENT, PART, ANOTHER, THIS.

**L5 · Molecules 90**: 26 semantic molecules selected for geometric novelty. Each L5 tap was required to have cosine similarity < 0.50 to all existing L1–L4 taps as measured in the all-MiniLM-L6-v2 embedding space (384 dimensions), confirming that the molecule encodes genuinely new semantic territory. The 26 molecules are: TREE, MOON, FOOT, BIRD, ROAD, STAR, DAY, PLANT, MAN, MOTHER, TOGETHER, ANIMAL, FATHER, EYE, EARTH, HARD, SHARP, MOUTH, EAR, ROUND, TASTE, BACK, NIGHT, GROUND, CLOTH, NOSE.

Of the 46 molecules tested, 19 were excluded because they fell within the semantic neighborhood of existing primes (similarity ≥ 0.50). These included SOUND, SMELL, FISH, HAND, CHILD, BETWEEN, HOUSE, HEAVY, SUN, WOMAN, AGAIN, FOOD, SKY, FACE, COLOR, FIRE, LONG, and HAND — all geometrically redundant given the prime set.

### 3.2 Phonological Completeness

Every Sago semantic tap is a CV (consonant-vowel) syllable. The phoneme inventory consists of 18 consonants — /p, t, k, b, d, g, m, n, f, s, h, v, z, l, r, w, j, y/ — and 5 vowels — /a, e, i, o, u/. The product is 18 × 5 = 90 CV syllables: exactly the number of semantic taps.

This phonological completeness is a structural constraint, not a coincidence of design. It means that the semantic system and the phonological system are in perfect bijection: every CV syllable in this phoneme space encodes exactly one semantic primitive, and no CV syllable is available for any other purpose. The property provides an unambiguous parsing guarantee: any CV syllable encountered in Sago speech is a semantic tap.

### 3.3 Tiered Acquisition

The five-tier structure aligns Sago acquisition with patterns observed in natural language development (Pinker, 1994). L1's eight taps provide a productive communication system from the first hours of instruction — a learner can express needs, negation, and basic social states immediately. Each tier adds expressiveness, and the meaning of previously learned taps remains stable as new taps are introduced. This property — *tier monotonicity* — ensures that communication between learners at different acquisition stages is productive, because lower-level taps are a subset of higher-level vocabularies.

---

## 4. Grammar

Sago grammar is defined by 22 rules organized around a core principle: *cognitive order equals tap order*. Tap sequences follow the natural sequence of conceptual attention — time frame, then topic, then action, then patient, then modifiers. This ordering mirrors topic-prominent typology documented across Japanese, Mandarin, Korean, Turkish, and related languages (Li & Thompson, 1976), and is grounded in cognitive-linguistic research on the relationship between conceptual structure and linguistic form (Langacker, 1987; Talmy, 2000).

### 4.1 Core Syntax

The canonical sentence structure is: `[TIME] TOPIC PREDICATE [PATIENT] [MODIFIERS]`

Sago eliminates the copula entirely. Topic-attribute juxtaposition is sufficient: `sa go` (SELF GOOD) = "I am well." This is typologically motivated — copula-drop is grammatical in Russian present tense, Arabic present tense, and numerous other languages (Stassen, 1997).

Tense is expressed sentence-initially using dedicated taps: `pa` (BEFORE) for past, `ya` (AFTER) for future, `mu` (MOMENT) for narrative instants. The aspect system distinguishes progressive (`ne` before predicate), habitual (`ma` after predicate), perfect (topic-initial `pa`), and ingressive (`ya` after predicate).

### 4.2 Negation

`na` (NOT) immediately precedes the element it negates, with tight scope. This means `sa na wu du` (SELF NOT-WANT WATER = "I don't want water") differs from `na sa wu du` (NOT-SELF WANT WATER = "someone other than me wants water") — structurally similar to negative polarity behavior across many languages (Klima, 1964).

### 4.3 Emotion Encoding

The initial vocabulary design produced a critical collision: LOVE, JOY, and PRIDE all mapped to `ba go ma` (FEEL GOOD MORE), while ANGER and HATE both mapped to `ba bi ma` (FEEL BAD MORE). This collision was discovered computationally when a 5,000-word dictionary generation found identical encodings for these distinct emotion terms.

The resolution draws on the cognitive theory of emotions (Ortony, Clore & Collins, 1988), which defines emotions by their *appraisal structure* — the cognitive evaluation that produces the emotional response. Ortony et al. distinguish emotions by their objects: events, agents, and objects; and by the evaluative valence applied to each. Sago encodes this structure directly through **directedness** — what the emotional response is *about*:

| Emotion | Encoding | Structure |
|---|---|---|
| Joy | `ba go za` | FEEL GOOD EXIST — about existence itself |
| Love | `ba go ma to` | FEEL GOOD MORE OTHER — toward another |
| Pride | `ba go da sa` | FEEL GOOD BECAUSE SELF — caused by oneself |
| Gratitude | `ba go da to` | FEEL GOOD BECAUSE OTHER — caused by another |
| Anger | `ba bi ma to` | FEEL BAD MORE OTHER — directed at another |
| Grief | `ba bi da na za` | FEEL BAD BECAUSE NOT-EXIST — about loss |
| Shame | `ba bi da sa de bi` | FEEL BAD BECAUSE SELF DO BAD |
| Fear | `ba bi da ya ze` | FEEL BAD BECAUSE AFTER SOMETHING |
| Courage | `de je ba bi` | DO TOGETHER FEEL BAD — acting while afraid |

The directedness model makes Sago's emotion system formally more precise than most natural languages, which rely on polysemous labels (the English word *shame* covers guilt, embarrassment, and mortification). Importantly, the structural distinctions are not arbitrary — they correspond to the cognitive appraisal differences that Ortony et al. identify as definitionally constitutive of each emotion.

### 4.4 Extended Grammar

The full grammar covers 22 rules including: comparatives (`sa ga ma lo to` = SELF BIG MORE LIKE OTHER = "I am bigger than you"), imperatives (subject-drop: `mo hi` = "Come!"), reflexives (`si` after verb: `sa vi si` = "I see myself"), reciprocals (`si je` after verb: `to ba go si je` = "they love each other"), reported speech (`we to [content]`), metaphor convention (`lo` before composition marks figurative use: `sa ba lo du ga` = "I feel like an ocean"), scalar particles (only, also, even, still, already, not yet, barely), modality (must = `na pi na` = NOT-CAN-NOT; should = `go pi` = GOOD CAN), and an epistemic certainty scale from `su` (certain) through `ma mi` (probable), `mi` (possible), `fi mi` (unlikely), to `na pi ha` (impossible).

---

## 5. Empirical Evaluation

### 5.1 Methodology

All evaluations use the `sentence-transformers/all-MiniLM-L6-v2` model (Reimers & Gurevych, 2019), producing 384-dimensional sentence embeddings, and word frequency lists from the `wordfreq` library (Speer et al., 2018). The 5,000-word dictionary and back-translation quality judgments both use Claude Haiku (Anthropic, 2024) as a computational tool. Readers should note that this creates a degree of methodological circularity — the same class of model that assisted in building the dictionary was used to evaluate its quality. We treat the results as a preliminary computational investigation; validation by human speakers and independent translators remains necessary before stronger claims can be made.

### 5.2 Semantic Orthogonality

A well-designed semantic vocabulary should maximize coverage while minimizing redundancy. We measured mean pairwise cosine similarity across tap subsets as an orthogonality proxy (lower = more orthogonal = better):

| Tier | Mean pairwise cosine similarity |
|---|---|
| L1 · Core 8 | 0.401 |
| L2 · Physical 16 | 0.328 |
| L3 · Grammar 32 | 0.334 |
| L4 · Wierzbicka 64 | 0.328 |
| L5 · Molecules 90 | 0.314 |

Orthogonality is stable across tiers (0.31–0.40), indicating that the progressive addition of taps does not substantially increase semantic redundancy. The slight drop from L1 to L2 reflects the L1 taps' intentional semantic breadth — eight taps must cover the broadest possible territory.

### 5.3 Vocabulary Coverage

Single-tap coverage — the fraction of top-5,000 English words within cosine similarity threshold 0.45 of at least one tap — follows a smooth curve across tiers:

| Tier | Single-tap coverage |
|---|---|
| L1 · Core 8 | 8.4% |
| L2 · Physical 16 | 16.6% |
| L3 · Grammar 32 | 25.6% |
| L4 · Wierzbicka 64 | 39.7% |
| L5 · Molecules 90 | 54.7% |

Pair composition — combining any two L3 taps — reaches 56.6% coverage using only 32 taps, essentially matching the full 90-tap single-tap coverage. This finding is consistent with theoretical predictions from combinatorial semantics: a well-chosen small vocabulary combined compositionally can match the coverage of a larger vocabulary used atomically.

The gap words — high-frequency English words not covered by 90 single taps or two-tap pairs — are predominantly institutional: *salary, fiscal, bureau, database, algorithm, parliament, mortgage*. These are not primitive semantic failures; they are concepts defined within specific institutional, legal, and technical frameworks that presuppose shared cultural context. Sago treats them as proper nouns, analogous to how any language treats technical jargon.

### 5.4 Dictionary Study

A 5,000-word English-to-Sago dictionary was constructed using Claude Haiku with the full tap inventory and grammar rules in the system prompt. For each word, the model assigned one of three types and a confidence score:

| Type | Count | Percentage | Mean confidence |
|---|---|---|---|
| Composition (2–5 taps) | 3,541 | 70.8% | 0.77 |
| Institutional | 1,000 | 20.0% | — |
| Single-tap | 459 | 9.2% | 0.89 |

The institutional category correctly identifies articles (*the*, *a*, *an*), copulas (*is*, *be*, *are*), and culturally specific concepts (*democracy*, *salary*, *automobile*, *music*). These are not Sago failures — they are concepts whose meaning is constituted by cultural institutions rather than universal semantic structure.

The most frequently used taps in compositions are DO (666 appearances), MANY (583), MOVE (496), BEFORE (407), GOOD (399), MORE (389), and NOT (368). This distribution is semantically informative: action, plurality, motion, temporal sequence, and evaluative polarity are the most combinatorially productive primitives.

### 5.5 Emergent Semantic Compositions

The dictionary study revealed several compositions of independent philosophical interest. These were not designed — they emerged from the model's application of compositional semantics to familiar words:

**Freedom = `na de na`** (NOT DO NOT). Freedom encodes as double negation: the absence of the prevention of action. This formulation precisely captures Isaiah Berlin's (1958) concept of negative liberty — freedom *from* constraint, as distinct from positive freedom (*to* do). The fact that double negation yields liberation is not obvious from the primitive set and suggests that NSM primitives encode substantive philosophical structure.

**Faith = `te su na vi`** (THINK TRUE NOT SEE). Believing truly in the absence of seeing. This is structurally identical to the definition in Hebrews 11:1: "the substance of things hoped for, the evidence of things not seen." The composition was derived independently from the primitive system, not from the biblical text.

**Spirit = `te re`** (THINK AIR). The connection between breath and consciousness is encoded in the etymology of *spiritus* (Latin), *ruach* (Hebrew), *pneuma* (Greek), *qi* (Chinese), and *prana* (Sanskrit). Sago's composition independently rediscovers this cross-cultural association.

**History = `we pa ka`** (SAY BEFORE MANY). History is the many sayings of the past — not what happened, but what was told about what happened. This aligns with narrativist philosophy of history (White, 1973).

**Marriage = `je li ti`** (TOGETHER ALIVE TWO). Two lives lived together.

**Courage = `de je ba bi`** (DO TOGETHER FEEL BAD). Acting while afraid — as distinct from the absence of fear. This corresponds to Aristotle's definition of courage as the mean between cowardice and recklessness.

These emergent compositions are not proofs of the system's validity, but they are evidence of semantic coherence. A vocabulary system that produces compositional structures aligned with independent philosophical and etymological analysis is doing something right.

### 5.6 Back-Translation Study

To evaluate communicative function, we conducted back-translation experiments: English text was translated to Sago by Claude (with the full tap inventory and grammar rules in the system prompt), then the Sago output was translated back to English by a second Claude call with no access to the original. We measured meaning preservation using two methods.

**Method 1: Cosine similarity** between sentence-transformer embeddings of original and back-translated text. This method has a known systematic bias: it measures vocabulary distribution similarity, not meaning equivalence. Sago's concept decomposition produces back-translations with different vocabulary from the original even when meaning is fully preserved ("I feel bad because of myself" for "I am sorry"). Cosine similarity penalizes these correct translations.

**Method 2: LLM-as-judge** (Claude Haiku), rating meaning preservation on a 1–5 scale with explicit instructions to score meaning equivalence rather than surface similarity. Judge scores were validated by manual inspection of 15 cases.

**Test set 1: 35 simple sentences** across 10 categories (needs, emotion, observation, social, question, narrative, spatial, temporal, logic, universal). This test set represents Sago's intended use cases.

| Category | Judge score (mean/5) |
|---|---|
| Spatial relations | 4.2/5 |
| Social phrases | 3.7/5 |
| Temporal/causal | 3.8/5 |
| Observation | 3.4/5 |
| Emotion | 3.6/5 |
| Needs/wants | 3.5/5 |
| Questions | 3.9/5 |
| Narrative | 2.5/5 |
| Logic | 3.3/5 |
| **Overall** | **3.69/5 (74%)** |

Fifteen of 35 sentences (43%) received 5/5 — complete meaning preservation with nothing lost. These included "I want water," "I cannot move," "I feel good because you are here," "There is no water here," and "Where are you going?" — demonstrating that core communicative acts translate with perfect fidelity. Twenty of 35 (57%) received 4/5 or better.

**Test set 2: 10 literary passages** from canonical Western literature (Jane Austen, Shakespeare, Dickens, Kafka, Orwell, Carroll, Melville, Hemingway, Fitzgerald, Darwin). These texts represent the opposite extreme of linguistic complexity — rich in metaphor, irony, cultural reference, and rhetorical structure.

| | Judge score | Cosine similarity |
|---|---|---|
| All 10 texts | 1.00/5 | 0.389 |

Every literary passage scored 1/5 — meaning effectively lost in translation. Crucially, the cosine metric systematically *overestimated* literary performance (0.389 cosine vs. 0.200 normalized judge score), because vocabulary overlap in a short passage can survive even when meaning is garbled.

**Metric comparison:**

| Test set | Cosine | Judge (norm.) | Direction of error |
|---|---|---|---|
| Simple sentences | 0.711 | 0.737 | Cosine underestimates |
| Literary texts | 0.389 | 0.200 | Cosine overestimates |

The cosine metric has errors in both directions. For simple sentences with primitive decomposition, it underestimates because different vocabulary is penalized even when meaning is preserved. For literary texts, it overestimates because word overlap survives even when narrative meaning is lost. We recommend LLM-as-judge as a more valid evaluation method for semantic languages.

---

## 6. Discussion

### 6.1 What Sago Is For

The back-translation results are evidence, not failure. A language built from semantic primitives performs excellently on primitive-expressible content (74% simple communication preservation, 43% perfect) and fails on content that depends on metaphor, cultural register, and institutional knowledge. This is precisely what the theoretical design predicts.

Sago's intended use cases are direct communication, expression of needs and states, observation of the physical world, simple narrative, spatial and temporal description, and logical reasoning. These are the domains where semantic primitives are complete. They are also the domains where natural language most often fails: ambiguity, polysemy, cultural untranslatability, and register-dependent meaning all undermine communication in natural language exactly where primitive encoding is most stable.

The failure on literary text is not a bug. Hamlet's soliloquy cannot be expressed in semantic primitives without losing what makes it Hamlet. This is correct: Hamlet's soliloquy is not *about* existence and non-existence in a primitive sense — it is *performing* a specific cultural, rhetorical, and literary act. No primitive vocabulary system should be expected to preserve that performance.

### 6.2 The Convention Problem

The most significant practical limitation revealed by the evaluation is not vocabulary incompleteness but *convention instability*. A language functions when all speakers share the same encoding conventions. "Water" in English is a shared convention — every English speaker encodes the same concept with the same word. In Sago, the composition for "cloud" (WATER·AIR), "river" (WATER·MOVE·ROAD), or "rain" (WATER·MOVE·DOWN) must be shared by convention, or two speakers will encode the same concept differently and fail to understand each other.

The 5,000-word dictionary is a first attempt at establishing canonical conventions, but it was generated computationally and has not been validated by a speaker community. Naturally occurring languages develop conventions through iterated social use. For Sago to function as a language in practice, the compositional conventions must be stabilized through community agreement and documented in a canonical convention dictionary — a process that requires actual speakers, not just computation.

### 6.3 Relation to Language Universals Research

Sago's design indirectly tests a claim from Greenberg (1963) and developed by Comrie (1981): that some semantic and structural properties are universal across all human languages. By building a complete language from the most robust universal semantic structures identified by 50 years of cross-linguistic research, Sago tests whether that universal set is *sufficient* for communication. The vocabulary evaluation result — 70.8% of common English words compositionally expressible — suggests that the universal semantic core is substantially, though not fully, complete for common communication needs.

The 20% institutional gap is structurally informative: it consists precisely of concepts whose meaning is constituted by specific cultural institutions (legal systems, monetary systems, political structures, technological artifacts). These concepts are not semantically primitive in any language — they are culturally specific, and their meaning varies across cultures that instantiate different institutions. The fact that Sago correctly identifies them as outside its encoding scope is evidence that the primitive/institutional distinction is semantically real.

### 6.4 Phonological Completeness as a Design Principle

The bijection between phonological and semantic space (90 CV syllables = 90 semantic taps) is, to our knowledge, unique among constructed languages. It provides the system with an elegant completeness property: the phonological system is full — there are no unused syllables — and the semantic system is exhaustive of the phonological space. Any new primitive would require a new phoneme or phoneme combination.

This completeness creates a useful pressure: expanding the semantic vocabulary would require either adding phonemes (increasing phonological complexity) or adopting a different syllable structure (CVC, CCV, etc.). The pressure encourages conservative vocabulary design and forces the question of whether a proposed addition is genuinely irreducible or decomposable from existing primes.

---

## 7. Future Work

**Empirical acquisition studies.** The tiered acquisition model predicts that L1 (8 taps) is learnable in days, with full L5 acquisition over months. These predictions are theoretically motivated but not empirically tested. Controlled acquisition studies — particularly with children and with deaf-blind users via haptic interfaces — would provide the strongest evidence for or against the design.

**Cross-linguistic convention studies.** Do speakers of Japanese, Arabic, and Swahili converge on the same compositional conventions when given the tap inventory? If the primitives are universal, the compositions should be too. If they diverge systematically, this would be evidence that cultural framing operates below the level of primitives.

**The primitive-native advantage hypothesis.** Children raised bilingually in Sago and a natural language may develop enhanced compositional reasoning — the ability to analyze novel concepts by decomposing them into primitives. This hypothesis is empirically testable and educationally significant, though it requires longitudinal study.

**Haptic interface development.** Sago was originally motivated by assistive communication for deaf-blind users. The haptic interface — 4-motor wearable encoding tap patterns — remains a design specification, not a built system. Building and testing the interface with deaf-blind participants is a natural next step.

**The convention dictionary as linguistic corpus.** The 5,000-word dictionary generated computationally in this study could be refined through community use. The distribution of conventional compositions across speakers would itself be a valuable linguistic dataset — a measure of how consistently the primitive set grounds compositional semantics across different native language backgrounds.

**Interactive acquisition system.** Effective language acquisition requires more than reference documents — it requires an immersive, adaptive environment where meaning is learned through context rather than translation. A purpose-built Sago acquisition system would combine animated scene generation (visual or haptic scenes that narrate themselves in Sago), AI-driven adaptive curriculum, and a locally-deployed language model fine-tuned on the Sago primitive vocabulary and grammar. Local deployment is essential: an acquisition system that requires cloud API calls for every interaction cannot serve low-bandwidth environments, deaf-blind users on wearable devices, or educational contexts where connectivity is unreliable. The primitive vocabulary is small enough (90 items) that a compact, locally-runnable model could encode the full Sago semantic space without network dependency — a tractable fine-tuning target that would make the language genuinely self-contained.

---

## 8. Conclusion

Sago demonstrates that Wierzbicka's Natural Semantic Metalanguage prime set is practically sufficient for constructing a complete communication system. The design achieves phonological completeness (90 CV syllables for 90 semantic taps), tiered acquisition aligned with natural language development, a complete grammar covering 22 rule categories, and 70.8% compositional coverage of common English vocabulary.

Back-translation evaluation establishes a clear performance profile: 74% meaning preservation for direct communication (43% perfect) and effectively zero preservation for literary content — a result that is both expected and informative. The metric comparison reveals that cosine similarity systematically underestimates primitive-decomposed translations and recommends LLM-based semantic judgment as a more valid evaluation method for semantic languages.

The most unexpected finding is philosophical: the composition of semantic primitives reveals structures that independently converge on definitions from Aristotelian philosophy, biblical theology, cognitive emotion theory, and Enlightenment political philosophy. *Freedom* as double negation, *faith* as believing without seeing, *courage* as acting while afraid — these are not designed features but emergent properties of a well-chosen primitive set applied compositionally.

Whether Sago can become a functional language depends on what every language ultimately depends on: a community of speakers who converge on shared conventions and transmit them. The primitive vocabulary and grammar are complete. The conventions are a beginning. The language is an invitation.

---

## References

Anthropic. (2024). *The Claude 3 model family: Opus, Sonnet, Haiku* [Technical report].

Aristotle. *Nicomachean Ethics* (trans. W. D. Ross). Oxford University Press, 1998.

Berlin, I. (1958). Two concepts of liberty. In *Four Essays on Liberty*. Oxford University Press, 1969.


Comrie, B. (1981). *Language Universals and Linguistic Typology*. University of Chicago Press.

Cowan, J. W. (1997). *The Complete Lojban Language*. Logical Language Group.



Everett, D. L. (2005). Cultural constraints on grammar and cognition in Pirahã. *Current Anthropology*, 46(4), 621–646.

Goddard, C. (2001). Lexico-semantic universals: A critical overview. *Linguistic Typology*, 5(1), 1–66.

Goddard, C. (2008). *Cross-Linguistic Semantics*. John Benjamins.

Goddard, C. (2011). *Semantic Analysis: A Practical Introduction* (2nd ed.). Oxford University Press.

Goddard, C., & Wierzbicka, A. (Eds.). (2002). *Meaning and Universal Grammar: Theory and Empirical Findings* (2 vols.). John Benjamins.

Greenberg, J. H. (Ed.). (1963). *Universals of Language*. MIT Press.

Klima, E. S. (1964). Negation in English. In J. A. Fodor & J. J. Katz (Eds.), *The Structure of Language*. Prentice Hall.

Lang, S. (2014). *Toki Pona: The Language of Good*. Toki Pona Press.

Langacker, R. W. (1987). *Foundations of Cognitive Grammar: Vol. 1, Theoretical Prerequisites*. Stanford University Press.

Leibniz, G. W. (1666/1989). *Dissertatio de Arte Combinatoria*. In G. W. Leibniz: *Philosophical Papers and Letters* (L. Loemker, trans.). Kluwer.

Levinson, S. C., & Evans, N. (2010). Time for a sea-change in linguistics. *Lingua*, 120(12), 2733–2758.

Li, C. N., & Thompson, S. A. (1976). Subject and topic: A new typology of language. In C. N. Li (Ed.), *Subject and Topic*. Academic Press.

Ogden, C. K., & Richards, I. A. (1923). *The Meaning of Meaning*. Kegan Paul.

Okrent, A. (2009). *In the Land of Invented Languages*. Spiegel & Grau.

Ortony, A., Clore, G. L., & Collins, A. (1988). *The Cognitive Structure of Emotions*. Cambridge University Press.

Pinker, S. (1994). *The Language Instinct*. William Morrow.

Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using Siamese BERT-networks. *Proceedings of EMNLP 2019*, 3982–3992.

Sapir, E. (1931). The function of an international auxiliary language. *Psyche*, 11, 4–15.

Speer, R., Chin, J., & Havasi, C. (2018). ConceptNet 5.5: An open multilingual graph of general knowledge. *AAAI 2017*, 4444–4451.

Stassen, L. (1997). *Intransitive Predication*. Oxford University Press.

Talmy, L. (2000). *Toward a Cognitive Semantics: Vol. 1, Concept Structuring Systems*. MIT Press.

White, H. (1973). *Metahistory: The Historical Imagination in Nineteenth-Century Europe*. Johns Hopkins University Press.

Wierzbicka, A. (1972). *Semantic Primitives*. Athenäum.

Wierzbicka, A. (1980). *Lingua Mentalis: The Semantics of Natural Language*. Academic Press.

Wierzbicka, A. (1992). *Semantics, Culture, and Cognition: Universal Human Concepts in Culture-Specific Configurations*. Oxford University Press.

Wierzbicka, A. (1996). *Semantics: Primes and Universals*. Oxford University Press.

Wierzbicka, A. (2007). NSM semantics 2006: In response to some of the commentators. In C. Goddard (Ed.), *Semantic Primes and Universal Grammar*. John Benjamins.

Wilkins, J. (1668). *An Essay Towards a Real Character and a Philosophical Language*. Royal Society.

---

*Correspondence: funk.ryan@gmail.com*  
*Code and data: available on request*  
*Word count: approximately 6,400*
