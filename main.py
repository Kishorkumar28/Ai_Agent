from agents.classifier_agent import classify_input
from agents.json_agent import process_json
from agents.email_agent import process_email
from agents.pdf_agent import process_pdf
from memory.memory_store import log_to_memory

import sys
import uuid
import os

def main(file_path):
    classification = classify_input(file_path)
    print(f"Intent detected by LLaMA: {classification['intent']}")

    thread_id = str(uuid.uuid4())

    if classification['format'] == 'JSON':
        result = process_json(classification['content'])
    elif classification['format'] == 'Email':
        result = process_email(classification['content'])
    elif classification['format'] == 'PDF':
        result = process_pdf(file_path)  # PDF processed from file path
    else:
        result = {'type': classification['format'], 'message': 'No agent implemented yet'}

    log_to_memory(thread_id, {
        'source': file_path,
        'format': classification['format'],
        'intent': classification['intent'],
        'result': result
    })

    print(f"Processed {file_path} | Thread ID: {thread_id}")
    print(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"File does not exist: {file_path}")
        sys.exit(1)

    main(file_path)

