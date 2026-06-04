#!/usr/bin/env python3
"""
Sago Canonize — officially add a new word to the Sago concept dictionary.

When someone proposes a word and you've decided it's right, run this.
It validates the word, checks for conflicts, adds it to concepts.json,
and rebuilds the website so the site immediately reflects the addition.

Usage:
  python3 canonize.py                            # interactive — prompts for everything
  python3 canonize.py lufa                       # check + add an existing proposal
  python3 canonize.py --list                     # list all canonical words by domain
  python3 canonize.py --check lufa               # validate without adding
  python3 canonize.py --rebuild                  # just rebuild site from current concepts.json
  python3 canonize.py --remove fumo              # un-canonize a word (keeps in json as deprecated)

After running, commit and push:
  git add language/concepts.json docs/index.html
  git commit -m "canonize: <word> — <concept>"
  git push
"""

import json
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).parent
LANG = TOOLS.parent / "language"
DOCS = TOOLS.parent / "docs"
CONCEPTS_FILE = LANG / "concepts.json"
INDEX_FILE = DOCS / "index.html"

sys.path.insert(0, str(TOOLS))
from phonics import PHONICS


# ── Validation ────────────────────────────────────────────────────────────────

def segment(word: str):
    """Split a flowing Sago word into its component phonics."""
    word = word.lower().strip()
    phonics = []
    i = 0
    while i < len(word):
        chunk = word[i:i+2]
        if chunk in PHONICS:
            phonics.append(chunk)
            i += 2
        else:
            return None
    return phonics if phonics else None


def validate_word(word: str):
    """Returns (ok, message, phonic_list)."""
    word = word.lower().strip()
    if not word:
        return False, "Empty word.", []
    if not re.match(r'^[a-z]+$', word):
        return False, "Sago words contain only lowercase a-z letters.", []
    if len(word) % 2 != 0:
        return False, f"'{word}' has {len(word)} letters — Sago words must have an even number (all phonics are 2 letters).", []
    phonics = segment(word)
    if phonics is None:
        return False, f"Could not parse '{word}' into valid phonics. Check each 2-letter pair.", []
    phonic_names = [PHONICS[c]["name"] for c in phonics]
    return True, f"Valid: {' + '.join(phonics)} = {' · '.join(phonic_names)}", phonics


def check_conflicts(word: str, concepts: dict) -> list[str]:
    """Return list of conflict descriptions."""
    conflicts = []
    if word in concepts:
        existing = concepts[word]
        conflicts.append(f"'{word}' already exists: {existing['concept']}")
    return conflicts


# ── Concepts I/O ──────────────────────────────────────────────────────────────

def load_concepts() -> dict:
    with open(CONCEPTS_FILE) as f:
        return json.load(f)


def save_concepts(data: dict):
    with open(CONCEPTS_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=False)


# ── Site rebuild ──────────────────────────────────────────────────────────────

def rebuild_site(concepts: dict):
    """Embed the full concepts.json into index.html's CONCEPTS constant."""
    if not INDEX_FILE.exists():
        print(f"  Warning: {INDEX_FILE} not found — skipping site rebuild.")
        return

    html = INDEX_FILE.read_text()
    # Build the compact JS object — only composed words for the browser
    # (primitive phonics are already in the PHONICS constant)
    composed = {
        word: {
            "word": entry["word"],
            "phonics": entry["phonics"],
            "phonic_names": entry["phonic_names"],
            "concept": entry["concept"],
            "domain": entry["domain"],
            "level": entry["level"],
        }
        for word, entry in concepts["concepts"].items()
    }

    js_data = json.dumps(composed, separators=(',', ':'), ensure_ascii=False)
    new_const = f"const CONCEPTS = {js_data};"

    # Replace the existing CONCEPTS constant
    new_html = re.sub(
        r'const CONCEPTS = \{.*?\};',
        new_const,
        html,
        flags=re.DOTALL,
    )

    if new_html == html:
        print(f"  Site already up to date: {len(composed)} concepts embedded.")
        return

    INDEX_FILE.write_text(new_html)
    print(f"  Site rebuilt: {len(composed)} concepts embedded in index.html")


# ── Display helpers ───────────────────────────────────────────────────────────

DOMAINS = [
    "action", "body", "degree", "emotion", "existence", "identity",
    "language", "life", "logic", "mental", "nature", "object",
    "physical", "quantity", "relation", "scale", "sense", "shape",
    "social", "space", "time", "value",
]


def print_entry(word: str, entry: dict):
    phonics_str = " · ".join(entry["phonics"])
    names_str = " + ".join(entry["phonic_names"])
    print(f"\n  {entry['word']}")
    print(f"  {phonics_str}  ({names_str})")
    print(f"  {entry['concept']}")
    print(f"  domain: {entry['domain']}   level: {entry['level']}")


# ── Commands ──────────────────────────────────────────────────────────────────

def cmd_check(word: str):
    ok, msg, phonics = validate_word(word)
    print(f"\n  Checking: {word}")
    if ok:
        print(f"  ✓  {msg}")
    else:
        print(f"  ✗  {msg}")
        return

    data = load_concepts()
    conflicts = check_conflicts(word, data["concepts"])
    if conflicts:
        for c in conflicts:
            print(f"  ⚠  Conflict: {c}")
    else:
        print(f"  ✓  No conflicts — '{word}' is available.")


def cmd_list(domain_filter: str = None):
    data = load_concepts()
    concepts = data["concepts"]
    by_domain: dict[str, list] = {}
    for word, entry in concepts.items():
        dom = entry.get("domain", "other")
        if domain_filter and dom != domain_filter:
            continue
        by_domain.setdefault(dom, []).append(entry)

    total = 0
    for dom in sorted(by_domain.keys()):
        entries = by_domain[dom]
        print(f"\n  {dom.upper()} ({len(entries)})")
        for e in sorted(entries, key=lambda x: x["word"]):
            phonics = " · ".join(e["phonics"])
            print(f"    {e['word']:<16} {phonics:<20} {e['concept'][:45]}")
            total += 1
    print(f"\n  Total: {total} concepts")


def cmd_add_interactive():
    print("\nSago Canonize — Add a New Word")
    print("=" * 45)
    print("Type the Sago word (flowing form, e.g. 'lufa'):")
    word = input("  Word: ").strip().lower()
    if not word:
        print("  Cancelled.")
        return

    ok, msg, phonics = validate_word(word)
    if not ok:
        print(f"  ✗  {msg}")
        return
    print(f"  ✓  {msg}")

    data = load_concepts()
    conflicts = check_conflicts(word, data["concepts"])
    if conflicts:
        for c in conflicts:
            print(f"  ⚠  {c}")
        confirm = input("  Add anyway? [y/N] ").strip().lower()
        if confirm != 'y':
            print("  Cancelled.")
            return

    phonic_names = [PHONICS[c]["name"] for c in phonics]
    gloss = " + ".join(phonic_names)
    print(f"\n  Phonics: {' · '.join(phonics)} = {gloss}")

    concept = input("  Concept (language-neutral description): ").strip()
    if not concept:
        print("  Cancelled — concept is required.")
        return

    print(f"\n  Domains: {', '.join(DOMAINS)}")
    domain = input("  Domain: ").strip().lower()
    if domain not in DOMAINS:
        print(f"  Warning: '{domain}' is not a standard domain. Using it anyway.")

    level_map = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "c": 5, "composed": 5}
    level_input = input("  Level [1-5, or press Enter for 'composed']: ").strip() or "c"
    level = level_map.get(level_input, 5)

    entry = {
        "word": word,
        "phonics": phonics,
        "phonic_names": phonic_names,
        "concept": concept,
        "domain": domain,
        "level": level,
    }

    print()
    print_entry(word, entry)
    confirm = input("\n  Canonize this word? [y/N] ").strip().lower()
    if confirm != 'y':
        print("  Cancelled.")
        return

    data["concepts"][word] = entry
    data["stats"]["total"] = len(data["concepts"])
    data["stats"]["primitive_phonics"] = sum(1 for e in data["concepts"].values() if len(e["phonics"]) == 1)
    data["stats"]["composed_words"] = sum(1 for e in data["concepts"].values() if len(e["phonics"]) > 1)
    if domain not in data.get("domains", []):
        data.setdefault("domains", []).append(domain)
        data["domains"].sort()

    save_concepts(data)
    print(f"\n  ✓  '{word}' added to concepts.json")

    rebuild_site(data)

    print(f"\n  Next: commit and push")
    print(f"    git add language/concepts.json docs/index.html")
    print(f"    git commit -m \"canonize: {word} — {concept[:40]}\"")
    print(f"    git push")


def cmd_add_direct(word: str, data: dict) -> dict:
    """Add a word non-interactively (for scripting)."""
    ok, msg, phonics = validate_word(word)
    if not ok:
        print(f"  ✗  {msg}")
        sys.exit(1)
    print(f"  ✓  {msg}")

    conflicts = check_conflicts(word, data["concepts"])
    if conflicts:
        for c in conflicts:
            print(f"  ⚠  {c}")
        sys.exit(1)

    phonic_names = [PHONICS[c]["name"] for c in phonics]
    concept = input(f"  Concept for '{word}': ").strip()
    domain = input(f"  Domain: ").strip()
    level_input = input(f"  Level [1-5]: ").strip()
    level = int(level_input) if level_input.isdigit() else 5

    entry = {
        "word": word,
        "phonics": phonics,
        "phonic_names": phonic_names,
        "concept": concept,
        "domain": domain,
        "level": level,
    }
    data["concepts"][word] = entry
    return data


def cmd_remove(word: str):
    data = load_concepts()
    word = word.lower().strip()
    if word not in data["concepts"]:
        print(f"  '{word}' not found in concepts.json.")
        return
    entry = data["concepts"][word]
    print_entry(word, entry)
    confirm = input(f"\n  Remove '{word}' from concepts.json? [y/N] ").strip().lower()
    if confirm == 'y':
        del data["concepts"][word]
        data["stats"]["total"] = len(data["concepts"])
        save_concepts(data)
        rebuild_site(data)
        print(f"  ✓  '{word}' removed.")
        print(f"  Remember: git add language/concepts.json docs/index.html && git commit && git push")
    else:
        print("  Cancelled.")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    if not args or args == ['--interactive']:
        cmd_add_interactive()

    elif args[0] == '--list':
        domain = args[1] if len(args) > 1 else None
        cmd_list(domain)

    elif args[0] == '--check' and len(args) > 1:
        cmd_check(args[1])

    elif args[0] == '--rebuild':
        data = load_concepts()
        rebuild_site(data)
        print("  Done. git add docs/index.html && git commit -m 'rebuild site' && git push")

    elif args[0] == '--remove' and len(args) > 1:
        cmd_remove(args[1])

    elif len(args) == 1 and not args[0].startswith('--'):
        # Direct word — interactive from there
        word = args[0].lower().strip()
        ok, msg, phonics = validate_word(word)
        if not ok:
            print(f"\n  ✗  {msg}")
            sys.exit(1)
        print(f"\n  {msg}")
        data = load_concepts()
        conflicts = check_conflicts(word, data["concepts"])
        if conflicts:
            for c in conflicts:
                print(f"  ⚠  Conflict: {c}")
        else:
            print(f"  ✓  Available.")
        cmd_add_interactive()

    else:
        print(__doc__)


if __name__ == "__main__":
    main()
