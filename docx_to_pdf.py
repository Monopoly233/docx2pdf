import os
import glob
from docx2pdf import convert

# gain all docx in same directory
docx_files = glob.glob("*.docx")

# print all files in the same directory 
print("sense all docx file：")
for file in docx_files:
    print(file)

# change every file to pdf 
for docx_file in docx_files:
    pdf_file = os.path.splitext(docx_file)[0] + ".pdf"
    convert(docx_file, pdf_file)
    print(f"{docx_file} to {pdf_file} success！")
