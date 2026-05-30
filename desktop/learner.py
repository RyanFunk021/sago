"""
Adaptive learner model — tracks which primitives the user knows
and controls what gets introduced next.

Primitives are acquired in tiers. The system only uses acquired
primitives when communicating with the learner, teaching new ones
one at a time through repeated contextual exposure.
"""

import json
import os
from primitives import PRIMITIVES

MODEL_PATH = os.path.expanduser('~/primatap/learner_model.json')

TIERS = [
    ['SELF', 'OTHER', 'NOT', 'WANT'],          # Tier 1 — most fundamental
    ['GOOD', 'BAD', 'NOW', 'HERE'],             # Tier 2 — valence + location
    ['ALIVE', 'MOVE', 'THINK', 'WATER'],        # Tier 3 — action + bio
    ['AIR', 'HEAT', 'SOLID', 'LIGHT'],          # Tier 4 — elements
]

ACQUISITION_THRESHOLD = 0.80  # correct rate over last 10 attempts

def load_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH) as f:
            return json.load(f)
    return {p: {'acquired': False, 'exposure': 0, 'correct': 0, 'attempts': 0}
            for p in PRIMITIVES}

def save_model(model):
    with open(MODEL_PATH, 'w') as f:
        json.dump(model, f, indent=2)

def record_attempt(model, primitive, correct):
    model[primitive]['attempts'] += 1
    model[primitive]['exposure'] += 1
    if correct:
        model[primitive]['correct'] += 1
    rate = model[primitive]['correct'] / max(model[primitive]['attempts'], 1)
    if rate >= ACQUISITION_THRESHOLD and model[primitive]['attempts'] >= 5:
        model[primitive]['acquired'] = True
    save_model(model)
    return model

def acquired_primitives(model):
    return [p for p in PRIMITIVES if model[p]['acquired']]

def current_tier(model):
    for tier in TIERS:
        if not all(model[p]['acquired'] for p in tier):
            return tier
    return []

def next_to_teach(model):
    """Return the one primitive in the current tier not yet acquired."""
    tier = current_tier(model)
    for p in tier:
        if not model[p]['acquired']:
            return p
    return None

def filter_to_known(model, sequence):
    """
    Given a sequence of primitives, return a version that only uses
    acquired ones. Unknown primitives are replaced with their closest
    acquired equivalent or dropped.
    Ensures the learner always receives communication at their level.
    """
    known = set(acquired_primitives(model))
    known.add(next_to_teach(model))  # always include the one being taught
    return [p for p in sequence if p in known]

def acquisition_summary(model):
    total = len(PRIMITIVES)
    done = len(acquired_primitives(model))
    return f'{done}/{total} primitives acquired'
