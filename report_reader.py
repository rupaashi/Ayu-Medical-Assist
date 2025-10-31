import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# ✅ Poppler absolute path (your exact one)
poppler_path = r"C:\Users\Rajneesh Jain\Downloads\poppler-25.07.0\Library\bin"


# ✅ Path to installed Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(file_path):
    """
    Reads text from a PDF medical report using OCR.
    Returns extracted text as a string.
    """
    try:
        # Explicitly give poppler_path to avoid PATH issues
        pages = convert_from_path(file_path, dpi=300, poppler_path=poppler_path)
        full_text = ""
        for page in pages:
            text = pytesseract.image_to_string(page)
            full_text += text + "\n"
        return full_text.strip()
    except Exception as e:
        return f"Error reading PDF: {str(e)}"


if __name__ == "__main__":
    # ✅ Your test PDF (make sure report.pdf exists in this folder)
    file_path = r"C:\Users\Rajneesh Jain\Documents\rupashi\voice assistant backend\report.pdf"
    text = extract_text_from_pdf(file_path)
    print("\nExtracted Text:\n")
    print(text)