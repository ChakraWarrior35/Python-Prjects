import os
import sys
import argparse
from PyPDF2 import PdfWriter


def resolve_path(name: str):
    if os.path.exists(name):
        return name
    if not name.lower().endswith('.pdf'):
        alt = name + '.pdf'
        if os.path.exists(alt):
            return alt
    return None


def interactive_input():
    pdfs = []
    try:
        n = int(input("Enter number of PDFs you want to merge: "))
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)

    for i in range(0, n):
        while True:
            name = input(f"Enter the name of PDF files {i+1}: ")
            rp = resolve_path(name)
            if rp:
                pdfs.append(rp)
                break
            print(f"File not found: {name}. Try again or provide a full path.")
    return pdfs


def main():
    parser = argparse.ArgumentParser(description="Merge multiple PDF files into one.")
    parser.add_argument('files', nargs='*', help='PDF files to merge (paths or names without .pdf)')
    parser.add_argument('-o', '--output', default='merged-pdf.pdf', help='Output merged PDF name')
    args = parser.parse_args()

    if args.files:
        pdfs = []
        for name in args.files:
            rp = resolve_path(name)
            if rp:
                pdfs.append(rp)
            else:
                print(f"File not found: {name}")
                sys.exit(1)
    else:
        pdfs = interactive_input()

    merger = PdfWriter()
    for pdf in pdfs:
        merger.append(pdf)

    try:
        with open(args.output, 'wb') as fout:
            merger.write(fout)
        print(f"Merged {len(pdfs)} files into {args.output}")
    except Exception as e:
        print("Failed to write output:", e)
        sys.exit(1)


if __name__ == '__main__':
    main()