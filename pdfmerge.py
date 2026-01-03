from PyPDF2 import PdfWriter
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
    merger.append(pdf)
    added += 1

if added == 0:
    print("No PDFs were merged. Ensure the files exist and try again.")
else:
    merger.write("merged-pdf.pdf")
    merger.close()
    print(f"Merged {added} PDFs into merged-pdf.pdf")
    
