import fitz

doc = fitz.open("input_samples/sample_invoice.pdf")  # Put your actual pdf path here

print(f"Number of pages: {doc.page_count}")
doc.close()
