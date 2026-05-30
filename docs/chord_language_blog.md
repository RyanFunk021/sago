# What If Language Didn't Need Words?

*A new communication system for deaf, blind, and deaf-blind people — built from the ground up*

---

I've been thinking about a problem that doesn't get enough attention: how do deaf-blind people communicate? Most people know about Braille — a tactile system of raised dots that maps to letters. But letters map to sounds, and sounds are something a deaf-blind person has never experienced. We're asking people to learn a system built on a sense they don't have, just to access meaning they already possess.

What if we built something different from scratch?

## The Idea: Language as Primitives

Here's the insight that started this. In the field of NLP — the branch of AI that deals with language — researchers discovered something surprising. You can represent the *meaning* of any word as a point in a high-dimensional mathematical space. Words with similar meanings cluster together. "Hot" and "warm" are neighbors. "King" minus "man" plus "woman" lands near "queen."

This space is called an embedding space, and it has hundreds of dimensions. But here's the thing: **most of the meaningful variation in human language can be traced back to a small set of fundamental concepts.**

Linguist Anna Wierzbicka spent decades arguing that all human meaning — across every language on earth — reduces to about 65 semantic primitives. Things like: SELF, OTHER, NOT, WANT, GOOD, BAD, HERE, NOW, ALIVE, MOVE.

What if those primitives were the alphabet?

## The Device

Imagine a small glove with vibration motors on the fingertips. A hearing parent speaks normally. The device listens, converts speech to text, maps the meaning onto semantic primitives, and squeezes the child's fingers in the corresponding pattern. WANT. WATER. SELF. MOVE. No letters. No sounds. No training required from the parent — they just talk.

The child responds by tapping their fingers back in chord patterns, like a tiny piano. The device maps those chords to primitives, reconstructs the meaning, and speaks it aloud to the parent. The AI is the interpreter, running both directions in real time.

```
Parent speaks
    ↓ speech-to-text
    ↓ NLP → semantic primitives
    ↓ device squeezes child's fingers
Child understands

Child taps finger chords
    ↓ chords → semantic primitives
    ↓ primitives → natural language
    ↓ spoken aloud
Parent hears
```

The child builds thoughts as sequences of primitives:

- `WANT + WATER` → thirsty
- `NOT + HEAT` → cold (without needing a word for cold)
- `WATER + AIR` → cloud, mist, rain
- `SELF + MOVE + HERE` → I'm coming

The most frequently used concepts get the simplest chords — one finger instead of four. This is the same principle used in Morse code (E is just a single dot because it's the most common letter) and in data compression algorithms. Frequent things should be cheap.

## Why This Could Work

**It bypasses the phoneme problem.** Every written language is secretly a code for spoken sounds. Braille is a code for English letters which are codes for English sounds. Deaf-blind readers are decoding a code of a code of something they've never experienced. This system skips all that — it's meaning directly to meaning.

**It's learnable in stages.** You start with a memory game. Can you learn to distinguish 4 tactile patterns? Level 1. Can you learn that two patterns together mean something new? Level 2. The progression mirrors how children naturally learn language — concrete before abstract, simple before complex.

**The same language works in both directions.** The device taps primitives to you. You tap primitives back. One system, full conversation.

**It's not just for deaf-blind people.** The same chord keyboard works as a visual display for deaf people — no sound required. For blind people, the chords could produce audio tones. For non-verbal people. For communication across language barriers — because WANT + WATER means the same thing whether you grew up speaking English, Mandarin, or Swahili.

## What I've Built So Far

I ran a quick experiment using sentence transformers — an AI model that converts words into their embedding space coordinates. I took 16 candidate primitives and visualized how spread out they are in meaning-space. The more spread out, the more information each one carries, and the better they work as a primitive alphabet.

I also tested composition: does averaging the vectors for WATER and AIR land near concepts like "cloud" or "mist"? The answer is directionally yes, and the experiment pointed toward exactly what needs to be refined next.

The chord keyboard design gives 15 usable combinations from just 4 fingers — enough to cover a full primitive set. Add two thumbs and you get 64 combinations, the same as Braille, but faster to input and not tied to any spoken language.

## What's Next

The first real experiment is simple: can people learn to distinguish 15 tactile patterns? Not deaf-blind people yet — just regular people, in a learning game, with a small reward for correct answers. If the answer is yes, and the learning curve is reasonable, the next question is whether two-pattern sequences reliably convey compound concepts.

This is testable. It's buildable with off-the-shelf hardware. And if it works, it opens a door to something genuinely new — a communication channel designed from first principles for the people who need it most.

I'm sharing this early because I think the idea is bigger than any one person. If you work in assistive technology, linguistics, cognitive science, or just think this is interesting — I'd love to hear from you.

## One More Thing

Think about what this system does for a deaf child communicating with hearing parents. The parent talks. The AI translates. The child responds in chords. No interpreter needed, no special training for the parent.

But that child — the one who grows up thinking in semantic primitives instead of the ambiguous, phoneme-laden mess of natural language — is going to outthink all of us.

Natural language is full of noise: irregular exceptions, borrowed metaphors, words that mean six things at once. A mind trained from the start on pure compositional meaning, where every concept is explicitly built from parts, has a different cognitive foundation. The notation you think *in* shapes what you can think. Mathematicians know this. Leibniz's calculus notation made calculus teachable; Newton's kept it obscure for a century in England.

Now imagine two of these children talking to each other.

No translation layer. No natural language overhead. Just two minds operating directly at the semantic primitive level, passing pure compressed meaning back and forth at full speed. No ambiguity, no noise, no fuzziness borrowed from a spoken language neither of them uses.

We frame assistive technology as closing a gap. What if the constraint is the advantage?

---

*This is version 0.1 of an idea. The experiment is just beginning.*

*— Ryan Funk, May 2026*
