# 🧠 Multi-Agent AI System — Flowbit AI Task

This project is a multi-agent AI pipeline that can classify, route, and process documents in various formats (PDF, JSON, Email). It uses a central **Classifier Agent** backed by **LLaMA 3.3 70B** via the Together API to identify document format and intent. Each file is routed to a specialized agent for further extraction and processing. The system also logs everything into shared memory for traceability and debugging.

---

## ✅ Objectives Achieved

- Detect document **format** and **intent** (Invoice, RFQ, Complaint, etc.)
- Route documents to appropriate agents:
  - **JSON Agent**
  - **Email Agent**
  - **PDF Agent**
- Extract structured information
- Maintain lightweight shared memory for logging
- Modular design, easy to extend

---

## 🧩 Agents Overview

### 1. Classifier Agent
- Classifies file type: `PDF`, `JSON`, `Email`
- Determines document intent using **LLaMA 3.3 70B Instruct Turbo**
- Routes to the appropriate agent
- Logs to memory with a unique thread ID

### 2. JSON Agent
- Accepts structured JSON
- Reformats to a standard schema
- Flags missing/invalid fields

### 3. Email Agent
- Accepts raw `.txt` or `.eml`
- Extracts:
  - Sender
  - Intent
  - Urgency level (based on keywords)

### 4. PDF Agent
- Extracts key fields like `invoice number` from PDF content
- Handles OCR-ready text-based PDFs

---

## 🧠 Memory Logging

All processed threads are logged with:
- Source file
- Detected format + intent
- Extracted values
- Unique thread ID

Memory is in-memory for simplicity (can easily swap for Redis or SQLite).

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **LLaMA 3.3 70B via Together API** (`together-ai`)
- **PyPDF2** for PDF parsing
- **dotenv** for config management

---

## 🧪 Sample Inputs

Found in the `/input_samples` directory:
- `sample_invoice.pdf`
- `sample_rfq.json`
- `sample_email.txt`

Each triggers a different flow through the system.

---

## 🚀 Running the System

### 1. Install requirements
```bash
pip install -r requirements.txt
