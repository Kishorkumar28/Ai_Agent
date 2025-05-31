import fitz  # PyMuPDF
import re
from agents.classifier_agent import detect_intent_with_llama  # Import LLaMA-based intent detection

def process_pdf(file_path):
    try:
        doc = fitz.open(file_path)
    except Exception as e:
        return {"error": f"Failed to open PDF: {e}"}
    
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

   
    intent = detect_intent_with_llama(text)


    invoice_number = None
    invoice_match = re.search(r"Invoice Number[:\s]*([A-Za-z0-9-]+)", text, re.IGNORECASE)
    if invoice_match:
        invoice_number = invoice_match.group(1)

    return {
        "type": "PDF",
        "intent": intent,
        "extracted_text_snippet": text[:500],  # Preview only
        "invoice_number": invoice_number
    }
