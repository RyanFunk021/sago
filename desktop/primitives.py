PRIMITIVES = {
    'SELF':  {'syllable': 'sa', 'key': 'f', 'emoji': '👤', 'meaning': 'I, me, my'},
    'OTHER': {'syllable': 'to', 'key': 'd', 'emoji': '👥', 'meaning': 'you, they, it'},
    'NOT':   {'syllable': 'na', 'key': 'j', 'emoji': '❌', 'meaning': 'no, negation, opposite'},
    'WANT':  {'syllable': 'wu', 'key': 'k', 'emoji': '🤲', 'meaning': 'desire, need, wish'},
    'GOOD':  {'syllable': 'go', 'key': 's', 'emoji': '✅', 'meaning': 'positive, correct, safe'},
    'BAD':   {'syllable': 'bi', 'key': 'l', 'emoji': '⚠️',  'meaning': 'negative, wrong, danger'},
    'NOW':   {'syllable': 'ne', 'key': 'g', 'emoji': '⚡', 'meaning': 'present time, immediate'},
    'HERE':  {'syllable': 'hi', 'key': 'h', 'emoji': '📍', 'meaning': 'this place, location'},
    'ALIVE': {'syllable': 'li', 'key': 'e', 'emoji': '💚', 'meaning': 'living, active, conscious'},
    'MOVE':  {'syllable': 'mo', 'key': 'r', 'emoji': '➡️', 'meaning': 'motion, action, go'},
    'WATER': {'syllable': 'du', 'key': 'i', 'emoji': '💧', 'meaning': 'liquid, fluid'},
    'AIR':   {'syllable': 're', 'key': 'o', 'emoji': '🌬️', 'meaning': 'gas, breath, sky, wind'},
    'HEAT':  {'syllable': 'fu', 'key': 'w', 'emoji': '🔥', 'meaning': 'temperature, energy, fire'},
    'SOLID': {'syllable': 'ko', 'key': 'v', 'emoji': '🪨', 'meaning': 'physical object, earth, hard'},
    'LIGHT': {'syllable': 'lu', 'key': 'n', 'emoji': '☀️', 'meaning': 'brightness, visible, color'},
    'THINK': {'syllable': 'te', 'key': 'u', 'emoji': '💭', 'meaning': 'know, understand, believe'},
}

KEY_MAP      = {v['key']: k      for k, v in PRIMITIVES.items()}
SYLLABLE_MAP = {v['syllable']: k for k, v in PRIMITIVES.items()}

# Common English words that map directly to primitives (for voice input)
WORD_MAP = {
    'i': 'SELF', 'me': 'SELF', 'my': 'SELF',
    'you': 'OTHER', 'they': 'OTHER', 'it': 'OTHER', 'he': 'OTHER', 'she': 'OTHER',
    'no': 'NOT', 'not': 'NOT', 'never': 'NOT',
    'want': 'WANT', 'need': 'WANT', 'wish': 'WANT',
    'good': 'GOOD', 'yes': 'GOOD', 'ok': 'GOOD', 'okay': 'GOOD', 'right': 'GOOD',
    'bad': 'BAD', 'wrong': 'BAD', 'danger': 'BAD',
    'now': 'NOW', 'today': 'NOW', 'soon': 'NOW',
    'here': 'HERE', 'place': 'HERE', 'where': 'HERE',
    'alive': 'ALIVE', 'live': 'ALIVE', 'life': 'ALIVE',
    'go': 'MOVE', 'move': 'MOVE', 'come': 'MOVE',
    'water': 'WATER', 'drink': 'WATER', 'wet': 'WATER',
    'air': 'AIR', 'wind': 'AIR', 'breath': 'AIR', 'sky': 'AIR',
    'heat': 'HEAT', 'hot': 'HEAT', 'fire': 'HEAT', 'warm': 'HEAT',
    'solid': 'SOLID', 'rock': 'SOLID', 'hard': 'SOLID', 'earth': 'SOLID',
    'light': 'LIGHT', 'bright': 'LIGHT', 'dark': 'LIGHT', 'see': 'LIGHT',
    'think': 'THINK', 'know': 'THINK', 'believe': 'THINK', 'understand': 'THINK',
}

# Learner model: tracks which primitives are acquired
DEFAULT_LEARNER = {p: {'acquired': False, 'exposure': 0, 'correct': 0, 'attempts': 0}
                   for p in PRIMITIVES}
