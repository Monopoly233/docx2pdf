import os
import glob
from docx2pdf import convert

# 获取当前目录下的所有docx文件
docx_files = glob.glob("*.docx")

# 打印检测到的所有docx文件
print("检测到的所有docx文件：")
for file in docx_files:
    print(file)

# 将每个docx文件转换为pdf文件
for docx_file in docx_files:
    pdf_file = os.path.splitext(docx_file)[0] + ".pdf"
    convert(docx_file, pdf_file)
    print(f"{docx_file} 转换为 {pdf_file} 成功！")
