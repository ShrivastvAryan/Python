from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files=[ file for file in os.listdir() if file.endswith('.pdf')]

for pdf in ['All Contents- Mega Pack.pdf','Biggst Bundle Data.pdf','Updated Courses.pdf']:
    merger.append(pdf)

merger.write('merger-pdf.pdf')
print("PDFs merged successfully into 'merger-pdf.pdf'.")
merger.close()