# keeps only specified pages of the PDF and removes other pages
from PyPDF2 import PdfFileWriter, PdfFileReader

pages_to_keep = [0] # page numbering starts from 0
infile = PdfFileReader('input.pdf', 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
  if i in pages_to_keep:
    p = infile.getPage(i)
    output.addPage(p)

with open('newfile.pdf', 'wb') as f:
  output.write(f)