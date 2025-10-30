import sounddevice as sd
import numpy as np
import wavio

duration = 3  # seconds
fs = 44100    # sample rate (Hz)

print("🎙️ Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()
wavio.write("output.wav", audio, fs, sampwidth=2)
print("✅ Saved as output.wav")

