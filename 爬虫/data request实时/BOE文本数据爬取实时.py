"""
bank of england
我们爬取的是：Monetary Policy Summary
示范网站为：https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2022/november-2022
可修改的格式：年份，月份
需要更改定位xpath，还要改年份格式,具体xpath定位的代码在下面
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def main_1(website):  # 适用于2021年8月到2022年整年
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    # options.add_argument("--window-size=1920,1080")  # 界面大小
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
            start = time.time()
            try:
                error_text = driver.find_element(By.XPATH,
                                                 '//*[@id="main-content"]/section[2]/div/div[1]/div[2]/div/h2').text
            except:
                error_text = "找到了"
            if (
                    error_text == 'This Monetary Policy Summary and minutes of the Monetary Policy Committee meeting will be published on 15 December 2022.'):  # 则为未更新的页面或者不存在的页面
                print("此时未更新,继续查询")
                count = count + 1
                time.sleep(random.randint(10, 15) / 1000)
            else:
                main_text = driver.find_element(By.XPATH, '//*[@id="output"]/section[1]')
                # print(time.time() - start)
                return main_text.text
        else:
            count = 0
            driver.refresh()


if __name__ == '__main__':
    print(main_1("https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2022/december-2022"))
    # print(main_1("https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2022/november-2022"))
