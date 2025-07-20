import fitz  # PyMuPDF

# Define the file path
file_path = r"C:\Users\Rahul Kumar\Desktop\testpdf.pdf"

try:
    with fitz.open(file_path) as pdf_file:
        text = ""
        for page_num, page in enumerate(pdf_file, start=1):
            text += f"\n📄 Page {page_num}:\n"
            text += page.get_text("text")  # Extract text

    print("📌 PDF Content:\n", text)

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
