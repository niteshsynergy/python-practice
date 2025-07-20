import fitz  # PyMuPDF (for reading PDF)
from reportlab.pdfgen import canvas  # For generating new PDF
import os
import datetime

# Define the input PDF file path
input_file = r"C:\Users\Rahul Kumar\Desktop\testpdf.pdf"

# Generate a new filename with current date & time (format: HH.MM.SS.DD.MM.YY)
current_time = datetime.datetime.now().strftime("%H.%M.%S.%d.%m.%y")
output_file = os.path.join(os.path.dirname(input_file), f"testpdf_{current_time}.pdf")

try:
    # Step 1: Read the PDF content
    with fitz.open(input_file) as pdf_file:
        text = ""
        for page_num, page in enumerate(pdf_file, start=1):
            text += f"\n📄 Page {page_num}:\n"
            text += page.get_text("text")  # Extract text from each page

    # Step 2: Convert text into a new PDF
    c = canvas.Canvas(output_file)
    c.setFont("Helvetica", 12)

    # Add text to new PDF (handling line breaks)
    line_height = 800  # Start writing from near top
    for line in text.split("\n"):
        c.drawString(50, line_height, line)
        line_height -= 20  # Move to next line

        if line_height < 50:  # If the page is filled, create a new page
            c.showPage()
            c.setFont("Helvetica", 12)
            line_height = 800  # Reset line height

    c.save()  # Save the new PDF

    print(f"✅ New PDF saved as: {output_file}")

except FileNotFoundError:
    print(f"Error: File not found at {input_file}")
except Exception as e:
    print(f"An error occurred: {e}")
