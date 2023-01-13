"""
BOJ 爬虫 USD/JPY  美元对日元 Japaneseyen
爬取的内容为pdf格式
直接向pdf网站发送请求，下载为pdf，再读取pdf
"""
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
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

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

def main(website):
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
    count=0
    while True:
        if count <= 20:
            start=time.time()
            try:
                error_text=driver.find_element(By.XPATH,'//*[@id="contents"]/h1').text #BOJ网页发生变化
            except:
                error_text="找到了"
            if (error_text == 'ページが見つかりません | Not Found'):  # 则为未更新的页面或者不存在的页面
                print("此时未更新,继续查询")
                count = count + 1
                time.sleep(random.randint(100, 150) / 1000)
            else:
                url = website
                start = time.time()
                r = requests.get(url, stream=True)
                with open('BOJ.pdf', 'wb') as fd:
                    for chunk in r.iter_content(4):
                        fd.write(chunk)
                pdf_path='BOJ.pdf'
                #print("耗时:",time.time()-start)
                return extract_text_from_pdf(pdf_path)

        else:
            count = 0
            driver.refresh()


if __name__ == '__main__':
    website = "https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2023/k230118a.pdf"  #日本央行的网站发生了变化
    #website = "https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2022/k221220a.pdf"
    print(main(website))

