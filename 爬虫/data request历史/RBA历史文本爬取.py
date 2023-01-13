from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import random
import socket


def main(website):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("--window-size=1920,1080")  # 界面大小
    options.add_argument("--headless")  # 无界面显示
    options.add_argument("--disable-gpu")  # 禁止gpu
    options.add_argument("--disable-software-rasterizer")  # 无界面
    options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片
    options.add_argument("--disable-extensions")  # 禁用插件加载
    driver = webdriver.Chrome(options=options)

    for i in range(1,13):
        driver.get(website)
        rba_date=driver.find_element(By.XPATH, '//*[@id="content"]/section/ul/li[{}]/a'.format(i)).text #得到了列表第一位的日期，可以来确定是否是我们想要的
        #if rba_website=="1 November 2022":
            #print(rba_website)
        rba_website=driver.find_element(By.XPATH,'//*[@id="content"]/section/ul/li[{}]/a'.format(i)).get_attribute("href") #获取到了我们真正想要爬到的页面
        print(rba_website)
        #开始正式文本的爬取
        driver.get(rba_website)
        main_text = driver.find_element(By.XPATH, '//*[@id="content"]')
        #print(main_text.text)
        # 后续需要增加端口去即时传输main_text.text
        full_name = "../RBA历史文本/"+"RBA "+rba_date+".txt"
        print(full_name)
        with open(full_name, 'w+', encoding="utf-8") as f:
            f.write(main_text.text)  # 录入实际发布文本的信息

if __name__ == "__main__":
    website = "https://www.rba.gov.au/monetary-policy/int-rate-decisions/2021/" #只需要改年份，可以获得当前年所有text
    main(website)

