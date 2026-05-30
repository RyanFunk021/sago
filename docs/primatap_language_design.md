# PrimaTap Language Design
## 16 Syllables + 16-Key Keyboard Overlay

---

## The 16 Primitives and Their Syllables

Short CV syllables (consonant + vowel). Distinct consonants within each vowel group to prevent confusion when strung together.

| # | Primitive | Syllable | Mnemonic |
|---|---|---|---|
| 1 | SELF | **sa** | Self → Sa |
| 2 | OTHER | **to** | The Other → To |
| 3 | NOT | **na** | Nah → Na |
| 4 | WANT | **wu** | Want → Wu |
| 5 | GOOD | **go** | Good/Go |
| 6 | BAD | **bi** | Bad → Bi |
| 7 | NOW | **ne** | Now → Ne |
| 8 | HERE | **hi** | Here → Hi |
| 9 | MOVE | **mo** | Move → Mo |
| 10 | THINK | **te** | Think/Te |
| 11 | ALIVE | **li** | Live/Vita → Li |
| 12 | WATER | **du** | Fluid → Du |
| 13 | HEAT | **fu** | Fire → Fu |
| 14 | AIR | **re** | Breath/Air → Re |
| 15 | SOLID | **ko** | Solid → Ko |
| 16 | LIGHT | **lu** | Lux → Lu |

---

## Spoken Examples

```
sa wu du          →  I'm thirsty        (SELF WANT WATER)
na fu             →  cold               (NOT HEAT)
du re             →  cloud / rain       (WATER AIR)
sa mo hi          →  I'm coming         (SELF MOVE HERE)
to na go          →  that's wrong       (OTHER NOT GOOD)
sa te to          →  I understand you   (SELF THINK OTHER)
li na li          →  dead / asleep      (NOT ALIVE)
sa wu go ne       →  I need this now    (SELF WANT GOOD NOW)
```

Fast, short, stackable. No grammar rules beyond order.

---

## 16-Key Keyboard Overlay on QWERTY

Pinkies untouched. Thumbs = SPACE. Frequency determines row.

```
╔═══╦══════╦═══════╦══════╦═══╦═══╦═══════╦═══════╦═════╦═══╗
║ Q ║  W   ║   E   ║  R   ║ T ║ Y ║   U   ║   I   ║  O  ║ P ║
║ — ║ HEAT ║ ALIVE ║ MOVE ║ — ║ — ║ THINK ║ WATER ║ AIR ║ — ║
║   ║  fu  ║  li   ║  mo  ║   ║   ║  te   ║  du   ║ re  ║   ║
╠═══╬══════╬═══════╬══════╬═══╬═══╬═══════╬═══════╬═════╬═══╣
║ A ║  S   ║   D   ║  F   ║ G ║ H ║   J   ║   K   ║  L  ║ ; ║
║ — ║ GOOD ║ OTHER ║ SELF ║NOW║HERE║  NOT  ║ WANT  ║ BAD ║ — ║
║   ║  go  ║  to   ║  sa  ║ne ║ hi║  na   ║  wu   ║ bi  ║   ║
╠═══╬══════╬═══════╬══════╬═══╬═══╬═══════╬═══════╬═════╬═══╣
║ Z ║  X   ║   C   ║  V   ║ B ║ N ║   M   ║   ,   ║  .  ║ / ║
║ — ║  —   ║   —   ║SOLID ║ — ║LIGHT║  —  ║   —   ║  —  ║ — ║
║   ║      ║       ║  ko  ║   ║ lu ║       ║       ║     ║   ║
╚═══╩══════╩═══════╩══════╩═══╩═══╩═══════╩═══════╩═════╩═══╝
                        [ S P A C E ]
```

---

## Key Assignment Logic

**Home row — most frequent (social, logical, temporal):**
```
S=GOOD   D=OTHER   F=SELF   G=NOW
H=HERE   J=NOT     K=WANT   L=BAD
```

**Top row — medium frequency (action, biological, elemental):**
```
W=HEAT   E=ALIVE   R=MOVE
U=THINK  I=WATER   O=AIR
```

**Bottom row — least frequent (physical elements):**
```
V=SOLID   N=LIGHT
```

**Unused (pinkies):** Q A Z P ; /
**Space:** both thumbs, as normal

---

## Finger Workload

| Finger | Keys used | Primitives |
|---|---|---|
| Left pinky | none | — |
| Left ring | S, W | GOOD, HEAT |
| Left middle | D, E, C | OTHER, ALIVE |
| Left index | F, R, G, V | SELF, MOVE, NOW, SOLID |
| Right index | J, U, H, N | NOT, THINK, HERE, LIGHT |
| Right middle | K, I | WANT, WATER |
| Right ring | L, O | BAD, AIR |
| Right pinky | none | — |
| Both thumbs | SPACE | — |

Most work goes to index and middle fingers — the strongest, fastest fingers.
Pinkies rest.

---

## Typing Speed Potential

- QWERTY typist: ~60-80 wpm (26 keys, complex patterns)
- Stenographer: 225+ wpm (chord system, trained)
- PrimaTap keyboard: 16 keys, logical layout, full muscle memory in days

A fluent PrimaTap typist sending primitive sequences should comfortably exceed
speaking speed (~175 wpm equivalent meaning-units) within weeks of practice.

---

## The Complete Interface Stack

| Modality | How | Speed |
|---|---|---|
| Spoken | String CV syllables aloud | ~175 wpm |
| Keyboard | 16-key primitive layout | 200+ wpm |
| Wearable chords | 4-finger glove, eyes-free | 150+ wpm |
| Receive (deaf-blind) | Vibration motors on fingertips | passive |

All four produce and consume the same primitive sequences.
Same language. Different physical channels.

---

*PrimaTap Language Design v0.1 — Ryan Funk, May 2026*
