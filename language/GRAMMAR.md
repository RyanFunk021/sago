# PrimaTap Grammar — v1.0

**Companion to TAPS.md**  
**Author:** Ryan Funk  
**Date:** May 2026

A language needs two things: a vocabulary and a grammar. TAPS.md defines the 90-chord vocabulary. This document defines the rules for combining taps into meaning.

---

## Core Principle

**Cognitive order = tap order.**

PrimaTap syntax follows the natural sequence of attention — the order in which a mind processes a situation:

1. **When** — time frame (establishes context)
2. **Who/What** — topic (what we're attending to)
3. **What's happening** — predicate (state or action)
4. **To/for what** — patient or goal (what's affected)
5. **How/how much** — modifiers (additional detail)

This is not arbitrary English-derived word order. It mirrors the cognitive structure of attention across languages. Topic-prominent, time-first syntax appears in Japanese, Chinese, Korean, Mandarin, Turkish, and many others. Grounding in cognition rather than any one language's history makes PrimaTap learnable without native-language interference.

---

## Rule 1 — Basic Sentence Structure

`[TIME]  TOPIC  PREDICATE  [PATIENT]  [MODIFIERS]`

```
sa wu du             SELF WANT WATER              I want water
to mo la             OTHER MOVE FAR               you / they leave
sa te to             SELF THINK OTHER             I understand you
sa mo hi             SELF MOVE HERE               I am coming
ka li va le          MANY ALIVE ABOVE TREE        birds in a tree
```

**No copula.** Topic + state = "is." The linking verb is structurally absent:

```
sa go                SELF GOOD                    I am fine / I'm okay
du fu                WATER HEAT                   hot water / the water is hot
to li                OTHER ALIVE                  you are alive
sa na go             SELF NOT-GOOD                I am not well
```

---

## Rule 2 — Tense

Tense markers appear at sentence start, before the topic. No marker = present.

| Marker | Tap | Meaning | Example |
|---|---|---|---|
| (none) | — | present / timeless | `sa wu du` = I want water |
| past | `pa` | already happened | `pa sa mo la` = I went away |
| future | `ya` | will happen | `ya to mo hi` = you will come |
| then / suddenly | `mu` | narrative moment | `mu sa te` = I suddenly understood |

```
pa sa ba bi          BEFORE SELF FEEL BAD         I was in pain / I used to suffer
ya sa te to          AFTER SELF THINK OTHER       I will understand you
mu sa vi lu          MOMENT SELF SEE LIGHT        I suddenly saw the light (literal or metaphorical)
```

**Progressive (ongoing action):** Add `ne` (NOW) before the predicate:

```
sa ne mo             SELF NOW MOVE                I am moving (right now)
pa sa ne mo          BEFORE SELF NOW MOVE         I was moving (ongoing past)
```

**Habitual (repeated action):** Add `ma` (MORE) after the predicate:

```
sa mo ma             SELF MOVE MORE               I usually move / I keep moving / I walk often
sa wu du ma          SELF WANT WATER MORE         I always want water / I'm always thirsty
```

**Perfect (completed with present relevance):** Add `pa` before predicate without sentence-initial `pa`:

```
sa pa mo la          SELF [already] MOVE FAR      I have gone (and am now far)
```
Note: when `pa` is sentence-initial it marks simple past; when it follows the topic it marks perfect aspect.

---

## Rule 3 — Negation

`na` (NOT) immediately precedes the element it negates. Scope is tight — it negates only the immediately following tap.

```
sa na wu du          SELF [NOT-WANT] WATER        I don't want water
na li                [NOT-ALIVE]                  dead / not living
sa mo na la          SELF MOVE [NOT-FAR]          I haven't gone far / I stayed close
to na pi mo          OTHER [NOT-CAN] MOVE         you cannot move / you are stuck
```

**Double negation = emphatic affirmation:**

```
sa na na wu du       SELF [NOT-NOT-WANT] WATER    I really do want water
```

**Negation scope examples:**

```
na sa wu du          [NOT-SELF] WANT WATER        someone other than me wants water
sa wu na du          SELF WANT [NOT-WATER]        I want something other than water
sa na wu du          SELF [NOT-WANT] WATER        I don't want water
```

---

## Rule 4 — Questions

### Yes/No Questions

`mi` (MAYBE) sentence-final, with rising prosody in speech or a marked tap pattern on the device.

```
to wu du mi          OTHER WANT WATER [?]         Do you want water?
to go mi             OTHER GOOD [?]               Are you okay?
sa ya mo mi          SELF AFTER MOVE [?]          Am I leaving?
to pi mo mi          OTHER CAN MOVE [?]           Can you move?
```

Short answers:
```
go                                                Yes / correct
na                                                No / not that
mi                                                I'm not sure
```

### Content Questions

WH-tap at sentence start, `mi` at end marks the question slot.

| Question | Tap | Full pattern | Example |
|---|---|---|---|
| What | `ze` (SOMETHING) | `ze [predicate] mi` | `ze to wu mi` — What do you want? |
| Who | `zo` (SOMEONE) | `zo [predicate] mi` | `zo mo hi mi` — Who is coming? |
| Where | `wa` (WHERE) | `wa [topic] [pred] mi` | `wa sa mo mi` — Where am I going? |
| When | `wi` (WHEN) | `wi [topic] [pred] mi` | `wi to mo hi mi` — When will you come? |
| Why | `da mi` (BECAUSE MAYBE) | `da mi [clause]` | `da mi to na wu` — Why don't you want it? |
| How | `lo` (LIKE) | `lo [topic] [pred] mi` | `lo to mo la mi` — How did you leave? |
| How many | `ka ze` (MANY SOMETHING) | `ka ze [noun] mi` | `ka ze du mi` — How much water? |

---

## Rule 5 — Modification

Modifiers follow the head they modify (post-nominal). The head comes first, description after:

```
du fu                WATER HEAT                   hot water
li go                ALIVE GOOD                   healthy (a living-good thing)
sa mo ve             SELF MOVE VERY               I move very much / quickly
du ka                WATER MANY                   a lot of water
re la                AIR FAR                      high altitude / distant air
```

**Stacking modifiers:** modifiers chain after the head, each scoping over the accumulating description:

```
li ko lu hi          ALIVE SOLID LIGHT NEAR       a creature: living, grounded, bright, close = house sparrow
```

**`pe` (KIND) as a category introducer:** groups a description as a named type:

```
pe li re             KIND ALIVE AIR               a kind of living air-creature = bird
pe li du             KIND ALIVE WATER             a kind of water-creature = fish
pe li ko             KIND ALIVE SOLID             a kind of solid living thing = plant (rooted)
pe li ko va          KIND ALIVE SOLID ABOVE       tall solid living thing = tree
```

**`ve` (VERY) marks degree, applies to the immediately following modifier:**

```
du ve fu             WATER VERY HOT               very hot water (boiling)
sa ba ve bi          SELF FEEL VERY BAD           I feel extremely bad
```

---

## Rule 6 — Possession

`ho` (HAVE) between possessor and possessed:

```
sa ho du             SELF HAVE WATER              my water
to ho ki             OTHER HAVE ANIMAL            your animal / their pet
sa ho na ze          SELF HAVE NOT SOMETHING      I have nothing
ka pu ho le          MANY PEOPLE HAVE TREE        the people's forest / shared trees
```

For general possession/existence, use `za` (EXIST):

```
du za hi             WATER EXIST HERE             there is water here
na li za             NOT-ALIVE EXIST              death is present / something died here
```

---

## Rule 7 — Quantity

Quantifiers precede the noun they quantify. Numbers (CVC digits, when defined) go in the same position.

| Quantifier | Tap | Example |
|---|---|---|
| all | `zu` | `zu li` — all living things |
| many | `ka` | `ka to` — many others / people |
| some | `so` | `so ki` — some animals |
| few | `fi` | `fi du` — a little water |
| one | `ta` | `ta ki` — one animal |
| two | `ti` | `ti le` — two trees |
| another | `nu` | `nu do` — another day |

```
ka to mo hi          MANY OTHER MOVE HERE         many people are coming
ta li mo la          ONE ALIVE MOVE FAR           one creature left
fi du za hi          FEW WATER EXIST HERE         there is little water here
zu li ba go          ALL ALIVE FEEL GOOD          all living things are happy
```

---

## Rule 8 — Causation and Conditionals

### BECAUSE (`da`) — connects cause to effect

```
sa na go da sa na wu du
→ SELF NOT-GOOD BECAUSE SELF NOT-WANT WATER
→ I am unwell because I don't want water (I'm not drinking)

di na fu ya du ko
→ IF NOT-HEAT AFTER WATER SOLID
→ If there is no heat, water becomes solid = freezing
```

`da` can precede the clause it introduces (English "because") or follow the result clause and precede the cause:

```
sa mo da sa wu du    SELF MOVE BECAUSE SELF WANT WATER    I'm moving because I want water
```

### IF (`di`) — introduces conditionals

```
di to mo hi ya sa go
→ IF OTHER MOVE HERE AFTER SELF GOOD
→ If you come, I will be happy

di na fu ya du ko
→ IF NOT-HEAT AFTER WATER SOLID
→ If not hot, water becomes solid

di sa na te to na pi we
→ IF SELF NOT-THINK OTHER NOT-CAN SAY
→ If I don't understand you, you can't communicate
```

---

## Rule 9 — Discourse Connectors

Connecting clauses and sentences:

| Connector | Taps | Meaning | Example |
|---|---|---|---|
| and | `je` | additive | `sa mo hi je to mo la` — I came and you left |
| but | `je na` | contrastive | `sa wu du je na du za` — I want water but there's none |
| so / therefore | `da` | result | `sa wu du da sa mo` — I want water, so I'm going |
| if / then | `di ... ya` | conditional chain | `di to mo hi ya sa go` — if you come, then I'm happy |
| although | `je di` | concessive | `sa go je di sa na du` — I'm okay although I have no water |
| or | `mi ... mi` | disjunction | `to wu du mi to wu re mi` — Do you want water or air? |

**Narrative chaining:** `mu` (MOMENT) marks plot beats in a story:

```
sa mo la  mu  sa vi le  mu  sa ni ki  mu  sa ba go
SELF MOVE FAR → MOMENT SELF SEE TREE → MOMENT SELF NEAR ANIMAL → MOMENT SELF FEEL GOOD
→ "I went away. Then I saw a tree. Then I found an animal. Then I felt happy."
```

---

## Rule 10 — Embedded Clauses

Embedded clauses follow the verb that introduces them. No subordinating conjunction — position signals the relationship:

```
sa te [pa to hi]     SELF THINK [BEFORE OTHER HERE]       I think you were here
sa we [sa wu du]     SELF SAY [SELF WANT WATER]           I said I want water
to no [du za]        OTHER KNOW [WATER EXIST]             you know there is water
sa ba go [pa to mo hi]  SELF FEEL GOOD [BEFORE OTHER MOVE HERE]  I was happy when you came
```

**Relative clauses:** `po` (PART) introduces a relative clause modifying the preceding noun:

```
du po ni to          WATER PART NEAR OTHER             the water that is near you
ki po pa mo hi       ANIMAL PART BEFORE MOVE HERE      the animal that came here
le po ga va          TREE PART BIG ABOVE               the tree that is very tall
```

---

## Evidentiality (Optional Layer)

How do you know what you're claiming? This optional layer is powerful for a precision language:

| Source | Tap pattern | Meaning |
|---|---|---|
| I saw it | `vi sa te` prefix | SEE-SELF-THINK = I saw and therefore believe |
| I heard it | `ra sa te` prefix | HEAR-SELF-THINK = I heard and therefore believe |
| I was told | `we to sa` prefix | SAY-OTHER-SELF = someone told me |
| I infer | `sa te da` suffix | SELF THINK BECAUSE = I reason this |
| I feel certain | `su` before claim | TRUE [claim] = this is fact |
| I'm uncertain | `mi` before claim | MAYBE [claim] = I'm not sure |

```
su du za la          TRUE WATER EXIST FAR             Water definitely exists far away
mi ki mo hi          MAYBE ANIMAL MOVE HERE           An animal might be coming
vi sa te ki za       SEE-SELF-KNOW ANIMAL EXIST       I saw it — an animal is there
we to sa ki za       OTHER-TOLD-SELF ANIMAL EXIST     I was told an animal is there
```

---

## Aspect Summary

| Aspect | Pattern | Example | Meaning |
|---|---|---|---|
| Simple | TOPIC PRED | `sa mo` | I move / I moved / I will move (context) |
| Progressive | TOPIC `ne` PRED | `sa ne mo` | I am moving (ongoing) |
| Habitual | TOPIC PRED `ma` | `sa mo ma` | I move regularly / I walk |
| Perfect | TOPIC `pa` PRED | `sa pa mo` | I have moved (and it matters now) |
| Immediate | TOPIC `mu` PRED | `sa mu mo` | I just moved |
| Ingressive (start) | TOPIC PRED `ya` | `sa mo ya` | I am about to move / I'm starting to move |

---

## The Social Register

Conventions for phatic communication and social bonding. These are fixed compositions, learnable as units:

| Social function | Tap sequence | Literal gloss | Use |
|---|---|---|---|
| Hello | `sa go ne hi` | SELF GOOD NOW HERE | I am well, I am present |
| Goodbye | `sa mo la` | SELF MOVE FAR | I'm going |
| Good morning | `sa go do` | SELF GOOD DAY | I am well this day |
| Good night | `sa go yu` | SELF GOOD NIGHT | Peace in the night |
| Yes / Okay | `go` | GOOD | Affirmation |
| No | `na` | NOT | Negation |
| Please | `wu` + [request] | WANT [request] | Request / please |
| Thank you | `sa go da to` | SELF GOOD BECAUSE OTHER | I am well because of you |
| Thank you very much | `sa ba go da to` | SELF FEEL GOOD BECAUSE OTHER | I feel good because of you |
| Sorry | `sa ba bi da sa` | SELF FEEL BAD BECAUSE SELF | I feel bad about my action |
| I forgive you | `go je to` | GOOD TOGETHER OTHER | Good, together with you |
| I don't understand | `sa na te` | SELF NOT-THINK | I don't grasp it |
| Say again | `ya we` | AFTER SAY | Please repeat |
| I'm thinking | `sa ne te` | SELF NOW THINK | Hold on, processing |
| Help me | `sa wu to de` | SELF WANT OTHER DO | I want you to act (for me) |
| I love you | `sa ba go ma to` | SELF FEEL GOOD MORE OTHER | I feel good, more [because of] you |
| I miss you | `sa ba bi da to na hi` | SELF FEEL BAD BECAUSE OTHER NOT-HERE | I feel bad because you are not here |

---

## Emotion Disambiguation

The dictionary revealed a critical collision: love = joy = pride all map to `ba go ma`. This must be resolved. The solution is **directedness** — emotions differ not just in valence and intensity but in *what they are about*.

### Structure of emotion in PrimaTap

`ba [valence] [intensity] [cause/direction]`

| Emotion | Tap sequence | Structure | Gloss |
|---|---|---|---|
| **joy** | `ba go za` | FEEL GOOD EXIST | good feeling about existence itself |
| **love** | `ba go ma to` | FEEL GOOD MORE OTHER | intense good feeling toward another |
| **pride** | `ba go da sa` | FEEL GOOD BECAUSE SELF | good feeling caused by oneself |
| **gratitude** | `ba go da to` | FEEL GOOD BECAUSE OTHER | good feeling caused by another |
| **relief** | `ba go da na bi` | FEEL GOOD BECAUSE NOT-BAD | good feeling because the bad ended |
| **awe** | `ba go ma la` | FEEL GOOD MORE FAR | intense good feeling toward something vast/distant |
| **anger** | `ba bi ma to` | FEEL BAD MORE OTHER | intense bad feeling directed at another |
| **hate** | `wu na to za` | WANT NOT OTHER EXIST | wanting another not to exist |
| **fear** | `ba bi da ya ze` | FEEL BAD BECAUSE AFTER SOMETHING | bad feeling caused by a future unknown |
| **grief** | `ba bi da na za` | FEEL BAD BECAUSE NOT-EXIST | bad feeling because something no longer exists |
| **shame** | `ba bi da sa de bi` | FEEL BAD BECAUSE SELF DO BAD | bad feeling caused by one's own bad action |
| **guilt** | `ba bi da sa de bi to` | FEEL BAD BECAUSE SELF DO BAD OTHER | shame with awareness of another harmed |
| **pain** | `ba bi bo` | FEEL BAD BODY | bad feeling in the body (physical only) |
| **loneliness** | `ba bi da na to hi` | FEEL BAD BECAUSE NOT OTHER HERE | bad feeling because others are absent |
| **jealousy** | `ba bi da to ho ze` | FEEL BAD BECAUSE OTHER HAVE SOMETHING | bad feeling because another has what I want |
| **envy** | `ba bi je wu to ho` | FEEL BAD TOGETHER WANT OTHER HAVE | bad feeling combined with wanting what another has |
| **anxiety** | `ba bi da ya mi` | FEEL BAD BECAUSE AFTER MAYBE | bad feeling about an uncertain future |
| **nostalgia** | `ba go da pa` | FEEL GOOD BECAUSE BEFORE | good feeling caused by the past |
| **hope** | `wu ya go` | WANT AFTER GOOD | wanting future good |
| **despair** | `na wu ya go` | NOT WANT AFTER GOOD | having stopped wanting future good |
| **courage** | `de je ba bi` | DO TOGETHER FEEL BAD | acting while afraid (not absence of fear — presence of action despite fear) |
| **wisdom** | `te ma go` | THINK MORE GOOD | better thinking |
| **wonder** | `te mi go` | THINK MAYBE GOOD | uncertain thinking about something positive |

**The principle:** Emotions are *structured* feelings. The structure tells you: 
1. Valence (good/bad)
2. Intensity (more/less)
3. Direction (toward self, other, past, future, existence, body, unknown)

This is how cognitive psychologists (Ortony, Clore, Collins) define emotion. PrimaTap encodes the structure directly.

---

## Extended Grammar — Solved Gaps

These patterns complete the core grammar. Each was a known gap now resolved.

---

### Comparatives

Pattern: `[TOPIC] [ATTR] ma lo [STANDARD]` — ATTR MORE LIKE STANDARD

```
sa ga ma lo to       SELF BIG MORE LIKE OTHER        I am bigger than you
le va ma lo bu       TREE ABOVE MORE LIKE BIRD        The tree is taller than the bird
du fu ma lo ne       WATER HOT MORE LIKE NOW          hotter than it is now
```

**Equality:** `[TOPIC] [ATTR] si lo [STANDARD]` — ATTR SAME-AS STANDARD

```
sa ga si lo to       SELF BIG SAME LIKE OTHER         I am as big as you
yo du si lo yo du    THIS WATER SAME LIKE THAT WATER  This water is the same temperature as that water
```

**Superlative:** `[TOPIC] [ATTR] ma zu` — ATTR MORE [than] ALL

```
sa ga ma zu          SELF BIG MORE ALL                I am the biggest
yo le va ma zu       THIS TREE ABOVE MORE ALL         This tree is the tallest
ba bi ma zu          FEEL BAD MORE ALL                the worst feeling (superlative suffering)
```

**Inferiority:** negate the comparison

```
sa na ga ma lo to    SELF NOT-BIG MORE LIKE OTHER     I am less big than you
sa gi ma lo to       SELF SMALL MORE LIKE OTHER       I am smaller than you (cleaner form)
```

---

### Imperatives

Drop the subject. Verb alone = command. Second person is implied.

```
mo hi                [you] MOVE HERE                  Come!
na mo                [you] NOT-MOVE                   Don't move! / Freeze!
we                   [you] SAY                        Speak!
te                   [you] THINK                      Think!
mo la                [you] MOVE FAR                   Go away!
na we                [you] NOT-SAY                    Be quiet!
```

**Polite request:** `wu` before the imperative = "please"

```
wu mo hi             WANT MOVE HERE                   Please come here.
wu we                WANT SAY                         Please speak.
wu na mo             WANT NOT-MOVE                    Please don't move.
```

**Urgent/strong command:** `de` before the imperative = "do it now"

```
de mo hi             DO MOVE HERE                     Move here! (urgent)
de na we             DO NOT-SAY                       Stop talking! (forceful)
```

---

### Reflexives

`si` (SAME) after the verb marks reflexive — the action returns to the subject.

```
sa vi si             SELF SEE SAME                    I see myself
sa de bi si          SELF DO BAD SAME                 I hurt myself
to ba go si          OTHER FEEL GOOD SAME             they feel good about themselves
sa te si             SELF THINK SAME                  I think of myself
```

Reflexive intensifier ("by oneself, alone"):

```
sa de yo si          SELF DO THIS SAME                I did it myself (no help)
```

---

### Reciprocals

`si je` after the verb = SAME TOGETHER = each to the other

```
to ba go si je       OTHER FEEL GOOD SAME TOGETHER    they love each other
to de go si je       OTHER DO GOOD SAME TOGETHER      they help each other
to vi si je          OTHER SEE SAME TOGETHER          they see each other
sa je to ba go si je SELF TOGETHER OTHER FEEL GOOD SAME TOGETHER   we love each other
```

---

### Reported Speech

`we to [content]` — SAY OTHER [what was said] = "someone said..."

Direct quote (verbatim): `we to` + original tap sequence

```
to we [sa mo hi]         OTHER SAY [SELF MOVE HERE]        they said: "I am coming"
ku we sa [sa ba go]      MOTHER SAY SELF [SELF FEEL GOOD]  my mother said she feels good
```

Indirect (paraphrase): use `we` + normal clause

```
to we ya to mo hi        OTHER SAY AFTER OTHER MOVE HERE   they said they would come
sa te [to we sa ba bi]   SELF THINK [OTHER SAY SELF-FEEL-BAD]  I think they said they felt bad
```

---

### Metaphor Convention

`lo` (LIKE) before a composition marks it as figurative, not literal.

```
lo du ga             LIKE WATER BIG               like an ocean = "oceanic" / overwhelmingly much
lo fu mo             LIKE HEAT MOVE               like fire = "fiery" / passionate
lo re mo             LIKE AIR MOVE                like the wind = free, swift, untethered
lo yu na li          LIKE NIGHT NOT-ALIVE          like death's darkness = total despair
```

Metaphorical sentence:

```
sa ba lo du ga       SELF FEEL LIKE WATER BIG     I feel like an ocean (I feel overwhelmingly much)
to mo lo re          OTHER MOVE LIKE AIR           you move like the wind (gracefully, swiftly)
yo we lo ko          THIS WORD LIKE SOLID          this word is like stone (heavy, hard to deny)
```

Compare to literal:

```
sa ba du ga          SELF FEEL WATER BIG           I feel the big water (I'm swimming / I'm in the ocean — literal)
sa ba lo du ga       SELF FEEL LIKE WATER BIG      I feel like the ocean (emotional overwhelm — figurative)
```

---

### Focus and Contrast

`yo` (THIS) immediately before an element = contrastive focus. "It is THIS that..."

```
yo sa mo             THIS SELF MOVE               IT IS I who moved (not someone else)
sa yo mo             SELF THIS MOVE               I MOVED (not did something else)
sa mo yo hi          SELF MOVE THIS HERE           I moved HERE (not somewhere else)
yo ne sa wu du       THIS NOW SELF WANT WATER      RIGHT NOW I want water (not later)
```

`ma` (MORE) before an element = emphatic/scalar focus. "Even...", "especially..."

```
ma sa te yo          MORE SELF THINK THIS          Even I understand this (surprising)
ma yu li go          MORE NIGHT ALIVE GOOD         Even at night, the living things are well
```

---

### Scalar Particles

These are common in every language but rarely defined in constructed languages.

| Concept | Pattern | Example | Meaning |
|---|---|---|---|
| only | `ta` before element | `ta sa mo` | only I moved |
| also / too | `je` after subject | `sa je mo` | I also moved |
| even | `ma` before element | `ma sa mo` | even I moved |
| still (ongoing) | `ne` | `sa ne mo` | I am still moving |
| already | `pa` | `sa pa mo` | I have already moved |
| not yet | `na pa` | `sa na pa mo` | I haven't moved yet |
| barely | `gi ma` | `sa gi ma mo` | I barely moved |
| too much | `ma ma` | `sa mo ma ma` | I moved way too much |
| enough | `pi go` before action | `sa pi go mo` | I can move enough / I have moved enough |
| almost | `ni` | `sa ni mo la` | I almost left / I nearly went |
| exactly | `su si` | `sa su si te` | I know exactly |

---

### Simultaneous Actions ("while")

`ne je` (NOW TOGETHER) connects two simultaneous events:

```
sa mo ne je to we         SELF MOVE NOW-TOGETHER OTHER SAY
→ I was moving while you were speaking.

du mo be ne je re mo va   WATER MOVE DOWN NOW-TOGETHER AIR MOVE ABOVE
→ The rain fell while the wind blew upward.
```

Or embed with `[...]` bracketing:

```
sa mo [ne to we]          SELF MOVE [NOW OTHER SAY]
→ I moved while you spoke.
```

---

### Sequential Actions ("first... then... finally")

Use `pa`, `ya`, and `mu` (MOMENT) to chain:

```
pa sa mo hi  ya sa te  ya sa we
BEFORE SELF MOVE HERE  AFTER SELF THINK  AFTER SELF SAY
→ First I came, then I understood, then I spoke.
```

`mu` marks discrete narrative moments:

```
mu sa vi ki  mu sa ba bi  mu sa mo la
MOMENT SEE ANIMAL  MOMENT FEEL BAD  MOMENT MOVE FAR
→ I saw the animal. Then I panicked. Then I ran.
```

---

### Purpose Clauses ("in order to")

Use `da wu` (BECAUSE WANT) to signal purpose:

```
sa mo da wu du            SELF MOVE BECAUSE WANT WATER
→ I moved in order to get water.

to te da wu we            OTHER THINK BECAUSE WANT SAY
→ They thought so they could speak. / They reflected in order to respond.
```

Or use forward-looking `ya`:

```
sa mo ya ho du            SELF MOVE AFTER HAVE WATER
→ I moved [so that] I would have water.
```

---

### Exclamations

Intensified sentence with `ve` or `ma ma` at end, or standalone:

```
ve go!                    VERY GOOD!                Wonderful! / Excellent!
ve bi!                    VERY BAD!                 Terrible! / Awful!
ba go ve!                 FEEL GOOD VERY!           What joy! / So happy!
ma lu!                    MORE LIGHT!               How bright! / Dazzling!
ve ga!                    VERY BIG!                 Enormous! / Incredible scale!
```

Question used as exclamation:

```
zo de yo mi               SOMEONE DO THIS?!         Who did this?! (rhetorical outrage)
da mi to na mo            WHY OTHER NOT MOVE?!       Why won't you move?! (frustration)
```

---

### Vocatives

Direct address: `to` alone, or name bracket, then content.

```
to, mo hi                 YOU, MOVE HERE            Hey you — come here.
we Ryan we, sa wu to de   [RYAN], SELF WANT OTHER DO  Ryan, I need your help.
to ba go, we mi           FRIEND, SAY [?]           Friend, will you speak?
```

---

### Approximation

`si lo` (SAME LIKE) = approximately, roughly, around:

```
si lo ka do               SAME LIKE MANY DAYS       about many days / approximately many days
sa mo si lo ni            SELF MOVE SAME LIKE NEAR  I moved roughly this far / approximately nearby
```

`ni` (NEAR) before a quantity or state = "almost", "nearly":

```
sa ni mo la               SELF NEAR MOVE FAR        I almost left.
du ni za                  WATER NEAR EXIST          water is almost here / barely present
ni do                     NEAR DAY                  nearly a day / almost a full day
```

---

### Passive / Agentless Events

PrimaTap handles this naturally: use `ha` (HAPPEN) when there is no agent, or move the patient to topic position.

```
du mo be                  WATER MOVE DOWN           water moves downward = rain falls
                                                    (no agent — water acts itself)

le gu                     TREE DIE                  the tree died (agentless)

li gu da ze               ALIVE DIE BECAUSE SOMETHING   something living died due to something
                                                         (agent unknown = passive-equivalent)
```

When you want to say "the tree was cut [by someone]":

```
zo de vo le               SOMEONE DO SHARP[=cut] TREE   someone cut the tree
ta zo pa de vo le         ONE SOMEONE BEFORE DO CUT TREE   someone cut the tree [passive reading: the tree was cut]
```

Agent can be omitted: `pa de vo le` = "the tree was cut [at some point]" — agentless passive by simply dropping the agent.

---

## Modality — Necessity, Permission, Obligation

`pi` (CAN) covers ability and possibility. Obligation and necessity need compounds:

| Modal | Pattern | Gloss | Example |
|---|---|---|---|
| can / able to | `pi` | CAN | `sa pi mo` = I can move |
| cannot | `na pi` | NOT CAN | `sa na pi mo` = I cannot move |
| must / have to | `na pi na` | NOT-CAN-NOT | `to na pi na mo` = you must move (can't not) |
| should / ought | `go pi` | GOOD CAN | `to go pi mo` = you should move |
| may / allowed | `to pi mo` | OTHER CAN | `to pi mo` = you may move |
| forbidden | `na pi de` | NOT CAN DO | `sa na pi de yo` = I am forbidden from doing this |
| impossible | `na pi ha` | NOT CAN HAPPEN | `yo na pi ha` = this cannot happen |

```
sa na pi na mo la    SELF NOT-CAN NOT MOVE FAR    I must leave (I cannot not go)
to go pi we          OTHER GOOD CAN SAY           You should speak
di to na mo ya to na pi na                        If you don't move, you will have to
```

---

## Certainty and Epistemic Scale

PrimaTap can encode how sure a speaker is about a claim:

| Certainty | Pattern | Example |
|---|---|---|
| certain | `su` + claim | `su du za hi` = Water is definitely here |
| probable | `ma mi` + claim | `ma mi to mo hi` = They will probably come |
| possible | `mi` + claim | `mi du za hi` = Water might be here |
| unlikely | `fi mi` + claim | `fi mi to mo` = They are unlikely to come |
| impossible | `na pi ha` | `na pi ha du la` = Water cannot be far |
| I believe | `sa te su` | `sa te su to go` = I believe you are well |
| I don't know | `sa na no` | `sa na no da mi` = I don't know why |
| I was told | `to we sa` prefix | `to we sa du za hi` = I was told water is here |
| I infer | `sa te da vi` | `sa te da vi to go` = I infer you are well (from what I've seen) |

---

## Repetition ("again", "repeatedly", "once more")

| Concept | Pattern | Gloss |
|---|---|---|
| again / once more | `nu [action]` | ANOTHER [action] — do it one more time |
| repeatedly | `[action] ma` | [action] MORE — keep doing it |
| never again | `na nu [action]` | NOT ANOTHER [action] |
| first time | `pa ta [action]` | BEFORE ONE [action] |
| last time | `ya na nu [action]` | AFTER NOT ANOTHER [action] |

```
ya we             AFTER SAY         Say again (please repeat)
nu mo hi          ANOTHER MOVE HERE Come again / come back
sa mo ma          SELF MOVE MORE    I keep moving / I move repeatedly
na nu te bi       NOT ANOTHER THINK-BAD  Never think this again
```

---

## Ordinal Numbers ("first", "second", "third")

Position in sequence: `po` (PART) + CVC digit + noun

| Ordinal | Pattern | Example |
|---|---|---|
| first | `po nun` + noun | `po nun do` = the zeroth day (day 0) |
| first (1st) | `po win` + noun | `po win do` = the first day |
| second | `po tim` + noun | `po tim do` = the second day |
| third | `po ron` + noun | `po ron do` = the third day |
| last | `po ya` + noun | `po ya do` = the last day |

```
po win sa mo hi      PART ONE SELF MOVE HERE    the first time I came
po tim to we         PART TWO OTHER SAY         the second time you spoke
```

---

## Past Habitual ("used to")

`pa [action] ma` = BEFORE [action] MORE = used to do [action] regularly

```
pa sa mo ma          BEFORE SELF MOVE MORE      I used to move a lot / I used to travel
pa sa te to ma       BEFORE SELF THINK OTHER MORE  I used to think of you often
pa du za hi ma       BEFORE WATER EXIST HERE MORE  Water used to be plentiful here
```

Contrast with simple past (`pa`) and perfect aspect:
- `pa sa mo` = I moved (once, specific event)
- `pa sa mo ma` = I used to move (habitual past)
- `sa pa mo` = I have moved (past with present relevance)

---

## Discourse Structure — Managing Conversation

| Function | Tap pattern | Gloss | Meaning |
|---|---|---|---|
| Change topic | `nu ro` | ANOTHER WORD | "on another subject..." |
| Return to topic | `si ro` | SAME WORD | "back to what we were saying..." |
| Aside / parenthetical | `ri we` | SIDE SAY | "by the way..." |
| Summarizing | `po zu we` | PART ALL SAY | "in summary..." |
| Emphasizing | `yo su we` | THIS TRUE SAY | "importantly..." / "note this:" |
| Conceding a point | `go je na` | GOOD TOGETHER NOT | "true, but..." |
| Disagreeing | `sa na te si` | SELF NOT-THINK SAME | "I don't see it that way" |
| Requesting clarification | `ze to we da` | WHAT OTHER SAY BECAUSE | "what do you mean by that?" |
| Acknowledging | `sa te` | SELF THINK | "I see." / "Got it." |

---

## Deixis — Pointing in Space and Time

PrimaTap's spatial system with refinement:

| Deictic | Tap | Meaning |
|---|---|---|
| here (near speaker) | `hi` | HERE |
| there (near listener) | `ni to` | NEAR OTHER |
| there (far from both) | `la` | FAR |
| up there | `la va` | FAR ABOVE |
| down there | `la be` | FAR BELOW |
| this (proximal) | `yo` | THIS |
| that (near you) | `yo ni to` | THIS NEAR OTHER |
| that (far) | `ze la` | SOMETHING FAR |
| now | `ne` | NOW |
| then (past) | `mu pa` | MOMENT BEFORE |
| then (future) | `mu ya` | MOMENT AFTER |
| soon | `ni ya` | NEAR AFTER |
| long ago | `pa la` | BEFORE FAR |
| in the future | `ya la` | AFTER FAR |

---

## Politeness and Hedging

Direct PrimaTap is monoregister — no grammatical formality distinction. Politeness is achieved structurally:

| Function | Pattern | Gloss | Effect |
|---|---|---|---|
| Polite request | `wu` + command | WANT [command] | Please... |
| Indirect request | `mi sa te di to pi...` | MAYBE I THINK IF YOU CAN... | I was wondering if you could... |
| Softened assertion | `mi` + claim | MAYBE [claim] | It seems to me that... |
| Acknowledging uncertainty | `sa na no su` | SELF NOT KNOW TRUE | I'm not certain, but... |
| Deferring | `to te ma` | OTHER THINK MORE | You know better than I do |
| Seeking permission | `sa pi de yo mi` | SELF CAN DO THIS? | May I...? |

```
mi sa te du za ni    MAYBE SELF THINK WATER EXIST NEAR   There might be water nearby
sa na no su je we    SELF NOT-KNOW TRUE TOGETHER SAY      I'm not sure, but: [claim]
wu to we ma          WANT OTHER SAY MORE                  Please tell me more
to te ma da to pa mo ma   OTHER THINK MORE BECAUSE OTHER BEFORE MOVE MORE
                     You know better because you've done this more
```

---

## What the Grammar Does Not Cover Yet

Genuinely open questions requiring community convention:

| Gap | Status | Notes |
|---|---|---|
| Long relative clauses | Open | `po` works ≤3 words; longer clauses need bracketing convention |
| Register / formality | Open | Monoregister by design; community may develop conventions |
| Irony / sarcasm | Open | Requires prosodic or contextual signal — cannot encode in taps alone |
| Fractions and decimals | Partial | CVC digit + `po` for fractions: `po tim` = one-half (1 of 2 parts) |
| Song / poetry / rhythm | Open | Aesthetic use of PrimaTap — undefined; possibly iconic tap patterns |
| Classifier system | Open | `pe` (KIND) partially serves this; needs more conventions for counting specific types |

---

## Complete Example: A Short Conversation

```
A: sa go ne hi
   SELF GOOD NOW HERE
   → Hello / I am here and well.

B: to go ne hi mi
   OTHER GOOD NOW HERE [?]
   → Are you well?

A: go  je  sa wu du
   GOOD  AND  SELF WANT WATER
   → Yes, and I want water.

B: du za la  je  na hi
   WATER EXIST FAR  AND  NOT HERE
   → Water exists far away, not here.

A: da mi
   BECAUSE [?]
   → Why?

B: sa pa de na du hi
   BEFORE SELF DO NOT-WATER HERE
   → I used to make sure no water was here.
   (I caused there to be no water here)

A: sa na te  —  ya we
   SELF NOT-THINK  —  AFTER SAY
   → I don't understand — say it again.
```

---

## Composition Reference

| English concept | Tap sequence | Gloss |
|---|---|---|
| cold | `na fu` | NOT HEAT |
| hot | `ve fu` | VERY HEAT |
| dead | `na li` | NOT ALIVE |
| healthy | `li go` | ALIVE GOOD |
| sick | `li bi` | ALIVE BAD |
| thirsty | `sa wu du` | SELF WANT WATER |
| hungry | `sa wu ze` | SELF WANT SOMETHING (context: food) |
| happy | `ba go` | FEEL GOOD |
| sad | `ba bi` | FEEL BAD |
| angry | `ba bi ma` | FEEL BAD MORE (intensified negative feeling) |
| afraid | `ba bi da ze` | FEEL BAD BECAUSE SOMETHING |
| cloud | `du re` | WATER AIR |
| steam | `du fu re` | WATER HEAT AIR |
| ice | `du na fu` | WATER NOT-HEAT |
| fire | `fu mo` | HEAT MOVE |
| light | `lu re` | LIGHT AIR (diffuse light, not a source) |
| shadow | `na lu` | NOT-LIGHT |
| forest | `ka le` | MANY TREE |
| ocean | `du ga` | WATER BIG |
| mountain | `ko va ga` | SOLID ABOVE BIG |
| cave | `ja ko` | INSIDE SOLID |
| child | `li gi` | ALIVE SMALL |
| elder | `li pa ga` | ALIVE BEFORE BIG = lived long, grown |
| friend | `to ba go` | OTHER FEEL GOOD (one who feels well with you) |
| enemy | `to ba bi` | OTHER FEEL BAD (one who feels bad toward you) |
| family | `je ku hu li` | TOGETHER MOTHER FATHER ALIVE = those alive together with parents |
| home | `hi je li` | HERE TOGETHER ALIVE = where living happens together |
| sun | `lu ga` | LIGHT BIG |
| rain | `du mo be` | WATER MOVE DOWN |
| wind | `re mo` | AIR MOVE |
| river | `du mo ru` | WATER MOVE ROAD |
| flower | `fa lu` | PLANT LIGHT (colorful plant) |
| seed | `fa gi pa` | PLANT SMALL BEFORE = the before-plant |
| egg | `li pa ju` | ALIVE BEFORE ROUND = round before-life |
| nest | `bu hi` | BIRD HERE = where the bird is |
| war | `ka pu ba bi de` | MANY PEOPLE FEEL BAD DO = people doing bad to each other |
| peace | `ka pu ba go je` | MANY PEOPLE FEEL GOOD TOGETHER |
| law | `ka pu we ro` | MANY PEOPLE SAY WORD = agreed words |
| story | `we pa` | SAY BEFORE = the telling of what happened |
| dream | `te yu` | THINK NIGHT |
| memory | `te pa` | THINK BEFORE |
| hope | `wu ya go` | WANT FUTURE GOOD |
| fear | `wu na bi` | WANT NOT-BAD = trying to avoid the bad |
| truth | `su we` | TRUE SAY |
| lie | `na su we` | NOT-TRUE SAY |
| question | `wu te mi` | WANT THINK [?] = wanting to know |
| answer | `te we` | THINK SAY |
| learn | `te ya` | THINK AFTER = come to know |
| teach | `to te ya` | OTHER THINK AFTER = cause another to know |
| grow | `li ma` | ALIVE MORE |
| sleep | `li na te` | ALIVE NOT-THINK |
| hungry | `sa wu ze` | SELF WANT SOMETHING (food context) |
| eat | `li ja ze` | ALIVE INSIDE SOMETHING |
| drink | `li ja du` | ALIVE INSIDE WATER |
| help (give) | `to de sa` | OTHER DO [for] SELF |
| help (want) | `sa wu to de` | SELF WANT OTHER DO |
| cold (weather) | `na fu za re` | NOT HEAT EXIST AIR |
| walk | `mo fo` | MOVE FOOT |
| run | `mo ve fo` | MOVE VERY FOOT |
| fly | `mo re va` | MOVE AIR ABOVE |
| swim | `mo du` | MOVE WATER |
| see | `vi` | SEE |
| hear | `ra` | HEAR |
| touch | `tu` | TOUCH |
| smell | `wo ba` | NOSE FEEL |
| taste | `fe ba` | TASTE FEEL |
| speak | `we vu` | SAY MOUTH |
| think | `te` | THINK |
| believe | `te su` | THINK TRUE |
| know | `no` | KNOW |
| forget | `na te pa` | NOT-THINK BEFORE — the past-thinking is gone |
| remember | `te pa ya` | THINK BEFORE AFTER — bringing the past into now |
| joy | `ba go za` | FEEL GOOD EXIST — good feeling about existence |
| love | `ba go ma to` | FEEL GOOD MORE OTHER — toward another |
| pride | `ba go da sa` | FEEL GOOD BECAUSE SELF |
| gratitude | `ba go da to` | FEEL GOOD BECAUSE OTHER |
| awe | `ba go ma la` | FEEL GOOD MORE FAR — overwhelmed by vastness |
| nostalgia | `ba go da pa` | FEEL GOOD BECAUSE BEFORE |
| relief | `ba go da na bi` | FEEL GOOD BECAUSE NOT-BAD |
| hope | `wu ya go` | WANT AFTER GOOD |
| despair | `na wu ya go` | NOT WANT AFTER GOOD |
| anger | `ba bi ma to` | FEEL BAD MORE OTHER |
| hate | `wu na to za` | WANT NOT OTHER EXIST |
| fear | `ba bi da ya ze` | FEEL BAD BECAUSE AFTER SOMETHING |
| grief | `ba bi da na za` | FEEL BAD BECAUSE NOT-EXIST |
| shame | `ba bi da sa de bi` | FEEL BAD BECAUSE SELF DO BAD |
| guilt | `ba bi da sa de bi to` | FEEL BAD BECAUSE SELF DO BAD OTHER |
| pain | `ba bi bo` | FEEL BAD BODY — physical only |
| loneliness | `ba bi da na to hi` | FEEL BAD BECAUSE NOT OTHER HERE |
| jealousy | `ba bi da to ho ze` | FEEL BAD BECAUSE OTHER HAVE SOMETHING |
| anxiety | `ba bi da ya mi` | FEEL BAD BECAUSE AFTER MAYBE |
| courage | `de je ba bi` | DO TOGETHER FEEL BAD — acting while afraid |
| wonder | `te mi go` | THINK MAYBE GOOD — curious awe |
| wisdom | `te ma go` | THINK MORE GOOD |
| faith | `te su na vi` | THINK TRUE NOT SEE |
| doubt | `na no` | NOT KNOW |
| truth | `su we` | TRUE SAY |
| lie | `we na su` | SAY NOT TRUE |
| promise | `we ya de` | SAY AFTER DO |
| spirit | `te re` | THINK AIR |
| freedom | `na de na` | NOT DO NOT — absence of prevention |
| justice | `de go ka pu` | DO GOOD MANY PEOPLE |
| history | `we pa ka` | SAY BEFORE MANY |
| marriage | `je li ti` | TOGETHER ALIVE TWO |
| city | `ka pu hi` | MANY PEOPLE HERE |
| language | `ro ka` | WORD MANY |
| art | `de lu go` | DO LIGHT GOOD — making something beautiful |
| music | `de ra go` | DO HEAR GOOD — making good sound |
| science | `te su de vi` | THINK TRUE DO SEE — knowing through observation |
| democracy | `ka pu de ro` | MANY PEOPLE DO WORD — governance by word of people |

---

*PrimaTap Grammar v1.1 — Ryan Funk, May 2026*  
*Companion to TAPS.md*
