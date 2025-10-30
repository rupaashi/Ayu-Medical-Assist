from transformers import pipeline

# ✅ Faster summarizer model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def analyze_report_text(report_text):
    """
    Summarizes and interprets the medical report text.
    Input: raw text from OCR
    Output: summarized + interpreted text
    """
    if not report_text or len(report_text.strip()) == 0:
        return "No text found in report."

    # Summarize text (handle long reports)
    max_chunk = 1000
    chunks = [report_text[i:i+max_chunk] for i in range(0, len(report_text), max_chunk)]
    summary = ""

    for chunk in chunks:
        part = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summary += part[0]['summary_text'] + " "

    # Keyword-based interpretation
    interpretation = ""
    if "hemoglobin" in report_text.lower():
        interpretation += "It looks like this report mentions hemoglobin. Check if the value is below 12 for women or 13.5 for men — that may indicate anemia.\n"
    if "glucose" in report_text.lower() or "sugar" in report_text.lower():
        interpretation += "Blood sugar levels are noted. Ensure they are within 70–140 mg/dL.\n"
    if "cholesterol" in report_text.lower():
        interpretation += "Cholesterol is mentioned — values above 200 mg/dL are considered high.\n"
    if "vitamin d" in report_text.lower():
        interpretation += "Vitamin D is mentioned. Levels below 30 ng/mL suggest deficiency.\n"
    if "creatinine" in report_text.lower():
        interpretation += "Creatinine levels are noted — normal is 0.6–1.2 mg/dL. Higher may indicate kidney issues.\n"

    final_text = f"🩺 Summary:\n{summary.strip()}\n\n💡 Interpretation:\n{interpretation or 'No specific health indicators detected.'}"
    return final_text


if __name__ == "__main__":
    # Test with a fake report
    sample = "Hemoglobin is 10.2 g/dL, Glucose fasting is 180 mg/dL, Vitamin D level is 20 ng/mL."
    print(analyze_report_text(sample))
