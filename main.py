from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Voice Assistant Backend is running!"}





from fastapi import FastAPI, UploadFile, File
import speech_recognition as sr
import shutil

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Voice Assistant Backend Running 🚀"}

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Save uploaded audio
    temp_filename = "temp_audio.wav"
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Speech recognition
    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_filename) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return {"transcribed_text": text}
        except sr.UnknownValueError:
            return {"error": "Could not understand audio"}
        except sr.RequestError as e:
            return {"error": f"Speech recognition service error: {e}"}
