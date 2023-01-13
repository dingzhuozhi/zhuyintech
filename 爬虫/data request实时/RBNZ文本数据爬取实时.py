"""
New Zealand dollar
reserve bank of new zealand
 NZD/USD
http://www.rbnz.govt.nz/hub/news/2022/10/continued-monetary-tightening
新西兰比中国快5小时
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import undetected_chromedriver as uc


def main_2(website):
    options = webdriver.ChromeOptions()
    """
    options.page_load_strategy = 'eager'
    # options.add_argument("--window-size=1920,1080")  # 界面大小
    options.add_argument("--headless")  # 无界面显示
    options.add_argument("--disable-gpu")  # 禁止gpu
    options.add_argument("--disable-software-rasterizer")  # 无界面
    options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片
    options.add_argument("--disable-extensions")  # 禁用插件加载
    """
    driver = webdriver.Chrome(options=options)
    driver.get(website)
    main_text = driver.find_element(By.XPATH, '/html/body/div/div/main/div[3]/div/div')
    return (main_text.text)


def main_1(title,website='https://www.rbnz.govt.nz/news-and-events/news#f:@hierarchicalz95xsz120xatopictagnames=[Monetary%20policy]'):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.set_capability("detach", True)

    # options.page_load_strategy = 'normal'
    # options.add_argument("--headless")  # 无界面显示
    # options.add_argument("--disable-gpu")  # 禁止gpu
    # options.add_argument("--disable-software-rasterizer")  # 无界面
    # options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片
    # options.add_argument("--disable-extensions")  # 禁用插件加载

    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = uc.Chrome(options=options)

    script = '''object.defineProperty(navigator,'webdriver',{get: () => undefined})'''
    # execute_cdp_cmd用来执行chrome开发这个工具命令
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})

    driver.get(website)

    count = 0
    while True:
        if count <= 20:
            previous_text = driver.find_element(By.XPATH, '//*[@id="coveo-result-list1"]/div/div[1]/a/h5/span')
            if (previous_text.text == title):  # 如果首行标题仍为上次标题，则未更新，继续刷新
                print("此时未更新,继续查询")
                count = count + 1
                time.sleep(random.randint(10, 15) / 1000)
            else:
                previous_text = driver.find_element(By.XPATH, '//*[@id="coveo-result-list1"]/div/div[1]/a')
                href_website = previous_text.get_attribute("href")
                main_text = main_2(href_website)
                return main_text
        else:
            count = 0
            driver.refresh()


if __name__ == '__main__':
    print(main_1("Monetary Policy Announcement and Financial Stability Report dates for 2023/24"))
