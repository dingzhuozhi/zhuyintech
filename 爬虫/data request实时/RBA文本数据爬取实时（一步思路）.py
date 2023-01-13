from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import random
import socket

"""
相比于两步思路，一步的速度更快
实际部署中，我们可以考虑根据当天最新序号，以+1原则来部署
"""
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

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
    count = 0
    while True:
        if count <= 20:
            main_text = driver.find_element(By.XPATH, '//*[@id="content"]').text  # 找到全文内容
            if (main_text[4:18] == 'Page Not Found'):  # 则为未更新的页面或者不存在的页面
                print("此时未更新,继续查询")
                count = count + 1
                time.sleep(random.randint(5, 10) / 1000)
            else:
                return main_text

        else:
            count = 0
            driver.refresh()

if __name__ == '__main__':
    website="https://www.rba.gov.au/media-releases/2022/mr-22-36.html"
    #website = "https://www.rba.gov.au/media-releases/2022/mr-22-41.html"
    maintext=main(website)
    print(maintext)