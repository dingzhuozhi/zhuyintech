import pandas as pd
import requests
import time
import random
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
import os
def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
    text = fake_file_handle.getvalue()
# close open handles
    converter.close()
    fake_file_handle.close()
    if text:
        return text

txt_list=[]
date_list=[]
file_list=os.listdir(r"D:\pachong\FOMC发布会视频文本pdf")
for file in file_list:
    print(file[:8])
    fomc_txt=extract_text_from_pdf(r"D:\pachong\FOMC发布会视频文本pdf\{}".format(file))
    date_list.append(file[:8])
    txt_list.append(fomc_txt)

df=pd.DataFrame({"date":date_list,"txt":txt_list})
df.to_csv(r"D:\pachong\历史文本csv版本\FOMC发布会视频文本.csv",index=False)