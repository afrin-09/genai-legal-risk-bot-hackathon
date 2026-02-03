import pdfplumber
from docx import Document


def extract_text(file, file_type):
    text = ""

    if file_type == "pdf":
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    elif file_type == "docx":
        doc = Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    elif file_type == "txt":
        text = file.read().decode("utf-8")

    return text.strip()
