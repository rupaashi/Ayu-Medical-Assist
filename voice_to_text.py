import speech_recognition as sr
import sounddevice as sd
import wavio

def record_voice(duration=5, filename="user_input.wav", samplerate=44100):
    print("🎙️ Recording... Speak now!")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()
    wavio.write(filename, audio, samplerate, sampwidth=2)
    print("✅ Recording complete!")

def recognize_speech(filename="user_input.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        print("🧠 Recognizing speech...")
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"💬 You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"⚠️ Error with speech recognition service: {e}")
        return None

if __name__ == "__main__":
    record_voice(duration=5)
    recognize_speech()
