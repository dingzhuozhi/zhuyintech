"""
european central bank 欧洲中央银行
"""
# ecb网站后缀无法预测，只能通过前置页面判断是否更新。
# ecb持续时间短，会被反爬
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import undetected_chromedriver as uc
import io
from datetime import datetime
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def main_2(website): #进入 monetary decisions 页面抓取文本
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("--headless")  # 无界面显示
    options.add_argument("--disable-gpu")  # 禁止gpu
    options.add_argument("--disable-software-rasterizer")  # 无界面
    options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片
    options.add_argument("--disable-extensions")  # 禁用插件加载
    driver = webdriver.Chrome(options=options)
    driver.get(website)
    main_text = driver.find_element(By.XPATH, '//*[@id="main-wrapper"]/main/div[2]')
    return (main_text.text)


def main(date, website="https://www.ecb.europa.eu/press/govcdec/mopo/html/index.en.html"): #进入前置页面查询文本是否更新
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    options.add_argument("--headless")  # 无界面显示
    options.add_argument("--disable-gpu")  # 禁止gpu
    options.add_argument("--disable-software-rasterizer")  # 无界面
    options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片
    options.add_argument("--disable-extensions")  # 禁用插件加载
    driver = uc.Chrome(options=options)
    driver.get(website)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })
            """  # 禁用webdriver
    })
    use_cookie = driver.find_element(By.XPATH, '//*[@id="cookieConsent"]/div[1]/div/a[2]')
    use_cookie.click()
    time.sleep(1)
    count = 0
    start_time=time.time()
    while True:
        if count <= 20:
            first_catch = driver.find_element(By.XPATH, '//*[@id="snippet0"]/dt[1]/div')  # 定位日期是否一致
            href_catch = driver.find_element(By.XPATH, '//*[@id="snippet0"]/dd[1]/div[1]/a')  # 定位后置文本网页的href
            if (first_catch.text != date):  # 则为未更新的页面或者不存在的页面
                #print("此时未更新,继续查询")
                print(time.time()-start_time)
                count = count + 1
                time.sleep(random.randint(10, 15) / 1000)
            else:
                website = href_catch.get_attribute("href")
                main_text = main_2(website)
                return main_text
        else:
            count = 0
            driver.refresh()


if __name__ == '__main__':
    #print(main(date="27 October 2022"))
    print(main(date="16 December 2022"))
    #https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.mp221027~df1d778b84.en.html