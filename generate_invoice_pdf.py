from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Invoice Number: INV-12345", ln=True)
pdf.cell(200, 10, txt="This is an invoice document for your recent purchase.", ln=True)

# Save to disk correctly
pdf.output("input_samples/sample_invoice.pdf", "F")
