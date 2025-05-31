import sys
from PyPDF2 import PdfReader

file_path = sys.argv[1]

try:
    reader = PdfReader(file_path)
    print(f"PDF has {len(reader.pages)} pages")
except Exception as e:
    print(f"Failed to open PDF: {e}")
