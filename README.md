# ⚙️ AYU – Medical Assistant Backend (FastAPI)

This backend powers **AYU**, a smart healthcare assistant that analyzes medical reports, retrieves health info, supports multilingual queries, and manages appointment booking.

---

## 🚀 Features
- 🧾 PDF OCR (Tesseract + Poppler)
- 💬 Medical report summarization using **HuggingFace Transformers**
- 🌐 Wikipedia-based health information API
- 📅 Appointment scheduling with SQLite
- 🌎 Multilingual support via Google Translator
- 🗣️ Voice to text using **SpeechRecognition**

---

## 🧠 Tech Stack
- **FastAPI**  
- **Python 3.13**  
- **SQLite**  
- **HuggingFace Transformers**  
- **Tesseract OCR**  
- **Wikipedia API**  
- **Googletrans**

---

## ▶️ How to Run Locally
```bash
# 1. Clone repo
git clone https://github.com/rupaashi/AYU-Backend.git](https://github.com/rupaashi/Ayu-Medical-Assist/blob/backend/
cd AYU-Backend

# 2. Activate virtual environment
.\.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run FastAPI
uvicorn app:app --reload
