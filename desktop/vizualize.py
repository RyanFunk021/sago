"""Audio visualization — waveform, pitch, and syllable matching."""

import numpy as np
import wave
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import librosa

def load_wav(path):
    with wave.open(path, 'rb') as wf:
        frames = wf.readframes(wf.getnframes())
        rate = wf.getframerate()
    audio = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0
    return audio, rate

def make_figure(audio, rate, recognized=None, target_syllable=None):
    """Return a matplotlib figure showing waveform + spectrogram + pitch."""

    duration = len(audio) / rate
    times = np.linspace(0, duration, len(audio))

    # Pitch (fundamental frequency)
    f0, voiced_flag, _ = librosa.pyin(audio, fmin=80, fmax=500, sr=rate)
    pitch_times = np.linspace(0, duration, len(f0))

    # Spectrogram
    S = librosa.feature.melspectrogram(y=audio, sr=rate, n_mels=64, fmax=4000)
    S_db = librosa.power_to_db(S, ref=np.max)

    fig = plt.figure(figsize=(10, 6), facecolor='#0e1117')
    gs = gridspec.GridSpec(3, 1, figure=fig, hspace=0.5)

    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    ax3 = fig.add_subplot(gs[2])

    for ax in [ax1, ax2, ax3]:
        ax.set_facecolor('#1a1d23')
        ax.tick_params(colors='#aaa')
        ax.spines[:].set_color('#333')

    # ── Waveform ──────────────────────────────────────────────────────────────
    amplitude = np.abs(audio).max()
    color = '#4CAF50' if amplitude > 0.05 else '#FF5252'
    ax1.plot(times, audio, color=color, linewidth=0.5, alpha=0.9)
    ax1.axhline(0, color='#333', linewidth=0.5)
    ax1.set_xlim(0, duration)
    ax1.set_ylim(-1, 1)
    ax1.set_ylabel('Amplitude', color='#aaa', fontsize=9)
    ax1.set_title(
        '🎙️ Audio captured' if amplitude > 0.05 else '⚠️  No sound detected — check microphone',
        color='#4CAF50' if amplitude > 0.05 else '#FF5252',
        fontsize=11, pad=6
    )

    # ── Spectrogram ───────────────────────────────────────────────────────────
    img = ax2.imshow(S_db, aspect='auto', origin='lower',
                     extent=[0, duration, 0, 4000],
                     cmap='magma', vmin=-80, vmax=0)
    ax2.set_ylabel('Frequency (Hz)', color='#aaa', fontsize=9)
    ax2.set_title('Spectrogram', color='#aaa', fontsize=10, pad=4)

    # ── Pitch track ───────────────────────────────────────────────────────────
    voiced = voiced_flag & ~np.isnan(f0)
    if voiced.any():
        ax3.plot(pitch_times[voiced], f0[voiced],
                 'o', color='#FF9800', markersize=3, label='Pitch (F0)')
        mean_pitch = np.nanmean(f0[voiced])
        ax3.axhline(mean_pitch, color='#FF9800', linewidth=1, linestyle='--', alpha=0.5)
        ax3.set_title(f'Pitch — avg {mean_pitch:.0f} Hz  ({note_name(mean_pitch)})',
                      color='#FF9800', fontsize=10, pad=4)
    else:
        ax3.set_title('Pitch — (no voiced sound detected)', color='#888', fontsize=10, pad=4)

    ax3.set_xlim(0, duration)
    ax3.set_ylim(50, 500)
    ax3.set_ylabel('Hz', color='#aaa', fontsize=9)
    ax3.set_xlabel('Time (s)', color='#aaa', fontsize=9)

    # Recognized label
    if recognized:
        fig.text(0.98, 0.98,
                 f'Heard: {recognized}',
                 ha='right', va='top', color='#4CAF50',
                 fontsize=13, fontweight='bold',
                 transform=fig.transFigure)

    plt.tight_layout(pad=1.5)
    return fig

def note_name(freq):
    if freq <= 0:
        return ''
    notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    midi = 12 * np.log2(freq / 440.0) + 69
    note = notes[int(round(midi)) % 12]
    octave = int(round(midi)) // 12 - 1
    return f'{note}{octave}'

def peak_amplitude(audio):
    return float(np.abs(audio).max())
