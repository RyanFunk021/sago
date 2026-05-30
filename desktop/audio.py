import subprocess
import tempfile
import wave
import pyaudio
from primitives import PRIMITIVES

VOICE = 'Samantha'
RATE = 180  # words per minute for say command

def speak(text, wait=False):
    cmd = ['say', '-v', VOICE, '-r', str(RATE), text]
    if wait:
        subprocess.run(cmd)
    else:
        subprocess.Popen(cmd)

def speak_syllable(primitive_name, wait=False):
    syllable = PRIMITIVES[primitive_name]['syllable']
    speak(syllable, wait=wait)

def speak_sequence(sequence, wait=False):
    syllables = '  '.join(PRIMITIVES[p]['syllable'] for p in sequence if p in PRIMITIVES)
    if syllables:
        speak(syllables, wait=wait)

def speak_meaning(sequence):
    meanings = ', '.join(PRIMITIVES[p]['meaning'].split(',')[0] for p in sequence if p in PRIMITIVES)
    speak(meanings, wait=False)

def record_audio(seconds=3, sample_rate=16000):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1,
                    rate=sample_rate, input=True,
                    frames_per_buffer=1024)
    frames = []
    for _ in range(0, int(sample_rate / 1024 * seconds)):
        frames.append(stream.read(1024))
    stream.stop_stream()
    stream.close()
    p.terminate()

    tmp = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
    with wave.open(tmp.name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))
    return tmp.name
