from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import random
import socket

"""
我们需要利用https://www.rba.gov.au/monetary-policy/rba-board-minutes/2022/来定位到最新RBA statement的网址，再进行爬取
需要注意的是需要监测列表第一个是否产生更新。
我们需要循环监测列表第一位日期是否和我们想要的日期一致，一致才会进入下一步
但这样导致的问题就是时间较长,
我们尝试了使用click操作，发现时间和重新get效果一致,甚至更慢。
"""

"""
实际部署中，我们可以考虑根据当天最新序号，以+1原则来部署
"""

def main(website, true_date):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("--window-size=1920,1080")  # 界面大小
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
            rba_date = driver.find_element(By.XPATH,
                                           '//*[@id="content"]/section/ul/li[1]/a').text  # 得到了列表第一位的日期，可以来确定是否是我们想要的
            if rba_date == true_date:  # 只有日期一致我们才会进行爬取，否则会一直循环
                rba_website = driver.find_element(By.XPATH, '//*[@id="content"]/section/ul/li[1]/a').get_attribute(
                    "href")  # 获取到了我们真正想要爬到的页面地址
                # 开始正式文本的爬取
                start = time.time()
                driver.get(rba_website)
                print(rba_website)
                main_text = driver.find_element(By.XPATH, '//*[@id="content"]')
                print(main_text.text)
                print(time.time() - start)
                return main_text
                # 后续需要增加端口去即时传输main_text.text
            else:
                count += 1
                print("最新日期尚未更新")
                time.sleep(random.randint(5, 10) / 1000)
        else:
            count = 0
            driver.refresh()


if __name__ == "__main__":
    website = "https://www.rba.gov.au/monetary-policy/int-rate-decisions/2022/"
    main(website, "1 November 2022")
