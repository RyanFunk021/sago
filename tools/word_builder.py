#!/usr/bin/env python3
"""
Sago Word Builder
==================
Look up or create a Sago composition for any English word or concept.

Checks the existing dictionary first. If not found, uses the Sago primitive
system to compose a new word, explains the reasoning, and offers to add it
to the dictionary.

Usage:
  python3 word_builder.py "photosynthesis"
  python3 word_builder.py "democracy" --add
  python3 word_builder.py --lookup "freedom"
  python3 word_builder.py --interactive
  python3 word_builder.py --validate "na de na"

Requires: anthropic  (pip install anthropic)
API key:  set ANTHROPIC_API_KEY environment variable
"""

import argparse
import json
import os
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).parent
LANG_DIR = TOOLS_DIR.parent / "language"
DICT_FILE = LANG_DIR / "dictionary.json"

sys.path.insert(0, str(TOOLS_DIR))
from phonics import PHONICS, BY_NAME, GRAMMAR_RULES, COMPOSITION_EXAMPLES, phonic_inventory_string


# ── API ───────────────────────────────────────────────────────────────────────

def load_api_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key:
        # Try common credential locations
        for path in [
            Path.home() / ".anthropic" / "key",
            Path("/Users/ryanfunk/projects/wordlens/creds.json"),
        ]:
            if path.exists():
                text = path.read_text()
                if path.suffix == ".json":
                    key = json.loads(text).get("ANTHROPIC_API_KEY", "")
                else:
                    key = text.strip()
                if key:
                    break
    if not key:
        import getpass
        key = getpass.getpass("ANTHROPIC_API_KEY: ").strip()
    return key


# ── Dictionary ────────────────────────────────────────────────────────────────

def load_dict() -> dict:
    if DICT_FILE.exists():
        with open(DICT_FILE) as f:
            return json.load(f)
    return {}


def save_dict(d: dict):
    DICT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DICT_FILE, "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False, sort_keys=True)


# ── Composition ───────────────────────────────────────────────────────────────

WORD_BUILDER_SYSTEM = f"""You are an expert in Sago, a semantic primitive language built from Wierzbicka's Natural Semantic Metalanguage.

PHONIC INVENTORY (90 CV syllables, each encodes exactly one primitive):
{phonic_inventory_string()}

{GRAMMAR_RULES}

{COMPOSITION_EXAMPLES}

WORD CREATION RULES:
1. Use 1–5 phonic syllables to compose the concept
2. Prefer fewer phonics (more compressed = more elegant)
3. The composition should feel semantically motivated — someone should be able to guess the meaning from the phonics
4. Avoid compositions that are already used for common words (check examples above)
5. If the concept is institutional (government, money, brand names, technical jargon with no semantic equivalent) — say so explicitly
6. type: "single" | "composition" | "institutional"

For institutional concepts, explain why they can't be primitively encoded and suggest the closest approximation.

Respond ONLY as JSON (no markdown fences):
{{
  "word": "...",
  "phonics": ["syl1", "syl2"],
  "phonic_names": ["NAME1", "NAME2"],
  "type": "single|composition|institutional",
  "confidence": 0.0,
  "gloss": "one-line explanation of why these phonics = this concept",
  "note": "optional longer explanation or alternatives"
}}"""


def compose_word(client, concept: str) -> dict:
    import anthropic
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        system=[{"type": "text", "text": WORD_BUILDER_SYSTEM, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": f'Create a Sago word for: "{concept}"'}],
    )
    text = response.content[0].text.strip()
    # Strip markdown fences if present
    if text.startswith("```"):
        text = "\n".join(text.split("\n")[1:-1])
    result = json.loads(text)
    # Validate phonics
    valid_syls = set(PHONICS.keys())
    result["phonics"] = [t for t in result.get("phonics", []) if t in valid_syls]
    result["phonic_names"] = [PHONICS[t]["name"] for t in result["phonics"]]
    return result


def segment_word(word: str):
    """Try to segment a flowing Sago word into its component phonics (greedy, left-to-right)."""
    word = word.lower()
    result = []
    i = 0
    while i < len(word):
        matched = False
        for length in (2,):  # all phonics are exactly 2 characters (CV)
            candidate = word[i:i+length]
            if candidate in PHONICS:
                result.append(candidate)
                i += length
                matched = True
                break
        if not matched:
            return None  # couldn't segment
    return result if result else None


def validate_composition(taps_str: str) -> dict:
    """Parse and validate phonic sequences or flowing composed words."""
    tokens = taps_str.lower().split()
    valid = []
    invalid = []
    segmented_from = []

    for token in tokens:
        if token in PHONICS:
            valid.append(token)
        else:
            # Try to segment it as a flowing composed word (nafu → na + fu)
            parts = segment_word(token)
            if parts:
                valid.extend(parts)
                segmented_from.append((token, parts))
            else:
                invalid.append(token)

    result = {
        "input": taps_str,
        "valid_phonics": valid,
        "invalid_tokens": invalid,
        "phonic_names": [PHONICS[t]["name"] for t in valid],
        "gloss": " + ".join(PHONICS[t]["name"] for t in valid),
        "is_valid": len(invalid) == 0 and len(valid) > 0,
    }
    if segmented_from:
        result["segmented"] = {w: parts for w, parts in segmented_from}
    return result


# ── Display ───────────────────────────────────────────────────────────────────

def print_entry(word: str, entry: dict, source: str = ""):
    phonics_str = " ".join(entry.get("phonics", []))
    names_str = " · ".join(entry.get("phonic_names", []))
    t = entry.get("type", "?")
    conf = entry.get("confidence", 0)
    gloss = entry.get("gloss", "")
    note = entry.get("note", "")

    src_tag = f"  [{source}]" if source else ""
    print(f"\n  {word}{src_tag}")

    if t == "institutional":
        print(f"  ✗  Institutional — no primitive equivalent")
        if gloss:
            print(f"     {gloss}")
        if note:
            print(f"     {note}")
    else:
        print(f"  {phonics_str}")
        print(f"  {names_str}")
        if gloss:
            print(f'  “{gloss}”')
        print(f"  type: {t}   confidence: {conf:.2f}")
        if note:
            print(f"  note: {note}")


# ── Commands ──────────────────────────────────────────────────────────────────

def cmd_lookup(word: str, dictionary: dict):
    word = word.lower().strip()
    if word in dictionary:
        print_entry(word, dictionary[word], source="dictionary")
    else:
        print(f"\n  '{word}' not found in dictionary.")
        print(f"  Run without --lookup to compose it.")


def cmd_build(concept: str, client, dictionary: dict, add: bool = False):
    concept_lower = concept.lower().strip()

    # Check dictionary first
    if concept_lower in dictionary:
        print_entry(concept_lower, dictionary[concept_lower], source="dictionary")
        return

    print(f"\n  Composing '{concept}'...", end=" ", flush=True)
    entry = compose_word(client, concept)
    print("done")

    print_entry(concept_lower, entry)

    try:
        prompt_add = (not add and entry.get("type") != "institutional" and
                      input("\n  Add to dictionary? [y/N] ").strip().lower() == "y")
    except EOFError:
        prompt_add = False
    if add or prompt_add:
        dictionary[concept_lower] = entry
        save_dict(dictionary)
        print(f"  Saved to {DICT_FILE.name}")


def cmd_validate(taps_str: str):
    result = validate_composition(taps_str)
    print(f"\n  Input:  {result['input']}")
    if result["is_valid"]:
        print(f"  Phonics: {' '.join(result['valid_phonics'])}")
        print(f"  Gloss:   {result['gloss']}")
        if result.get("segmented"):
            for word, parts in result["segmented"].items():
                print(f"  Parsed: {word} → {' + '.join(parts)}")
    else:
        if result["valid_phonics"]:
            print(f"  Valid phonics:   {' '.join(result['valid_phonics'])}")
        if result["invalid_tokens"]:
            print(f"  Could not parse: {' '.join(result['invalid_tokens'])}")
            print(f"  Hint: use space-separated phonics (na fu) or a valid composed word (nafu)")


def cmd_interactive(client, dictionary: dict):
    print("\nSago Word Builder — Interactive Mode")
    print("Commands: lookup <word>, build <concept>, validate <phonics>, quit\n")
    while True:
        try:
            line = input("sago> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue
        parts = line.split(None, 1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if cmd in ("quit", "exit", "q"):
            break
        elif cmd == "lookup" and arg:
            cmd_lookup(arg, dictionary)
        elif cmd == "build" and arg:
            cmd_build(arg, client, dictionary, add=False)
        elif cmd == "validate" and arg:
            cmd_validate(arg)
        elif cmd in ("lookup", "build", "validate"):
            print("  Missing argument.")
        else:
            # Treat whole line as a build request
            cmd_build(line, client, dictionary, add=False)


def cmd_stats(dictionary: dict):
    types = {}
    for v in dictionary.values():
        t = v.get("type", "?")
        types[t] = types.get(t, 0) + 1
    confs = [v["confidence"] for v in dictionary.values() if v.get("confidence", 0) > 0]

    print(f"\n  Dictionary: {len(dictionary)} entries")
    for k, v in sorted(types.items(), key=lambda x: -x[1]):
        bar = "█" * (v // 50)
        print(f"  {k:<16} {v:5d}  {bar}")
    if confs:
        print(f"  Avg confidence: {sum(confs)/len(confs):.3f}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Sago Word Builder — look up or compose any concept in Sago",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 word_builder.py photosynthesis
  python3 word_builder.py "democracy" --add
  python3 word_builder.py --lookup freedom
  python3 word_builder.py --validate "na de na"
  python3 word_builder.py --interactive
  python3 word_builder.py --stats
        """,
    )
    parser.add_argument("concept", nargs="?", help="Word or concept to build")
    parser.add_argument("--lookup", "-l", metavar="WORD", help="Look up in dictionary only (no API)")
    parser.add_argument("--validate", "-v", metavar="PHONICS", help="Validate a phonic sequence")
    parser.add_argument("--add", "-a", action="store_true", help="Auto-add result to dictionary")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")
    parser.add_argument("--stats", "-s", action="store_true", help="Show dictionary stats")
    args = parser.parse_args()

    dictionary = load_dict()

    if args.stats:
        cmd_stats(dictionary)
        return

    if args.lookup:
        cmd_lookup(args.lookup, dictionary)
        return

    if args.validate:
        cmd_validate(args.validate)
        return

    # Need API for build and interactive
    if args.interactive or args.concept:
        import anthropic
        api_key = load_api_key()
        client = anthropic.Anthropic(api_key=api_key)

        if args.interactive:
            cmd_interactive(client, dictionary)
        elif args.concept:
            cmd_build(args.concept, client, dictionary, add=args.add)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
