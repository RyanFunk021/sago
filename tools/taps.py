"""
PrimaTap shared tap definitions — canonical source of truth.
Mirrors desktop/TAPS.md. Import this module in all PrimaTap scripts.
"""

TAPS = {
    # L1 · Core 8
    "sa": {"name": "SELF",    "level": 1, "meaning": "I, me, the speaker"},
    "to": {"name": "OTHER",   "level": 1, "meaning": "you, they, any non-self"},
    "na": {"name": "NOT",     "level": 1, "meaning": "negation, absence, opposite"},
    "wu": {"name": "WANT",    "level": 1, "meaning": "desire, need, intention"},
    "go": {"name": "GOOD",    "level": 1, "meaning": "positive, correct, safe"},
    "bi": {"name": "BAD",     "level": 1, "meaning": "negative, wrong, harmful"},
    "ne": {"name": "NOW",     "level": 1, "meaning": "present, immediate"},
    "hi": {"name": "HERE",    "level": 1, "meaning": "this place, proximal"},

    # L2 · Physical 16
    "li": {"name": "ALIVE",   "level": 2, "meaning": "living, conscious, animate"},
    "mo": {"name": "MOVE",    "level": 2, "meaning": "motion, action, change"},
    "te": {"name": "THINK",   "level": 2, "meaning": "know, understand, believe"},
    "du": {"name": "WATER",   "level": 2, "meaning": "liquid, fluid"},
    "fu": {"name": "HEAT",    "level": 2, "meaning": "temperature, thermal energy"},
    "re": {"name": "AIR",     "level": 2, "meaning": "gas, breath, wind, sky"},
    "ko": {"name": "SOLID",   "level": 2, "meaning": "matter, hard, tangible, earth"},
    "lu": {"name": "LIGHT",   "level": 2, "meaning": "visible energy, brightness, color"},

    # L3 · Grammar 32
    "pa": {"name": "BEFORE",  "level": 3, "meaning": "prior in time, past"},
    "ya": {"name": "AFTER",   "level": 3, "meaning": "subsequent, future"},
    "da": {"name": "BECAUSE", "level": 3, "meaning": "reason, cause, therefore"},
    "di": {"name": "IF",      "level": 3, "meaning": "conditional, hypothetical"},
    "pi": {"name": "CAN",     "level": 3, "meaning": "ability, possibility"},
    "ma": {"name": "MORE",    "level": 3, "meaning": "greater degree, very, much"},
    "si": {"name": "SAME",    "level": 3, "meaning": "identical, equal, matching"},
    "la": {"name": "FAR",     "level": 3, "meaning": "distant, away from here"},
    "va": {"name": "ABOVE",   "level": 3, "meaning": "higher than, over"},
    "ja": {"name": "INSIDE",  "level": 3, "meaning": "contained within, interior"},
    "ba": {"name": "FEEL",    "level": 3, "meaning": "emotion, sensation"},
    "ra": {"name": "HEAR",    "level": 3, "meaning": "auditory sense"},
    "we": {"name": "SAY",     "level": 3, "meaning": "speak, express, communicate"},
    "ka": {"name": "MANY",    "level": 3, "meaning": "plural, numerous"},
    "bo": {"name": "BODY",    "level": 3, "meaning": "physical form, flesh"},
    "pe": {"name": "KIND",    "level": 3, "meaning": "type, category, sort"},

    # L4 · Wierzbicka 64
    "zo": {"name": "SOMEONE",  "level": 4, "meaning": "an unspecified person"},
    "ze": {"name": "SOMETHING","level": 4, "meaning": "an unspecified thing"},
    "pu": {"name": "PEOPLE",   "level": 4, "meaning": "humans collectively"},
    "ta": {"name": "ONE",      "level": 4, "meaning": "single instance, unit"},
    "ti": {"name": "TWO",      "level": 4, "meaning": "a pair"},
    "so": {"name": "SOME",     "level": 4, "meaning": "an indefinite quantity"},
    "zu": {"name": "ALL",      "level": 4, "meaning": "every instance, universal"},
    "fi": {"name": "FEW",      "level": 4, "meaning": "a small number"},
    "ga": {"name": "BIG",      "level": 4, "meaning": "large in scale"},
    "gi": {"name": "SMALL",    "level": 4, "meaning": "small in scale"},
    "no": {"name": "KNOW",     "level": 4, "meaning": "certain knowledge, fact"},
    "vi": {"name": "SEE",      "level": 4, "meaning": "visual perception"},
    "tu": {"name": "TOUCH",    "level": 4, "meaning": "physical contact"},
    "de": {"name": "DO",       "level": 4, "meaning": "intentional action"},
    "ha": {"name": "HAPPEN",   "level": 4, "meaning": "event without agent, occur"},
    "ho": {"name": "HAVE",     "level": 4, "meaning": "possession, contain"},
    "za": {"name": "EXIST",    "level": 4, "meaning": "there is, presence"},
    "gu": {"name": "DIE",      "level": 4, "meaning": "cease living"},
    "su": {"name": "TRUE",     "level": 4, "meaning": "factual, real, actual"},
    "ro": {"name": "WORD",     "level": 4, "meaning": "linguistic unit, name"},
    "mi": {"name": "MAYBE",    "level": 4, "meaning": "uncertain, possible"},
    "lo": {"name": "LIKE",     "level": 4, "meaning": "similar to, as, in the manner of"},
    "ve": {"name": "VERY",     "level": 4, "meaning": "intensifier, to a great degree"},
    "ni": {"name": "NEAR",     "level": 4, "meaning": "close to, proximate"},
    "be": {"name": "BELOW",    "level": 4, "meaning": "lower than, under"},
    "ri": {"name": "SIDE",     "level": 4, "meaning": "lateral, beside"},
    "wi": {"name": "WHEN",     "level": 4, "meaning": "at which time"},
    "wa": {"name": "WHERE",    "level": 4, "meaning": "at which place"},
    "mu": {"name": "MOMENT",   "level": 4, "meaning": "an instant, a point in time"},
    "po": {"name": "PART",     "level": 4, "meaning": "a component, piece of a whole"},
    "nu": {"name": "ANOTHER",  "level": 4, "meaning": "a different one"},
    "yo": {"name": "THIS",     "level": 4, "meaning": "the proximal referent"},

    # L5 · Molecules 26
    "le": {"name": "TREE",     "level": 5, "meaning": "woody plant, standing plant"},
    "ge": {"name": "MOON",     "level": 5, "meaning": "Earth's satellite, night light"},
    "fo": {"name": "FOOT",     "level": 5, "meaning": "lowest part of leg, base"},
    "bu": {"name": "BIRD",     "level": 5, "meaning": "flying vertebrate, feathered animal"},
    "ru": {"name": "ROAD",     "level": 5, "meaning": "path for travel, route"},
    "se": {"name": "STAR",     "level": 5, "meaning": "distant sun, point of night light"},
    "do": {"name": "DAY",      "level": 5, "meaning": "period of sunlight, solar cycle"},
    "fa": {"name": "PLANT",    "level": 5, "meaning": "rooted living thing, vegetation"},
    "me": {"name": "MAN",      "level": 5, "meaning": "adult male human"},
    "ku": {"name": "MOTHER",   "level": 5, "meaning": "female parent"},
    "je": {"name": "TOGETHER", "level": 5, "meaning": "in mutual company, jointly"},
    "ki": {"name": "ANIMAL",   "level": 5, "meaning": "non-plant living thing, creature"},
    "hu": {"name": "FATHER",   "level": 5, "meaning": "male parent"},
    "ye": {"name": "EYE",      "level": 5, "meaning": "visual organ"},
    "he": {"name": "EARTH",    "level": 5, "meaning": "soil, ground material, the planet"},
    "ji": {"name": "HARD",     "level": 5, "meaning": "resistant to deformation, solid surface"},
    "vo": {"name": "SHARP",    "level": 5, "meaning": "pointed, cutting edge"},
    "vu": {"name": "MOUTH",    "level": 5, "meaning": "oral opening, speaking organ"},
    "jo": {"name": "EAR",      "level": 5, "meaning": "auditory organ"},
    "ju": {"name": "ROUND",    "level": 5, "meaning": "circular, spherical"},
    "fe": {"name": "TASTE",    "level": 5, "meaning": "flavor, gustatory sense"},
    "yi": {"name": "BACK",     "level": 5, "meaning": "posterior surface, rear"},
    "yu": {"name": "NIGHT",    "level": 5, "meaning": "period of darkness"},
    "zi": {"name": "GROUND",   "level": 5, "meaning": "surface underfoot, floor"},
    "ke": {"name": "CLOTH",    "level": 5, "meaning": "woven fabric, textile"},
    "wo": {"name": "NOSE",     "level": 5, "meaning": "olfactory organ"},
}

# Reverse lookups
BY_NAME = {v["name"]: syl for syl, v in TAPS.items()}
BY_LEVEL = {lvl: [syl for syl, v in TAPS.items() if v["level"] == lvl] for lvl in range(1, 6)}


def tap_inventory_string() -> str:
    """Format all 90 taps as a compact string for LLM system prompts."""
    level_labels = {1: "L1·Core", 2: "L2·Physical", 3: "L3·Grammar",
                    4: "L4·Wierzbicka", 5: "L5·Molecules"}
    lines = []
    current_level = 0
    for syl, info in TAPS.items():
        if info["level"] != current_level:
            current_level = info["level"]
            lines.append(f"\n{level_labels[current_level]}:")
        lines.append(f"  {syl} = {info['name']} — {info['meaning']}")
    return "\n".join(lines)


GRAMMAR_RULES = """
GRAMMAR RULES (PrimaTap v1.1):

1. SENTENCE ORDER: [TIME] TOPIC PREDICATE [PATIENT] [MODIFIERS]
   sa wu du = SELF WANT WATER = "I want water"
   to mo la = OTHER MOVE FAR = "you/they leave"

2. NO COPULA: topic + state = "is"
   sa go = SELF GOOD = "I am fine"
   du fu = WATER HEAT = "hot water / water is hot"

3. TENSE: time marker at sentence start; none = present
   pa = past:    pa sa mo la = "I went away"
   ya = future:  ya to mo hi = "you will come"
   mu = sudden:  mu sa te = "I suddenly understood"
   sa ne mo = SELF NOW MOVE = "I am moving" (progressive: ne before verb)
   sa mo ma = SELF MOVE MORE = "I usually move" (habitual: ma after verb)

4. NEGATION: na immediately precedes what it negates (tight scope)
   sa na wu du = SELF NOT-WANT WATER = "I don't want water"
   na li = NOT-ALIVE = "dead"

5. QUESTIONS:
   Yes/No: mi at sentence end — to wu du mi = "Do you want water?"
   Content: WH-tap at start — ze to wu mi = "What do you want?"
   WH-taps: ze=what, zo=who, wa=where, wi=when, da mi=why, lo=how

6. MODIFICATION: modifier follows head (post-nominal)
   du fu = WATER HEAT = "hot water"
   li go = ALIVE GOOD = "healthy"
   pe li re = KIND ALIVE AIR = "a bird" (kind of air-creature)

7. POSSESSION: POSSESSOR ho POSSESSED
   sa ho du = SELF HAVE WATER = "my water"

8. QUANTITY: quantifier before noun
   ka to = MANY OTHER = "people"
   ta ki = ONE ANIMAL = "an animal"
   zu li = ALL ALIVE = "all living things"

9. CAUSATION/CONDITIONALS:
   da = because/so — sa mo da sa wu du = "I move because I want water"
   di = if — di to mo hi ya sa go = "if you come, I will be happy"

10. DISCOURSE:
    je = and — sa mo hi je to mo la = "I came and you left"
    je na = but — sa wu du je na du za = "I want water but there's none"
    po = relative clause — du po ni to = "water that is near you"

EXTENDED RULES:
11. COMPARATIVES:
    bigger than: sa ga ma lo to (SELF BIG MORE LIKE OTHER)
    as big as:   sa ga si lo to (SELF BIG SAME LIKE OTHER)
    biggest:     sa ga ma zu (SELF BIG MORE ALL)
    smallest:    sa gi ma zu (SELF SMALL MORE ALL)

12. IMPERATIVES: drop subject, verb alone = command
    mo hi = Come!  na mo = Don't move!  wu mo hi = Please come.

13. REFLEXIVE: si after verb = action returns to subject
    sa vi si = I see myself  sa de bi si = I hurt myself

14. RECIPROCAL: si je after verb = each to the other
    to ba go si je = they love each other

15. METAPHOR: lo before composition = figurative reading
    lo du ga = "like an ocean" (not literal water)
    sa ba lo du ga = "I feel like an ocean" (overwhelmed)

16. FOCUS: yo before element = contrastive focus
    yo sa mo = IT IS I who moved  sa yo mo = I MOVED (not other action)

17. SCALAR PARTICLES:
    only: ta before element — ta sa mo = only I moved
    also: je after subject — sa je mo = I also moved
    even: ma before — ma sa mo = even I moved
    not yet: na pa — sa na pa mo = I haven't moved yet
    already: pa — sa pa mo = I already moved
    still: ne — sa ne mo = I am still moving
    almost: ni — sa ni mo la = I almost left
    barely: gi ma — sa gi ma mo = I barely moved

18. PURPOSE ("in order to"): da wu = BECAUSE WANT
    sa mo da wu du = I moved in order to get water

19. SIMULTANEOUS ("while"): ne je = NOW TOGETHER
    sa mo ne je to we = I moved while you spoke

20. REPORTED SPEECH: we to [content] = someone said...
    to we [sa mo hi] = they said: "I am coming"

21. EXCLAMATIONS: ve/ma at end intensifies
    ve go! = Wonderful!  ba go ve! = What joy!

22. PASSIVE (agentless): use ha (HAPPEN) or drop agent
    le gu = the tree died (no agent)  pa de vo le = the tree was cut

SOCIAL PHRASES (fixed):
  Hello: sa go ne hi | Goodbye: sa mo la | Yes: go | No: na
  Please: wu + request | Thank you: sa go da to | Sorry: sa ba bi da sa
  I don't understand: sa na te | Say again: ya we
"""


COMPOSITION_EXAMPLES = """
COMPOSITION EXAMPLES (English → PrimaTap):
  cold = na fu (NOT HEAT)
  hot = ve fu (VERY HEAT)
  dead = na li (NOT ALIVE)
  healthy = li go (ALIVE GOOD)
  sick = li bi (ALIVE BAD)
  thirsty = sa wu du (SELF WANT WATER)
  happy = ba go (FEEL GOOD)
  sad = ba bi (FEEL BAD)
  cloud = du re (WATER AIR)
  steam = du fu re (WATER HEAT AIR)
  ice = du na fu (WATER NOT-HEAT)
  fire = fu mo (HEAT MOVE)
  forest = ka le (MANY TREE)
  ocean = du ga (WATER BIG)
  rain = du mo be (WATER MOVE DOWN)
  wind = re mo (AIR MOVE)
  bird = pe li re (KIND ALIVE AIR)
  fish = pe li du (KIND ALIVE WATER)
  plant = pe li ko (KIND ALIVE SOLID)
  hungry = sa wu ze (SELF WANT SOMETHING — food context)
  eat = li ja ze (ALIVE INSIDE SOMETHING)
  drink = li ja du (ALIVE INSIDE WATER)
  afraid = ba bi da ze (FEEL BAD BECAUSE SOMETHING)
  help someone = sa wu to de (SELF WANT OTHER DO)
  cold-weather = na fu za re (NOT HEAT EXIST AIR)
  sleep = li na te (ALIVE NOT-THINK)
  dream = te yu (THINK NIGHT)
  memory = te pa (THINK BEFORE)
  hope = wu ya go (WANT FUTURE GOOD)
  story = we pa (SAY BEFORE)
  truth = su we (TRUE SAY)
  question = wu te mi (WANT THINK ?)
  learn = te ya (THINK AFTER)
  grow = li ma (ALIVE MORE)
  walk = mo fo (MOVE FOOT)
  fly = mo re va (MOVE AIR ABOVE)
  home = hi je li (HERE TOGETHER ALIVE)
  friend = to ba go (OTHER FEEL GOOD)
  enemy = to ba bi (OTHER FEEL BAD)
  child = li gi (ALIVE SMALL)
  love = ba go ma (FEEL GOOD MORE)
  war = ka pu ba bi de (MANY PEOPLE FEEL BAD DO)
  peace = ka pu ba go je (MANY PEOPLE FEEL GOOD TOGETHER)
  law = ka pu we ro (MANY PEOPLE SAY WORD)

COMPARATIVES AND DEGREE:
  bigger than you = sa ga ma lo to (SELF BIG MORE LIKE OTHER)
  as big as you = sa ga si lo to (SELF BIG SAME LIKE OTHER)
  biggest of all = sa ga ma zu (SELF BIG MORE ALL)
  worse than before = ba bi ma lo pa (FEEL BAD MORE LIKE BEFORE)

REFLEXIVES AND RECIPROCALS:
  I see myself = sa vi si (SELF SEE SAME)
  I hurt myself = sa de bi si (SELF DO BAD SAME)
  they love each other = to ba go si je (OTHER FEEL GOOD SAME TOGETHER)
  we help each other = sa je to de go si je (SELF TOGETHER OTHER DO GOOD SAME TOGETHER)

METAPHOR (lo before composition):
  like an ocean = lo du ga (LIKE WATER BIG)
  like fire = lo fu mo (LIKE HEAT MOVE)
  like the wind = lo re mo (LIKE AIR MOVE)
  I feel overwhelmed = sa ba lo du ga (SELF FEEL LIKE WATER BIG)
  your words are heavy = to ho we lo ko (OTHER HAVE WORD LIKE SOLID)

IMPERATIVES:
  come = mo hi (MOVE HERE)
  go away = mo la (MOVE FAR)
  don't move = na mo (NOT MOVE)
  please come = wu mo hi (WANT MOVE HERE)
  stop talking = de na we (DO NOT SAY)

SCALAR AND FOCUS:
  only I moved = ta sa mo (ONE SELF MOVE)
  I also moved = sa je mo (SELF TOGETHER MOVE)
  even I moved = ma sa mo (MORE SELF MOVE)
  I haven't moved yet = sa na pa mo (SELF NOT BEFORE MOVE)
  I barely moved = sa gi ma mo (SELF SMALL MORE MOVE)
  it was ME who came = yo sa mo hi (THIS SELF MOVE HERE)

PURPOSE CLAUSES:
  I moved to get water = sa mo da wu du (SELF MOVE BECAUSE WANT WATER)
  she spoke to be understood = zo we da wu to te (SOMEONE SAY BECAUSE WANT OTHER THINK)

EXCLAMATIONS:
  wonderful = ve go (VERY GOOD)
  terrible = ve bi (VERY BAD)
  what joy = ba go ve (FEEL GOOD VERY)
  how big = ga ve (BIG VERY)
"""
