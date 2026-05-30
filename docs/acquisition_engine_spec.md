# PrimaTap Acquisition Engine — System Specification

**Version 0.1 — May 2026**

---

## Overview

The Acquisition Engine is the AI core of PrimaTap learning. It generates a living visual world that narrates itself in semantic primitives — exactly the way a parent's speech narrates the world to a baby. No lessons. No explanations. No curriculum. Just a world that talks.

The learner watches. The primitives arrive — as sound, vibration, or glyphs depending on their mode. Patterns accumulate. Fluency emerges.

---

## Core Design Principles

**1. Meaning is always grounded**
Every primitive is delivered at the moment its referent appears or acts on screen. SOLID appears when a rock appears. MOVE appears when it moves. Never in isolation. Never as an abstraction.

**2. Nobody explains anything**
No definitions. No translations. No "SOLID means a physical object." The AI shows a rock. You feel SOLID. A hundred rocks, trees, cups, walls later — you know what SOLID means. The same way you know what "red" means without ever having read a definition.

**3. The world is the teacher**
The AI generates scenes. The scenes generate primitives. The learner receives primitives. The loop is: world → meaning → learner. Not: teacher → rule → learner.

**4. Acquisition, not instruction**
The engine tracks what the learner knows by watching their anticipation — do they tap the primitive before the prompt arrives? Acquisition is measured by prediction, not recall.

---

## Learning Stages

### Stage 1 — Single Primitives (Days 1-3)
One primitive at a time. Vivid, unambiguous visuals. Immediate delivery.

| Scene | Primitive delivered |
|---|---|
| A rock sits on screen | SOLID |
| It bounces | MOVE |
| Rain falls | WATER |
| Fire appears | HEAT |
| Wind blows leaves | AIR |
| Sun rises | LIGHT |
| Darkness falls | NOT + LIGHT |
| A creature blinks | ALIVE |
| Creature reaches for rock | WANT |
| Two creatures appear | OTHER |

The engine cycles through all 15 primitives across hundreds of small vivid moments. Same primitive, different objects, different contexts — building generalization.

### Stage 2 — Two-Primitive Combinations (Days 4-14)
The world becomes slightly more complex. Events happen. Cause follows effect.

```
Rock falls into water     →  SOLID + WATER
Water heats up, steams    →  WATER + HEAT
Steam rises into air      →  WATER + HEAT + AIR  (sneak preview of Stage 3)
Creature moves toward rock →  ALIVE + MOVE
Creature wants the water  →  OTHER + WANT + WATER
Light disappears          →  NOT + LIGHT
Creature is unhappy       →  OTHER + NOT + GOOD
```

The engine introduces combinations gradually, always reusing primitives the learner has seen before, combining them in new ways.

### Stage 3 — Three-Chord Sequences (Weeks 2-4)
Narrative begins. Simple stories. Cause, effect, reaction.

```
Creature is cold (NOT + HEAT + OTHER)
Creature wants fire (OTHER + WANT + HEAT)
Fire appears — creature is good (OTHER + GOOD + NOW)
```

Short loops. Repeated with variation. The learner starts to feel narrative rhythm — the emotional arc of primitive sequences.

### Stage 4 — Full Scenes and Agency (Month 2+)
The learner begins to interact. The world responds to their chords. They make things happen.

- Tap MOVE → something on screen moves
- Tap WATER → rain falls
- Tap NOT + LIGHT → screen dims
- Tap OTHER + WANT → a creature reaches for something

The learner is no longer a receiver. They are a participant. The world speaks their language back to them.

---

## AI Components

### Scene Generator
Produces short looping visual scenes (3-10 seconds) featuring objects and creatures acting out primitive meanings.

**Inputs:**
- Current stage
- Primitives already acquired
- Target primitive(s) for this scene
- Learner's confusion history (which primitives they've mixed up before)

**Outputs:**
- Visual scene description → rendered via image generation AI (DALL-E, Stable Diffusion, or procedural animation)
- Primitive sequence to deliver, timestamped to scene events
- Scene metadata for logging

**Scene types:**
- Object appearance (single primitive)
- Object interaction (two primitives)
- Creature intent (WANT, SELF, OTHER)
- Environmental change (HEAT, WATER, AIR, LIGHT)
- Narrative loop (three+ primitives in sequence)

### Primitive Delivery System
Delivers primitives to the learner in sync with scene events, in their selected mode:

| Mode | Delivery |
|---|---|
| Audio | Distinct tone or invented syllable per primitive |
| Tactile | Vibration pattern on finger(s) |
| Visual | Glyph flashes on screen overlay |
| Combined | Any combination of above |

Delivery is precisely timestamped to the moment the referent appears or acts on screen.

### Acquisition Tracker
Watches the learner's responses and builds a model of what they know.

**Metrics per primitive:**
- `exposure_count` — how many times seen
- `anticipation_rate` — how often learner responds before prompt
- `confusion_pairs` — which other primitives this one gets mixed up with
- `acquired` — boolean, set when anticipation_rate > 0.85 over 20 trials

**Acquisition threshold:** A primitive is considered acquired when the learner consistently anticipates it — taps it before the audio/vibration prompt arrives — across varied scenes and object types.

**Adaptive logic:**
- If a primitive has low anticipation rate → increase exposure frequency, try different visual contexts
- If two primitives are frequently confused → generate contrast scenes that highlight the difference
- If anticipation rate > 0.85 → graduate to combinations involving this primitive
- Never introduce a combination until both component primitives are acquired

### Curriculum Planner
Decides what to show next based on the acquisition model.

```
Algorithm:
1. Identify primitives with exposure_count < 20  →  prioritize
2. Identify acquired primitives  →  available for combinations
3. If |acquired| >= 2  →  introduce combinations
4. If combination acquisition_rate > 0.75  →  introduce in narrative sequences
5. Always interleave new primitives with review of recently acquired ones
6. Ratio: 70% known material, 30% new — mirrors Krashen's i+1 principle
```

### Feedback Engine
Responds to learner input in Stage 4 with world events.

- Learner taps a valid chord → world responds visually to that primitive's meaning
- Learner taps an unrecognized chord → gentle visual question mark, replay the scene
- Learner taps correctly before prompt → scene celebrates (creature dances, colors brighten)
- No punishment for errors — only more exposure

---

## Learner Model (Persistent)

Stored per user, updated after every session:

```json
{
  "user_id": "...",
  "stage": 2,
  "session_count": 14,
  "total_exposure_minutes": 87,
  "primitives": {
    "SOLID":  { "acquired": true,  "anticipation_rate": 0.91, "exposure_count": 203 },
    "WATER":  { "acquired": true,  "anticipation_rate": 0.88, "exposure_count": 187 },
    "MOVE":   { "acquired": true,  "anticipation_rate": 0.86, "exposure_count": 176 },
    "HEAT":   { "acquired": false, "anticipation_rate": 0.61, "exposure_count": 94  },
    "AIR":    { "acquired": false, "anticipation_rate": 0.43, "exposure_count": 67  },
    ...
  },
  "combinations_acquired": [
    ["SOLID", "WATER"],
    ["ALIVE", "MOVE"]
  ],
  "confusion_pairs": [
    ["HEAT", "LIGHT"],
    ["AIR", "MOVE"]
  ]
}
```

This model travels with the learner across all three PrimaTap apps — Learn, Watch, and Type. Progress in one mode accelerates the others.

---

## The TV Mode Integration

Any video stream can be run through the Acquisition Engine in parallel:

1. Audio transcribed in real time (Whisper)
2. Transcript mapped to primitive sequences (PrimaTap dictionary + LLM)
3. Primitives delivered in sync with speech — vibration, glyphs, or audio tones
4. Learner model updated based on anticipation responses

The learner watches their favorite show. The show teaches them PrimaTap. They don't study. They watch TV.

---

## The Narration Mode Integration

A mobile camera points at the world. The AI identifies objects and actions in the frame and delivers primitives in real time:

- Camera sees a glass of water → WATER + SOLID
- User picks it up → SELF + MOVE + SOLID
- User drinks → SELF + WANT + WATER (satisfied)
- User sets it down → SOLID + HERE

The world narrates itself. Every moment of every day is a lesson that doesn't feel like a lesson.

---

## Success Metrics

| Milestone | Target |
|---|---|
| All 15 primitives acquired | 2-4 weeks |
| 50 two-primitive combinations fluent | 6-8 weeks |
| Basic three-chord sentences | 10-12 weeks |
| Computer control via chords | 12-16 weeks |
| Peer-to-peer conversation | 4-6 months |

These targets assume 30-60 minutes of daily exposure across any combination of modes. They are faster than any natural language acquisition timeline for a comparable expressive range, for one reason: the system was designed to be learned, not evolved to be spoken.

---

## Open Questions

- What visual primitives best ground abstract concepts (WANT, NOT, SELF, GOOD, BAD)?
- Does audio tone design affect acquisition speed? (musical intervals vs. arbitrary tones vs. invented syllables)
- Can the confusion-pair detection generalize across learners to improve the global primitive design?
- At what anticipation rate does a learner stop needing audio/tactile prompts entirely?

---

*PrimaTap Acquisition Engine — specification v0.1*
*Ryan Funk, May 2026*
