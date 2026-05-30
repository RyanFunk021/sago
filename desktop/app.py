import streamlit as st
import subprocess
import random
import sys
import os
import matplotlib
matplotlib.use('Agg')

sys.path.insert(0, os.path.dirname(__file__))

from primitives import PRIMITIVES, KEY_MAP
from audio import speak, speak_syllable, speak_sequence, record_audio
from learner import (load_model, save_model, record_attempt, acquired_primitives,
                     next_to_teach, filter_to_known, acquisition_summary, current_tier)
from vizualize import load_wav, make_figure, peak_amplitude

st.set_page_config(page_title='PrimaTap', page_icon='👤', layout='wide')

# ── session state ──────────────────────────────────────────────────────────────
if 'learner' not in st.session_state:
    st.session_state.learner = load_model()
if 'sequence' not in st.session_state:
    st.session_state.sequence = []
if 'quiz_target' not in st.session_state:
    st.session_state.quiz_target = None
if 'quiz_result' not in st.session_state:
    st.session_state.quiz_result = None
if 'history' not in st.session_state:
    st.session_state.history = []

model = st.session_state.learner

# ── header ─────────────────────────────────────────────────────────────────────
st.title('PrimaTap')
st.caption(acquisition_summary(model))

tab_learn, tab_speak, tab_type = st.tabs(['📚 Learn', '🎙️ Speak', '⌨️ Type'])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — LEARN
# ══════════════════════════════════════════════════════════════════════════════
with tab_learn:

    mode = st.radio('Mode', ['Explore', 'Quiz'], horizontal=True)

    # ── Explore: click any card to hear it ────────────────────────────────────
    if mode == 'Explore':
        st.markdown('#### Click a primitive to hear it')
        cols = st.columns(4)
        for idx, (name, data) in enumerate(PRIMITIVES.items()):
            with cols[idx % 4]:
                acquired = model[name]['acquired']
                teaching = (name == next_to_teach(model))
                border = '3px solid #4CAF50' if acquired else ('3px solid #FF9800' if teaching else '1px solid #555')
                label = f"{data['emoji']}  **{name}**  \n`{data['syllable']}`  \n*{data['meaning']}*"
                if st.button(label, key=f'learn_{name}', use_container_width=True):
                    speak_syllable(name)
                    model[name]['exposure'] += 1
                    save_model(model)
                    st.toast(f"{data['syllable']} — {data['meaning']}")

        st.divider()
        st.markdown('**Keyboard layout**')
        st.code(
            "  —   HEAT  ALIVE  MOVE   —    —   THINK  WATER   AIR    —\n"
            "  —   GOOD  OTHER  SELF  NOW  HERE   NOT   WANT   BAD    —\n"
            "  —    —     —    SOLID   —   LIGHT   —     —      —     —\n"
            "                        [  S P A C E  ]",
            language=None
        )

    # ── Quiz: hear syllable, pick the primitive ───────────────────────────────
    elif mode == 'Quiz':
        tier = current_tier(model)
        quiz_pool = acquired_primitives(model) + ([next_to_teach(model)] if next_to_teach(model) else [])

        if len(quiz_pool) < 2:
            st.info('Start in Explore mode and click a few primitives first to build your quiz pool.')
        else:
            if st.button('🔊 Play syllable', use_container_width=True) or st.session_state.quiz_target is None:
                st.session_state.quiz_target = random.choice(quiz_pool)
                st.session_state.quiz_result = None
                speak_syllable(st.session_state.quiz_target)

            target = st.session_state.quiz_target
            st.markdown(f'**Which primitive was that?**')

            cols = st.columns(4)
            for idx, name in enumerate(quiz_pool):
                with cols[idx % 4]:
                    data = PRIMITIVES[name]
                    if st.button(f"{data['emoji']} {name}", key=f'quiz_{name}', use_container_width=True):
                        correct = (name == target)
                        st.session_state.learner = record_attempt(model, target, correct)
                        st.session_state.quiz_result = ('✅ Correct!' if correct else
                                                         f'❌ That was **{target}** ({PRIMITIVES[target]["syllable"]})')
                        if correct:
                            speak('good', wait=False)
                        else:
                            speak_syllable(target, wait=False)

            if st.session_state.quiz_result:
                st.markdown(f'### {st.session_state.quiz_result}')

            # Progress bars
            st.divider()
            st.markdown('**Acquisition progress**')
            for name, data in model.items():
                if data['attempts'] > 0:
                    rate = data['correct'] / data['attempts']
                    st.progress(rate, text=f"{PRIMITIVES[name]['emoji']} {name}  ({data['correct']}/{data['attempts']})")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — SPEAK
# ══════════════════════════════════════════════════════════════════════════════
with tab_speak:

    # ── Reference syllables ───────────────────────────────────────────────────
    st.markdown('#### 🔊 Hear a syllable first — then try to match it')
    ref_cols = st.columns(8)
    for idx, (name, data) in enumerate(PRIMITIVES.items()):
        with ref_cols[idx % 8]:
            if st.button(f"{data['emoji']}\n**{data['syllable']}**",
                         key=f'ref_{name}',
                         use_container_width=True,
                         help=f"{name} — {data['meaning']}"):
                speak_syllable(name, wait=False)
                st.toast(f"{name}: say \"{data['syllable']}\"")

    st.divider()

    # ── Record ────────────────────────────────────────────────────────────────
    st.markdown('#### 🎙️ Now speak')
    st.caption('Say syllables like **sa to na wu** — or just say the English word')

    col_rec, col_sec = st.columns([3, 1])
    with col_sec:
        seconds = st.slider('Seconds', 2, 6, 3, label_visibility='collapsed')
        st.caption(f'{seconds}s recording')
    with col_rec:
        record_btn = st.button('🎙️  Record now', use_container_width=True, type='primary')

    if record_btn:
        progress = st.progress(0, text=f'Recording for {seconds} seconds — speak now...')
        import time
        audio_path = record_audio(seconds=seconds)
        progress.progress(100, text='Processing...')

        # Load audio and show waveform immediately
        audio, rate = load_wav(audio_path)
        amp = peak_amplitude(audio)

        if amp < 0.01:
            st.error('⚠️ No audio captured. Check System Preferences → Privacy → Microphone and allow Terminal/your browser.')
        else:
            # Show waveform + spectrogram + pitch
            with st.spinner('Analyzing audio...'):
                try:
                    from recognizer import transcribe_and_parse
                    text, primitives_found = transcribe_and_parse(audio_path)
                    fig = make_figure(audio, rate, recognized=text)
                    st.pyplot(fig, use_container_width=True)

                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown('**Whisper heard:**')
                        st.info(f'"{text}"' if text.strip() else '(silence)')
                    with col2:
                        st.markdown('**Primitives:**')
                        if primitives_found:
                            display = '  →  '.join(
                                f"{PRIMITIVES[p]['emoji']} **{p}**" for p in primitives_found
                            )
                            st.success(display)
                            speak_sequence(primitives_found)
                            st.session_state.history.append({
                                'heard': text, 'primitives': primitives_found
                            })
                        else:
                            st.warning('No primitives matched. Try speaking more slowly and clearly.')
                            st.caption('Tips: short crisp syllables, one at a time, pause between them')

                    # Teach next primitive
                    teaching = next_to_teach(model)
                    if teaching:
                        t = PRIMITIVES[teaching]
                        st.divider()
                        st.markdown(f"**Now learning:** {t['emoji']} **{teaching}** = say `{t['syllable']}` — *{t['meaning']}*")
                        if st.button(f"🔊 Hear {t['syllable']} again", key='teach_again'):
                            speak_syllable(teaching, wait=False)

                except Exception as e:
                    # Still show the waveform even if recognition fails
                    fig = make_figure(audio, rate)
                    st.pyplot(fig, use_container_width=True)
                    st.error(f'Recognition error: {e}')
                    st.caption('The waveform above shows your audio was captured. Recognition failed — check the error.')

        os.unlink(audio_path)

    # ── History ───────────────────────────────────────────────────────────────
    if st.session_state.history:
        st.divider()
        st.markdown('**Session history**')
        for item in reversed(st.session_state.history[-8:]):
            prim_str = '  →  '.join(
                f"{PRIMITIVES[p]['emoji']} {p}" for p in item['primitives']
            ) or '—'
            st.markdown(f'`{item["heard"]}` → {prim_str}')

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — TYPE
# ══════════════════════════════════════════════════════════════════════════════
with tab_type:
    st.markdown('Type using your 16-key layout. Each key maps to a primitive.')
    st.markdown('**Keys:** `s d f g h j k l` (home) · `w e r u i o` (top) · `v n` (bottom) · `space` = send')

    st.code(
        "  [W]   [E]   [R]        [U]   [I]   [O]\n"
        " HEAT  ALIVE MOVE       THINK WATER  AIR\n"
        "  fu    li    mo          te    du    re\n\n"
        "  [S]   [D]   [F]  [G][H] [J]   [K]   [L]\n"
        " GOOD  OTHER SELF  NOW HERE NOT  WANT  BAD\n"
        "  go    to    sa   ne  hi   na    wu    bi\n\n"
        "        [V]              [N]\n"
        "       SOLID            LIGHT\n"
        "        ko               lu",
        language=None
    )

    raw = st.text_input(
        'Type your chord sequence here (then press Enter to send)',
        placeholder='e.g. fsdk → SELF GOOD OTHER WANT',
        key='type_input'
    )

    if raw:
        decoded = []
        unknown = []
        for ch in raw.lower():
            if ch == ' ':
                continue
            if ch in KEY_MAP:
                decoded.append(KEY_MAP[ch])
            elif ch not in ('\n', '\r'):
                unknown.append(ch)

        if decoded:
            st.markdown('**Sequence:**')
            display = '  →  '.join(f"{PRIMITIVES[p]['emoji']} **{p}**  `{PRIMITIVES[p]['syllable']}`"
                                   for p in decoded)
            st.success(display)

            col1, col2 = st.columns(2)
            with col1:
                if st.button('🔊 Speak sequence', use_container_width=True):
                    speak_sequence(decoded)
            with col2:
                if st.button('🔊 Speak meanings', use_container_width=True):
                    from audio import speak_meaning
                    speak_meaning(decoded)

        if unknown:
            st.caption(f"Unmapped keys ignored: {', '.join(unknown)}")

    st.divider()
    st.markdown('**Quick reference**')
    ref_cols = st.columns(4)
    for idx, (name, data) in enumerate(PRIMITIVES.items()):
        with ref_cols[idx % 4]:
            st.markdown(f"`{data['key'].upper()}` → {data['emoji']} {name} · *{data['syllable']}*")
