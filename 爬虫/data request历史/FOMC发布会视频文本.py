"""
BOJ 爬虫 USD/JPY  美元对日元 Japaneseyen
爬取的内容为pdf格式
直接向pdf网站发送请求，下载为pdf，再读取pdf
"""
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import random
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

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

def main(website,date):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    #options.add_argument("--window-size=1920,1080")  # 界面大小
    options.add_argument("--headless")  # 无界面显示
    options.add_argument("--disable-gpu")  # 禁止gpu
    options.add_argument("--disable-software-rasterizer")  # 无界面
    options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片
    options.add_argument("--disable-extensions")  # 禁用插件加载
    driver = webdriver.Chrome(options=options)
    driver.get(website)
    url = website
    r = requests.get(url, stream=True)
    date_time=date
    print('D:\pachong\FOMC发布会视频文本pdf\{}.pdf'.format(date_time))
    with open(r'D:\pachong\FOMC发布会视频文本pdf\{}.pdf'.format(date_time), 'wb') as fd:
        for chunk in r.iter_content(4):
            fd.write(chunk)
    # pdf_path=r'D:\pachong\FOMC发布会视频文本pdf\{}.pdf'.format(date_time)
    # print("耗时:",time.time()-start)


#写入pdf版本。
if __name__ == '__main__':
    date_list=[]
    for i in os.listdir(r"C:\Users\Dell\Desktop\DataBase\DataBase\FOMC\Features\statement"):
        date_list.append(i[8:16])
    date_list.append("20221102")
    print(date_list)
    for i in date_list[::-1]:
        website="https://www.federalreserve.gov/mediacenter/files/FOMCpresconf{}.pdf".format(i)
        main(website,i)

