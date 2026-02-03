# GenAI-Powered Contract Risk Assessment Assistant

## Hackathon
Career Carnival Hackathon 2026 – Data Science

---

## Problem Statement
Small and medium businesses often sign contracts without fully understanding complex legal clauses, exposing them to financial and operational risks. This project builds a **GenAI-powered legal assistant** that analyzes contracts, identifies risky clauses, and explains them in simple business-friendly language.

---

## Solution Overview
This application allows users to upload contracts (PDF / DOCX / TXT) and automatically:
- Extract contract text
- Split the contract into clauses
- Identify potentially risky clauses
- Assign clause-level risk scores (Low / Medium / High)
- Explain risky clauses in plain language using GenAI
- Provide an overall contract risk summary

The goal is **clarity, not legal advice**, enabling SMEs to make informed decisions before consulting a lawyer.

---

## Key Features

### 📄 Contract Processing
- Supports PDF, DOCX, and TXT formats
- Clean text extraction using Python utilities

### 📌 Clause Detection
- Automatically splits contracts into logical clauses
- Classifies clauses (Termination, Confidentiality, Payment, etc.)

### ⚠️ Risk Assessment
- Clause-level risk scoring:
  - 🟢 Low
  - 🟠 Medium
  - 🔴 High
- Detects unfavorable patterns such as unilateral termination, indemnity, penalties, and non-compete clauses

### 🧠 GenAI Explanation
- Uses an OpenAI GPT-based language model
- Explains risky clauses in **simple, non-legal language**
- Designed for small business owners

> Note: Due to API quota limitations, live LLM responses may be demonstrated using representative outputs. The architecture fully supports real-time GenAI integration.

### 📊 Contract Summary
- Total clauses detected
- Count of high and medium risk clauses
- Overall contract risk level

---

## Tech Stack

- **Language:** Python 3.10
- **UI:** Streamlit
- **NLP (Lightweight):** Regex-based clause extraction
- **GenAI:** OpenAI GPT (via API)
- **Document Parsing:** pdfplumber, python-docx
- **Configuration:** python-dotenv

---

## Architecture (High-Level)

1. User uploads contract
2. Text extracted from document
3. Contract split into clauses
4. Risk engine evaluates each clause
5. GenAI explains risky clauses
6. UI displays results and summary

---

## Limitations

- This is a prototype and does not provide legal advice
- Indian law compliance is rule-based and illustrative
- Live GenAI output depends on API availability

---

## Future Enhancements

- Multilingual contract support (Hindi + English)
- Clause similarity matching with standard templates
- PDF export of analysis report
- Audit logs and contract history
- Enhanced compliance checks

---

## How to Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py

