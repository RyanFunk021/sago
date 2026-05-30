import whisper
import difflib
from primitives import PRIMITIVES, SYLLABLE_MAP, WORD_MAP

_model = None

# Whisper tends to map our invented syllables to the nearest English word.
# This table catches the most common mistranscriptions.
WHISPER_CORRECTIONS = {
    # SELF (sa)
    'saw': 'SELF', 'sah': 'SELF', 'suh': 'SELF', 'sa': 'SELF',
    # OTHER (to)
    'to': 'OTHER', 'too': 'OTHER', 'two': 'OTHER', 'toe': 'OTHER',
    # NOT (na)
    'nah': 'NOT', 'na': 'NOT', 'nuh': 'NOT', 'naw': 'NOT',
    # WANT (wu)
    'woo': 'WANT', 'wu': 'WANT', 'who': 'WANT', 'ooh': 'WANT', 'whoo': 'WANT',
    # GOOD (go)
    'go': 'GOOD', 'goh': 'GOOD',
    # BAD (bi)
    'be': 'BAD', 'bee': 'BAD', 'bi': 'BAD', 'by': 'BAD', 'bye': 'BAD',
    # NOW (ne)
    'nay': 'NOW', 'ne': 'NOW', 'neh': 'NOW', 'knee': 'NOW', 'ney': 'NOW',
    # HERE (hi)
    'hi': 'HERE', 'hey': 'HERE', 'hay': 'HERE',
    # ALIVE (li)
    'lee': 'ALIVE', 'lea': 'ALIVE', 'li': 'ALIVE', 'lie': 'ALIVE',
    # MOVE (mo)
    'mo': 'MOVE', 'mow': 'MOVE', 'moe': 'MOVE',
    # WATER (du)
    'do': 'WATER', 'doo': 'WATER', 'du': 'WATER', 'due': 'WATER', 'dew': 'WATER',
    # AIR (re)
    'ray': 'AIR', 're': 'AIR', 'reh': 'AIR', 'rae': 'AIR', 'raye': 'AIR',
    # HEAT (fu)
    'foo': 'HEAT', 'fu': 'HEAT', 'phoo': 'HEAT', 'few': 'HEAT',
    # SOLID (ko)
    'co': 'SOLID', 'ko': 'SOLID', 'coe': 'SOLID', 'koh': 'SOLID', 'coh': 'SOLID',
    # LIGHT (lu)
    'lu': 'LIGHT', 'lou': 'LIGHT', 'luke': 'LIGHT', 'loo': 'LIGHT', 'lew': 'LIGHT',
    # THINK (te)
    'teh': 'THINK', 'te': 'THINK', 'tay': 'THINK', 'the': 'THINK', 'ta': 'THINK',
}

# Whisper prompt biases the model toward our syllable sounds
WHISPER_PROMPT = (
    "The speaker is saying short invented syllables from this list: "
    "sa, to, na, wu, go, bi, ne, hi, li, mo, du, re, fu, ko, lu, te. "
    "Transcribe exactly what is said."
)

def get_model():
    global _model
    if _model is None:
        _model = whisper.load_model('tiny')
    return _model

def transcribe(audio_path):
    model = get_model()
    result = model.transcribe(
        audio_path,
        language='en',
        fp16=False,
        initial_prompt=WHISPER_PROMPT
    )
    return result['text'].strip().lower()

def match_token(token):
    """Match a single token to a primitive."""
    token = token.strip().strip('.,!?\'"').lower()

    if not token:
        return None

    # 1. Direct Whisper correction table
    if token in WHISPER_CORRECTIONS:
        return WHISPER_CORRECTIONS[token]

    # 2. Direct syllable match
    if token in SYLLABLE_MAP:
        return SYLLABLE_MAP[token]

    # 3. English word match
    if token in WORD_MAP:
        return WORD_MAP[token]

    # 4. Fuzzy match against all known mappings
    all_known = list(WHISPER_CORRECTIONS.keys()) + list(SYLLABLE_MAP.keys()) + list(WORD_MAP.keys())
    close = difflib.get_close_matches(token, all_known, n=1, cutoff=0.75)
    if close:
        hit = close[0]
        if hit in WHISPER_CORRECTIONS:
            return WHISPER_CORRECTIONS[hit]
        if hit in SYLLABLE_MAP:
            return SYLLABLE_MAP[hit]
        if hit in WORD_MAP:
            return WORD_MAP[hit]

    return None

def parse_utterance(text):
    tokens = text.lower().split()
    return [m for m in (match_token(t) for t in tokens) if m]

def transcribe_and_parse(audio_path):
    text = transcribe(audio_path)
    primitives = parse_utterance(text)
    return text, primitives
