---
name: Word Proposal
about: Propose a new canonical Sago word for a concept
title: "Word proposal: [sago-word] — [concept]"
labels: proposal
assignees: ''
---

## Concept

<!-- What concept does this word express? Describe it without using English — what is the thing itself? -->


## Proposed Sago word

<!-- The flowing Sago word, e.g. "lufa" -->

**Word:** 

**Phonic breakdown:** `lu + fa` = LIGHT + PLANT

<!-- Validate it: python3 tools/canonize.py --check yourword -->

## Why these phonics

<!-- Why is this the right composition? What makes it semantically motivated? -->


## Domain

<!-- action / body / emotion / identity / language / life / logic / mental / nature / object / physical / quantity / relation / sense / social / space / time / value -->


## Alternatives considered

<!-- Did you consider other compositions? Why did you choose this one? -->


## Checklist

- [ ] I ran `python3 tools/canonize.py --check <word>` and it shows valid
- [ ] No conflict with an existing word in `language/concepts.json`
- [ ] The concept description is language-neutral (not just an English gloss)
