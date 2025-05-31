import os
import json
from dotenv import load_dotenv
from together import Together

load_dotenv()

# Initialize Together client (reads TOGETHER_API_KEY from env automatically)
client = Together()

# Use the free LLaMA 3.3 70B instruct turbo model from Together
LLAMA_MODEL = "meta-llama/llama-3.3-70b-instruct-turbo-free"

def detect_intent_with_llama(text):
    prompt = f"""You are an AI agent that classifies the intent of a given document. Only respond with one of the following: Invoice, RFQ, Complaint, Regulation, or Unknown.

Document:
{text[:1000]}  # Limit to first 1000 characters to save tokens

Intent:"""

    try:
        response = client.chat.completions.create(
            model=LLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_tokens=10,
        )
        intent = response.choices[0].message.content.strip()
        if intent in ['Invoice', 'RFQ', 'Complaint', 'Regulation']:
            return intent
        else:
            return 'Unknown'
    except Exception as e:
        print(f"LLAMA intent detection failed: {e}")
        return "Unknown"

def classify_input(file_path):
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    format = "Unknown"
    content = ""

    if ext == ".json":
        format = "JSON"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    elif ext == ".txt" or ext == ".eml":
        format = "Email"
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    elif ext == ".pdf":
        format = "PDF"
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(file_path)
            content = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        except Exception as e:
            print(f"Error reading PDF for LLaMA: {e}")
            content = ""
    else:
        format = "Unknown"

    # Run LLaMA on all formats including PDF
    intent = detect_intent_with_llama(content)

    return {
        "format": format,
        "intent": intent,
        "content": content
    }
