# extracts the characters from Image using Tessaract Library
# Dependencies: Tessaract
from PIL import Image
import pytesseract

im = Image.open("sample.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')
escaped_text = text.encode('ascii', 'ignore')

# print(text)
file = open('output.txt', 'w')
file.write(escaped_text)
file.close()