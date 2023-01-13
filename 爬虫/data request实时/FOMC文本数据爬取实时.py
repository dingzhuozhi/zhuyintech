from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import random
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

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
    count = 0
    driver.get(website)  # 需要修改网址
    while True:
        if count <= 20:
            try:
                title = driver.find_element(By.XPATH, '//*[@id="content"]').text  # 找到全文内容
            except:
                title="find it"
            if (title[5:19] == 'Page not found'):  # 则为未更新的页面或者不存在的页面
                print("此时未更新,继续查询")
                count = count + 1
                time.sleep(random.randint(5, 10) / 1000)
            else:
                main_text = driver.find_element(By.XPATH, '//*[@id="article"]/div[3]')  # 可以通过f12定位元素后直接右键复制获取
                print(main_text.text)
                return main_text.text
        else:  # 未更新次数超过20，刷新网页
            driver.refresh()
            count = 0  # 重新计时


if __name__ == '__main__':
    website_a = "https://www.federalreserve.gov/newsevents/pressreleases/monetary20221214a.htm"
    #website_a = "https://www.federalreserve.gov/newsevents/pressreleases/monetary20221102a.htm"
    main(website_a)
