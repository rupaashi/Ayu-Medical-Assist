from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline
import pytesseract
from PIL import Image
import wikipediaapi
import sqlite3
from datetime import datetime
from deep_translator import GoogleTranslator
import io

# ---------------------------- SETUP ----------------------------
app = FastAPI(title="AYU - Intelligent Health Assistant")

# Enable CORS (important for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load summarization model once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ---------------------------- DATABASE ----------------------------
def init_db():
    conn = sqlite3.connect("appointments.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            doctor TEXT,
            date TEXT,
            time TEXT,
            reason TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------------------------- MODELS ----------------------------
class Appointment(BaseModel):
    name: str
    doctor: str
    date: str
    time: str
    reason: str

# ---------------------------- OCR ENDPOINT ----------------------------
@app.post("/extract_text")
async def extract_text_from_image(file: UploadFile = File(...)):
    """
    Extracts text from uploaded medical report image.
    """
    try:
        image = Image.open(io.BytesIO(await file.read()))
        text = pytesseract.image_to_string(image)
        if not text.strip():
            raise HTTPException(status_code=400, detail="No readable text found in image.")
        return {"extracted_text": text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading image: {e}")

# ---------------------------- REPORT ANALYZER ----------------------------
@app.post("/analyze_report")
async def analyze_report(report_text: str = Form(...)):
    """
    Summarizes and interprets a given medical report text.
    """
    try:
        if not report_text.strip():
            raise HTTPException(status_code=400, detail="Empty report text.")

        # Chunk text if long
        max_chunk = 1000
        chunks = [report_text[i:i+max_chunk] for i in range(0, len(report_text), max_chunk)]
        summary = ""

        for chunk in chunks:
            part = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
            summary += part[0]["summary_text"] + " "

        # Basic interpretation
        interpretation = ""
        text_lower = report_text.lower()
        if "hemoglobin" in text_lower:
            interpretation += "Hemoglobin mentioned — low levels may indicate anemia.\n"
        if "glucose" in text_lower or "sugar" in text_lower:
            interpretation += "Glucose levels noted — ensure within 70–140 mg/dL.\n"
        if "cholesterol" in text_lower:
            interpretation += "Cholesterol mentioned — values above 200 mg/dL may be high.\n"

        final_output = f"🩺 Summary:\n{summary.strip()}\n\n💡 Interpretation:\n{interpretation or 'No key indicators detected.'}"
        return {"result": final_output}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing report: {str(e)}")

# ---------------------------- APPOINTMENT SCHEDULING ----------------------------
@app.post("/appointments")
def book_appointment(appointment: Appointment):
    """
    Saves an appointment to SQLite database.
    """
    try:
        conn = sqlite3.connect("appointments.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO appointments (name, doctor, date, time, reason)
            VALUES (?, ?, ?, ?, ?)
        """, (appointment.name, appointment.doctor, appointment.date, appointment.time, appointment.reason))
        conn.commit()
        conn.close()
        return {"message": "Appointment booked successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/appointments")
def get_appointments():
    """
    Returns all appointments from database.
    """
    try:
        conn = sqlite3.connect("appointments.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointments")
        rows = cursor.fetchall()
        conn.close()
        return {"appointments": rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ---------------------------- HEALTH INFORMATION (Wikipedia Fixed) ----------------------------
@app.get("/health_info")
def get_health_info(query: str):
    """
    Fetches health info using Wikipedia (safe method).
    """
    try:
        wiki = wikipediaapi.Wikipedia(
            language='en',
            user_agent='AYU Health Assistant/1.0 (contact: ayu-support@example.com)'
        )
        page = wiki.page(query)
        if page.exists():
            return {"info": page.summary[:600]}
        else:
            raise HTTPException(status_code=404, detail="No information found on this topic.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")

# ---------------------------- MULTILINGUAL SUPPORT ----------------------------
@app.post("/translate")
def translate_text(text: str = Form(...), target_lang: str = Form("en")):
    """
    Translates text to and from English for multilingual conversations.
    """
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return {"translated_text": translated}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {e}")

# ---------------------------- ROOT ----------------------------
@app.get("/")
def home():
    return {"message": "Welcome to AYU - Intelligent Health Assistant 💬"}

# ---------------------------- RUN ----------------------------
# Run using: uvicorn app:app --reload




import os
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
