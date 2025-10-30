from report_reader import extract_text_from_pdf
from report_analyzer import analyze_report_text

def process_medical_report(file_path):
    """
    Full pipeline:
    1. Extract text from the uploaded medical report PDF
    2. Summarize & interpret that text
    3. Return clean output
    """
    print("🔍 Reading the medical report...")
    text = extract_text_from_pdf(file_path)

    if text.startswith("Error"):
        return f"❌ Could not process report: {text}"

    print("🧠 Analyzing report content...")
    analysis = analyze_report_text(text)

    return analysis


if __name__ == "__main__":
    # ✅ TEST with your own sample PDF path here
    test_pdf_path = r"C:\Users\Rajneesh Jain\Documents\rupashi\voice assistant backend\report.pdf"
    result = process_medical_report(test_pdf_path)
    print("\n✅ Final Output:\n")
    print(result)
