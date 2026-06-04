#!/usr/bin/env python3
"""
Build language/concepts.json — the concept-based Sago dictionary.

Primary entries are Sago words (phonic sequences as flowing words).
Not organized around English — any language speaker can use this.

Run:
  python3 build_concepts.py
Output:
  ../language/concepts.json
"""

import json
from pathlib import Path

OUT = Path(__file__).parent.parent / "language" / "concepts.json"

# ── Concept definitions ───────────────────────────────────────────────────────
# Format: (sago_word, [phonics], [phonic_names], concept_description, domain, level)
# concept_description is language-neutral — describes the thing, not an English word

CONCEPTS = [

    # ── L1 Primitive Phonics (the 8 core) ─────────────────────────────────────
    ("sa",  ["sa"],  ["SELF"],   "the one who speaks; the speaker; first person",           "identity",  1),
    ("to",  ["to"],  ["OTHER"],  "any being or thing that is not the speaker",               "identity",  1),
    ("na",  ["na"],  ["NOT"],    "negation; absence; the opposite",                          "logic",     1),
    ("wu",  ["wu"],  ["WANT"],   "desire; need; intention; motivation toward something",     "mental",    1),
    ("go",  ["go"],  ["GOOD"],   "positive; correct; beneficial; safe; well",                "value",     1),
    ("bi",  ["bi"],  ["BAD"],    "negative; harmful; wrong; dangerous; broken",              "value",     1),
    ("ne",  ["ne"],  ["NOW"],    "the present moment; immediacy; currently happening",       "time",      1),
    ("hi",  ["hi"],  ["HERE"],   "this place; where the speaker is; proximal location",     "space",     1),

    # ── L2 Primitive Phonics (physical world) ─────────────────────────────────
    ("li",  ["li"],  ["ALIVE"],  "living; animate; conscious; functioning as life does",    "life",      2),
    ("mo",  ["mo"],  ["MOVE"],   "motion; change of position or state; action",             "action",    2),
    ("te",  ["te"],  ["THINK"],  "mental activity; knowing; believing; understanding",      "mental",    2),
    ("du",  ["du"],  ["WATER"],  "liquid substance; fluid; water-like material",            "physical",  2),
    ("fu",  ["fu"],  ["HEAT"],   "thermal energy; warmth; temperature above neutral",       "physical",  2),
    ("re",  ["re"],  ["AIR"],    "gaseous matter; breath; atmosphere; the open sky",        "physical",  2),
    ("ko",  ["ko"],  ["SOLID"],  "hard matter; the tangible earth; resistance to change",   "physical",  2),
    ("lu",  ["lu"],  ["LIGHT"],  "visible energy; brightness; electromagnetic radiation",   "physical",  2),

    # ── L3 Primitive Phonics (grammar and logic) ───────────────────────────────
    ("pa",  ["pa"],  ["BEFORE"], "prior in time; earlier; what happened first",             "time",      3),
    ("ya",  ["ya"],  ["AFTER"],  "subsequent in time; later; what will happen next",        "time",      3),
    ("da",  ["da"],  ["BECAUSE"],"cause; reason; the explanation for why",                  "logic",     3),
    ("di",  ["di"],  ["IF"],     "conditional; hypothetical; the case where",               "logic",     3),
    ("pi",  ["pi"],  ["CAN"],    "ability; possibility; what is permitted or feasible",     "logic",     3),
    ("ma",  ["ma"],  ["MORE"],   "greater degree; increase; comparative augmentation",      "degree",    3),
    ("si",  ["si"],  ["SAME"],   "identical; equal; the equivalent of",                    "relation",  3),
    ("la",  ["la"],  ["FAR"],    "distant; away; remote from here",                        "space",     3),
    ("va",  ["va"],  ["ABOVE"],  "higher than; over; elevated relative to",                "space",     3),
    ("ja",  ["ja"],  ["INSIDE"], "contained within; interior; enclosed by",                "space",     3),
    ("ba",  ["ba"],  ["FEEL"],   "emotional or physical sensation; affective state",       "emotion",   3),
    ("ra",  ["ra"],  ["HEAR"],   "auditory perception; receiving sound",                   "sense",     3),
    ("we",  ["we"],  ["SAY"],    "verbal expression; communication; speaking",             "language",  3),
    ("ka",  ["ka"],  ["MANY"],   "plural; numerous; more than a few",                      "quantity",  3),
    ("bo",  ["bo"],  ["BODY"],   "the physical form; flesh; the biological structure",     "life",      3),
    ("pe",  ["pe"],  ["KIND"],   "a type or category; the sort of thing",                  "relation",  3),

    # ── L4 Primitive Phonics (completing NSM) ─────────────────────────────────
    ("zo",  ["zo"],  ["SOMEONE"], "an unspecified person; some individual",                "identity",  4),
    ("ze",  ["ze"],  ["SOMETHING"],"an unspecified thing; some entity",                   "object",    4),
    ("pu",  ["pu"],  ["PEOPLE"],  "humans collectively; the human group",                  "identity",  4),
    ("ta",  ["ta"],  ["ONE"],     "a single instance; unit; the number one",               "quantity",  4),
    ("ti",  ["ti"],  ["TWO"],     "a pair; two instances",                                 "quantity",  4),
    ("so",  ["so"],  ["SOME"],    "an indefinite portion; a number greater than one but not all", "quantity", 4),
    ("zu",  ["zu"],  ["ALL"],     "every instance; the entire set; universal",             "quantity",  4),
    ("fi",  ["fi"],  ["FEW"],     "a small number; not many",                              "quantity",  4),
    ("ga",  ["ga"],  ["BIG"],     "large in scale, size, or degree",                       "scale",     4),
    ("gi",  ["gi"],  ["SMALL"],   "small in scale, size, or degree",                       "scale",     4),
    ("no",  ["no"],  ["KNOW"],    "certain knowledge; established fact; what is verified", "mental",    4),
    ("vi",  ["vi"],  ["SEE"],     "visual perception; the sense of sight",                 "sense",     4),
    ("tu",  ["tu"],  ["TOUCH"],   "physical contact; tactile perception",                  "sense",     4),
    ("de",  ["de"],  ["DO"],      "intentional action; deliberate doing",                  "action",    4),
    ("ha",  ["ha"],  ["HAPPEN"],  "an event without an agent; occurring without intent",   "action",    4),
    ("ho",  ["ho"],  ["HAVE"],    "possession; containing; belonging to",                  "relation",  4),
    ("za",  ["za"],  ["EXIST"],   "presence; being there; there is",                       "existence", 4),
    ("gu",  ["gu"],  ["DIE"],     "ceasing to live; the end of life",                      "life",      4),
    ("su",  ["su"],  ["TRUE"],    "factual; real; actual; what is the case",               "logic",     4),
    ("ro",  ["ro"],  ["WORD"],    "a linguistic unit; a name; the vehicle of language",    "language",  4),
    ("mi",  ["mi"],  ["MAYBE"],   "uncertain; possible; perhaps",                          "logic",     4),
    ("lo",  ["lo"],  ["LIKE"],    "similar to; in the manner of; as if",                   "relation",  4),
    ("ve",  ["ve"],  ["VERY"],    "intensifier; to a great degree; strongly",              "degree",    4),
    ("ni",  ["ni"],  ["NEAR"],    "close to; proximate; almost touching",                  "space",     4),
    ("be",  ["be"],  ["BELOW"],   "lower than; under; beneath",                            "space",     4),
    ("ri",  ["ri"],  ["SIDE"],    "lateral; beside; adjacent",                             "space",     4),
    ("wi",  ["wi"],  ["WHEN"],    "at which time; the temporal question",                  "time",      4),
    ("wa",  ["wa"],  ["WHERE"],   "at which place; the spatial question",                  "space",     4),
    ("mu",  ["mu"],  ["MOMENT"],  "a brief instant; a point in time",                      "time",      4),
    ("po",  ["po"],  ["PART"],    "a component; a piece of a whole",                       "relation",  4),
    ("nu",  ["nu"],  ["ANOTHER"], "a different one; not this; an alternative",             "identity",  4),
    ("yo",  ["yo"],  ["THIS"],    "the proximal referent; what is indicated now",          "identity",  4),

    # ── L5 Molecule Phonics ────────────────────────────────────────────────────
    ("le",  ["le"],  ["TREE"],    "a tall woody plant with a trunk",                        "nature",    5),
    ("ge",  ["ge"],  ["MOON"],    "the large natural satellite visible at night",           "nature",    5),
    ("fo",  ["fo"],  ["FOOT"],    "the lowest part of the leg; the base of standing",       "body",      5),
    ("bu",  ["bu"],  ["BIRD"],    "a feathered flying vertebrate",                          "nature",    5),
    ("ru",  ["ru"],  ["ROAD"],    "a path made for travel; a route through space",          "space",     5),
    ("se",  ["se"],  ["STAR"],    "a distant sun; a point of light in the night sky",       "nature",    5),
    ("do",  ["do"],  ["DAY"],     "the period of solar light; one rotation of the earth",  "time",      5),
    ("fa",  ["fa"],  ["PLANT"],   "a rooted living thing; vegetation; flora",               "nature",    5),
    ("me",  ["me"],  ["MAN"],     "an adult male human",                                    "identity",  5),
    ("ku",  ["ku"],  ["MOTHER"],  "the female parent; the one who gave birth",              "identity",  5),
    ("je",  ["je"],  ["TOGETHER"],"in mutual company; jointly; with each other",            "relation",  5),
    ("ki",  ["ki"],  ["ANIMAL"],  "a non-plant living creature; fauna",                    "nature",    5),
    ("hu",  ["hu"],  ["FATHER"],  "the male parent; the one who contributed genetically",  "identity",  5),
    ("ye",  ["ye"],  ["EYE"],     "the visual organ; the organ of sight",                   "body",      5),
    ("he",  ["he"],  ["EARTH"],   "the ground; soil; this planet",                          "nature",    5),
    ("ji",  ["ji"],  ["HARD"],    "resistant to deformation; rigid; solid surface",         "physical",  5),
    ("vo",  ["vo"],  ["SHARP"],   "having a fine point or cutting edge",                    "physical",  5),
    ("vu",  ["vu"],  ["MOUTH"],   "the oral opening; the organ of speech",                  "body",      5),
    ("jo",  ["jo"],  ["EAR"],     "the auditory organ; the organ of hearing",               "body",      5),
    ("ju",  ["ju"],  ["ROUND"],   "circular or spherical in form",                          "shape",     5),
    ("fe",  ["fe"],  ["TASTE"],   "gustatory sense; the flavor quality of things",          "sense",     5),
    ("yi",  ["yi"],  ["BACK"],    "the posterior surface; the rear side",                   "space",     5),
    ("yu",  ["yu"],  ["NIGHT"],   "the period of darkness; solar absence",                  "time",      5),
    ("zi",  ["zi"],  ["GROUND"],  "the surface underfoot; the floor",                       "space",     5),
    ("ke",  ["ke"],  ["CLOTH"],   "woven fabric; textile material",                         "object",    5),
    ("wo",  ["wo"],  ["NOSE"],    "the olfactory organ; the organ of smell",                "body",      5),

    # ── Composed words (phonics joined into flowing words) ─────────────────────

    # Physical world
    ("nafu",    ["na","fu"],          ["NOT","HEAT"],          "absence of heat; cold temperature",                "physical",  2),
    ("fumo",    ["fu","mo"],          ["HEAT","MOVE"],         "heat in motion; combustion; fire",                 "physical",  2),
    ("dure",    ["du","re"],          ["WATER","AIR"],         "water in gaseous suspension; cloud or mist",       "physical",  2),
    ("dufure",  ["du","fu","re"],     ["WATER","HEAT","AIR"],  "water heated to gas; steam",                      "physical",  2),
    ("dunаfu",  ["du","na","fu"],     ["WATER","NOT","HEAT"],  "water in cold state; ice",                        "physical",  2),
    ("dumo",    ["du","mo"],          ["WATER","MOVE"],        "moving water; flowing liquid; river or stream",    "nature",    2),
    ("remo",    ["re","mo"],          ["AIR","MOVE"],          "air in motion; wind",                             "nature",    2),
    ("duga",    ["du","ga"],          ["WATER","BIG"],         "a large body of water; ocean or sea",             "nature",    2),
    ("lure",    ["lu","re"],          ["LIGHT","AIR"],         "diffuse light; glow; atmosphere of light",        "physical",  2),
    ("nalu",    ["na","lu"],          ["NOT","LIGHT"],         "absence of light; darkness; shadow",              "physical",  2),
    ("komo",    ["ko","mo"],          ["SOLID","MOVE"],        "slow flow of solid material; drift; glacial movement","physical",2),
    ("kova",    ["ko","va"],          ["SOLID","ABOVE"],       "solid elevated matter; mountain or rock face",    "nature",    3),

    # Life and living
    ("nali",    ["na","li"],          ["NOT","ALIVE"],         "not living; dead; the state after life ended",    "life",      2),
    ("ligo",    ["li","go"],          ["ALIVE","GOOD"],        "in a good state of life; healthy; thriving",      "life",      2),
    ("libi",    ["li","bi"],          ["ALIVE","BAD"],         "in a bad state of life; sick; ill",               "life",      2),
    ("lina",    ["li","na"],          ["ALIVE","NOT"],         "life negated; ceasing; dying",                    "life",      2),
    ("lima",    ["li","ma"],          ["ALIVE","MORE"],        "more alive; growing; becoming larger or stronger","life",      2),
    ("linаte",  ["li","na","te"],     ["ALIVE","NOT","THINK"], "living without thought; unconscious; asleep",     "life",      2),
    ("liре",    ["li","re"],          ["ALIVE","AIR"],         "breathing creature; an air-breathing being",      "life",      2),
    ("lidu",    ["li","du"],          ["ALIVE","WATER"],       "water-dwelling creature; a fish or aquatic being","nature",    2),
    ("liko",    ["li","ko"],          ["ALIVE","SOLID"],       "rooted living thing; a plant fixed to earth",     "nature",    2),

    # Emotions (all distinct by directedness)
    ("bago",    ["ba","go"],          ["FEEL","GOOD"],         "a positive affective state; pleasant feeling",    "emotion",   3),
    ("babi",    ["ba","bi"],          ["FEEL","BAD"],          "a negative affective state; unpleasant feeling",  "emotion",   3),
    ("bagoza",  ["ba","go","za"],     ["FEEL","GOOD","EXIST"], "joy; good feeling about existence itself",        "emotion",   3),
    ("bagoto",  ["ba","go","ma","to"],["FEEL","GOOD","MORE","OTHER"],"love; intense good feeling directed at another","emotion",3),
    ("bagosa",  ["ba","go","da","sa"],["FEEL","GOOD","BECAUSE","SELF"],"pride; good feeling caused by one's own action","emotion",3),
    ("bagodato",["ba","go","da","to"],["FEEL","GOOD","BECAUSE","OTHER"],"gratitude; good feeling because of another","emotion",3),
    ("bagola",  ["ba","go","ma","la"],["FEEL","GOOD","MORE","FAR"],"awe; intense good feeling before something vast","emotion",3),
    ("bagodapa",["ba","go","da","pa"],["FEEL","GOOD","BECAUSE","BEFORE"],"nostalgia; good feeling caused by the past","emotion",3),
    ("babito",  ["ba","bi","ma","to"],["FEEL","BAD","MORE","OTHER"],"anger; intense bad feeling directed at another","emotion",3),
    ("wunato",  ["wu","na","to","za"],["WANT","NOT","OTHER","EXIST"],"hate; wanting another not to exist",        "emotion",   3),
    ("babiyaze",["ba","bi","da","ya","ze"],["FEEL","BAD","BECAUSE","AFTER","SOMETHING"],"fear; bad feeling about an unknown future","emotion",3),
    ("babinaza",["ba","bi","da","na","za"],["FEEL","BAD","BECAUSE","NOT","EXIST"],"grief; bad feeling because something no longer exists","emotion",3),
    ("babisade",["ba","bi","da","sa","de","bi"],["FEEL","BAD","BECAUSE","SELF","DO","BAD"],"shame; bad feeling caused by one's own wrong action","emotion",3),
    ("babito",  ["ba","bi","da","na","to","hi"],["FEEL","BAD","BECAUSE","NOT","OTHER","HERE"],"loneliness; bad feeling because others are absent","emotion",3),
    ("dejeba",  ["de","je","ba","bi"],["DO","TOGETHER","FEEL","BAD"],"courage; acting despite fear; doing while afraid","emotion",3),
    ("wuyago",  ["wu","ya","go"],     ["WANT","AFTER","GOOD"],  "hope; desiring a future good state",             "emotion",   3),
    ("nawuyago",["na","wu","ya","go"],["NOT","WANT","AFTER","GOOD"],"despair; having given up on future good",   "emotion",   3),

    # Mental states
    ("tesu",    ["te","su"],          ["THINK","TRUE"],        "believing firmly; conviction; faith in what is real","mental",  3),
    ("tesunavi",["te","su","na","vi"],["THINK","TRUE","NOT","SEE"],"faith; believing truly without seeing",     "mental",    4),
    ("nano",    ["na","no"],          ["NOT","KNOW"],           "not knowing; uncertainty; doubt",               "mental",    4),
    ("tere",    ["te","re"],          ["THINK","AIR"],          "the breath-mind; spirit; conscious animating force","mental",  2),
    ("temigo",  ["te","mi","go"],     ["THINK","MAYBE","GOOD"], "wonder; curious awe; open-ended good wondering","mental",   3),
    ("temago",  ["te","ma","go"],     ["THINK","MORE","GOOD"],  "wisdom; thinking that leads consistently to good","mental",  4),
    ("teya",    ["te","ya"],          ["THINK","AFTER"],        "coming to know; learning; acquiring understanding","mental",  3),
    ("teyago",  ["te","pa","ya"],     ["THINK","BEFORE","AFTER"],"remembering; bringing the past into current thought","mental",3),
    ("natеpa",  ["na","te","pa"],     ["NOT","THINK","BEFORE"], "forgetting; the past thinking is gone",         "mental",    3),

    # Communication and language
    ("wena",    ["we","na"],          ["SAY","NOT"],            "being silent; refusing to speak; silence",       "language",  3),
    ("wepa",    ["we","pa"],          ["SAY","BEFORE"],         "a telling of the past; story; history",          "language",  3),
    ("wepaka",  ["we","pa","ka"],     ["SAY","BEFORE","MANY"],  "the accumulated sayings of the past; History",   "language",  5),
    ("suwе",    ["su","we"],          ["TRUE","SAY"],           "true saying; truth; a factual statement",        "language",  4),
    ("nawеsu",  ["na","we","su"],     ["NOT","SAY","TRUE"],     "a false saying; a lie",                          "language",  4),
    ("weyade",  ["we","ya","de"],     ["SAY","AFTER","DO"],     "a commitment to future action; a promise",       "language",  4),
    ("roka",    ["ro","ka"],          ["WORD","MANY"],          "many words; a language; a system of words",      "language",  4),
    ("kаpuwеro",["ka","pu","we","ro"],["MANY","PEOPLE","SAY","WORD"],"governance by the words of many; democracy","social",  5),

    # Social concepts
    ("jeliti",  ["je","li","ti"],     ["TOGETHER","ALIVE","TWO"],"two lives lived together; partnership; marriage","social",  5),
    ("kаpuhi",  ["ka","pu","hi"],     ["MANY","PEOPLE","HERE"], "many people gathered here; a town or city",     "social",   4),
    ("kahili",  ["hi","je","li"],     ["HERE","TOGETHER","ALIVE"],"where living happens together; home",         "social",   3),
    ("kаpubabide",["ka","pu","ba","bi","de"],["MANY","PEOPLE","FEEL","BAD","DO"],"many people doing bad to each other; war","social",5),
    ("kаpubagoje",["ka","pu","ba","go","je"],["MANY","PEOPLE","FEEL","GOOD","TOGETHER"],"many people feeling good together; peace","social",5),
    ("надena",  ["na","de","na"],     ["NOT","DO","NOT"],        "the absence of prevention; freedom",            "social",   4),
    ("degokаpu",["de","go","ka","pu"],["DO","GOOD","MANY","PEOPLE"],"doing good for many; justice",              "social",   5),

    # Nature (composed)
    ("kаle",    ["ka","le"],          ["MANY","TREE"],          "many trees; a forest; woodland",                 "nature",   5),
    ("dumoru",  ["du","mo","ru"],     ["WATER","MOVE","ROAD"],  "water moving on a road; a river",               "nature",   3),
    ("dumobe",  ["du","mo","be"],     ["WATER","MOVE","DOWN"],  "water moving downward; rain",                   "nature",   3),
    ("kaki",    ["ka","ki"],          ["MANY","ANIMAL"],        "a group of animals; a herd or flock",            "nature",   5),
    ("kabu",    ["ka","bu"],          ["MANY","BIRD"],          "many birds; a flock of birds",                   "nature",   5),
    ("luga",    ["lu","ga"],          ["LIGHT","BIG"],          "a great source of light; the sun",               "nature",   3),
    ("lugodo",  ["lu","ga","do"],     ["LIGHT","BIG","DAY"],    "the great light of the day; the sun in context","nature",   3),
    ("geyu",    ["ge","yu"],          ["MOON","NIGHT"],         "the moon at night; moonlight",                   "nature",   5),
    ("hebе",    ["he","be"],          ["EARTH","BELOW"],        "deep earth; underground; the depths of soil",   "nature",   5),

    # Actions (composed)
    ("mofo",    ["mo","fo"],          ["MOVE","FOOT"],          "moving on foot; walking",                        "action",   3),
    ("movefo",  ["mo","ve","fo"],     ["MOVE","VERY","FOOT"],   "moving fast on foot; running",                  "action",   3),
    ("moreva",  ["mo","re","va"],     ["MOVE","AIR","ABOVE"],   "moving through the air upward; flying",          "action",   3),
    ("modu",    ["mo","du"],          ["MOVE","WATER"],         "moving through water; swimming",                 "action",   3),
    ("lijazedu",["li","ja","du"],     ["ALIVE","INSIDE","WATER"],"taking water inside while alive; drinking",    "action",   3),
    ("lijazе",  ["li","ja","ze"],     ["ALIVE","INSIDE","SOMETHING"],"taking something inside while alive; eating","action", 3),
    ("dekago",  ["de","ka","go"],     ["DO","MANY","GOOD"],     "doing good repeatedly or for many; to help",    "action",   4),
    ("wuto",    ["wu","to","de"],     ["WANT","OTHER","DO"],    "wanting another to act; asking for help",       "action",   3),

    # Time (composed)
    ("nepa",    ["ne","pa"],          ["NOW","BEFORE"],         "just now past; a moment ago",                   "time",     3),
    ("neya",    ["ne","ya"],          ["NOW","AFTER"],          "about to happen; imminently; very soon",        "time",     3),
    ("pala",    ["pa","la"],          ["BEFORE","FAR"],         "long ago; distant past; ancient time",          "time",     3),
    ("yala",    ["ya","la"],          ["AFTER","FAR"],          "far in the future; a long time hence",          "time",     3),
    ("pado",    ["pa","do"],          ["BEFORE","DAY"],         "before today; yesterday",                       "time",     5),
    ("yado",    ["ya","do"],          ["AFTER","DAY"],          "after today; tomorrow",                         "time",     5),
    ("doyu",    ["do","yu"],          ["DAY","NIGHT"],          "a full cycle of day and night; a full day",     "time",     5),
    ("gamu",    ["ga","mu"],          ["BIG","MOMENT"],         "a long time; extended duration",                "time",     3),
    ("gimu",    ["gi","mu"],          ["SMALL","MOMENT"],       "a brief time; short duration",                  "time",     3),
    ("tepayu",  ["te","pa"],          ["THINK","BEFORE"],       "thinking of the past; memory",                  "mental",   3),
    ("teyu",    ["te","yu"],          ["THINK","NIGHT"],        "thinking in the dark; dreaming",                "mental",   3),

    # Properties
    ("vigo",    ["vi","go"],          ["SEE","GOOD"],           "good to see; pleasing to the eye; beautiful",   "value",    4),
    ("lugu",    ["lu","go"],          ["LIGHT","GOOD"],         "good light; brightness that feels right; beautiful","value",4),
    ("gobo",    ["go","bo"],          ["GOOD","BODY"],          "a body in good condition; fit; physically well", "life",    3),
    ("kota",    ["ko","ta"],          ["SOLID","ONE"],          "a single solid object; a stone or unit of matter","object",  3),
    ("judu",    ["ju","du"],          ["ROUND","WATER"],        "a sphere of water; a drop; a round liquid form", "object",  5),
    ("juko",    ["ju","ko"],          ["ROUND","SOLID"],        "a round solid object; a ball or sphere",         "object",  5),
    ("voko",    ["vo","ko"],          ["SHARP","SOLID"],        "a sharp solid object; a blade or point",         "object",  5),
]


def build():
    entries = {}
    for row in CONCEPTS:
        word, phonics, phonic_names, concept, domain, level = row
        entries[word] = {
            "word": word,
            "phonics": phonics,
            "phonic_names": phonic_names,
            "concept": concept,
            "domain": domain,
            "level": level,
        }

    output = {
        "schema": "sago-concept-dictionary-v2",
        "description": (
            "Language-neutral concept dictionary for Sago. "
            "Primary entries are Sago words, not English translations. "
            "Any language speaker can use this by searching domain and concept."
        ),
        "stats": {
            "total": len(entries),
            "primitive_phonics": sum(1 for e in entries.values() if len(e["phonics"]) == 1),
            "composed_words": sum(1 for e in entries.values() if len(e["phonics"]) > 1),
        },
        "domains": sorted(set(e["domain"] for e in entries.values())),
        "concepts": entries,
    }

    OUT.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"Written {len(entries)} concepts to {OUT}")
    print(f"  Primitive phonics: {output['stats']['primitive_phonics']}")
    print(f"  Composed words:   {output['stats']['composed_words']}")
    print(f"  Domains: {', '.join(output['domains'])}")


if __name__ == "__main__":
    build()
