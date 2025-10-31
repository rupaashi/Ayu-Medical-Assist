import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Load your recorded file
with sr.AudioFile("output.wav") as source:
    audio = r.record(source)  # Read the entire audio file

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError:
    print("Speech recognition service is unavailable.")
