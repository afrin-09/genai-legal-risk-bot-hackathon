from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime


def generate_pdf_summary(filename, summary_data):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Contract Risk Assessment Summary")
    y -= 30

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    y -= 30

    for key, value in summary_data.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 20

    c.showPage()
    c.save()
