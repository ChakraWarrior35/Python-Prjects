from PyPDF2 import PdfWriter
from PyPDF2.errors import DependencyError
import os

merger = PdfWriter()

pdfs = []

n = int(input("Enter number of PDFs you want to merge: "))

for i in range(0, n):
    name = input(f"Enter the name of PDF files with .pdf {i+1}: ")
    if not name.lower().endswith('.pdf'):
        name = name + '.pdf'
    pdfs.append(name)

added = 0
for pdf in pdfs:
    if not os.path.exists(pdf):
        print(f"File not found, skipping: {pdf}")
        continue
    try:
        merger.append(pdf)
        added += 1
    except DependencyError:
        print(
            f"Cannot append {pdf}: PyCryptodome is required for AES-encrypted PDFs.\n"
            "Install it with: python -m pip install pycryptodome"
        )
    except Exception as e:
        print(f"Failed to append {pdf}: {e}")

if added == 0:
    print("No PDFs were merged. Ensure the files exist and try again.")
else:
    merger.write("merged-pdf.pdf")
    merger.close()
print(f"Merged {added} PDFs into 'merged-pdf.pdf'")