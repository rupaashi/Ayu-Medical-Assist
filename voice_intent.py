import sounddevice as sd
import wavio
import speech_recognition as sr
import pyttsx3
import requests

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    """AYU speaks aloud."""
    print("AYU 🩺:", text)
    engine.say(text)
    engine.runAndWait()

def record_audio(filename="input.wav", duration=5, fs=44100):
    """Record the user's voice."""
    print("🎙️ Speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wavio.write(filename, audio, fs, sampwidth=2)
    print("✅ Recording saved as", filename)
    return filename

def recognize_speech(filename="input.wav"):
    """Convert recorded speech to text."""
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        print("🎧 Recognizing speech...")
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        print("🗣️ You said:", text)
        return text
    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        speak("Network issue while processing.")
        return ""

def get_health_info(query):
    """Call FastAPI /health_info endpoint to get response."""
    try:
        url = f"http://127.0.0.1:8000/health_info?query={query}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            if "error" in data:
                return "Sorry, I couldn’t fetch that information."
            return data.get("info", "No detailed info found.")
        else:
            return "The server didn’t respond properly."
    except Exception as e:
        return f"Error connecting to backend: {str(e)}"

if __name__ == "__main__":
    audio_file = record_audio(duration=5)
    user_text = recognize_speech(audio_file)

    if user_text:
        speak("Got it! Let me check that for you...")
        response = get_health_info(user_text)
        speak(response)
