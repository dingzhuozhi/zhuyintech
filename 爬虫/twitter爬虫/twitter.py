"""
bank of canda
https://www.bankofcanada.ca/2022/10/fad-press-release-2022-10-26/ 格式比较固定
main_text = driver.find_element(By.CLASS_NAME, 'post-content')
加拿大有13小时时差，但是都是中国时间晚上，所以还是在同一天
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def main(website):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    #options.add_argument("--window-size=1920,1080")  # 界面大小
    # options.add_argument("--headless")  # 无界面显示
    # options.add_argument("--disable-gpu")  # 禁止gpu
    # options.add_argument("--disable-software-rasterizer")  # 无界面
    # options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片
    # options.add_argument("--disable-extensions")  # 禁用插件加载
    driver = webdriver.Chrome(options=options)
    driver.get(website)
    time.sleep(20)
    for i in range(1,20):
        main_text = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[{}]/div/div/div/article'.format(i))
        print(main_text.text)



if __name__ == '__main__':
    print(main("https://twitter.com/NickTimiraos"))
"""
'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/div/article'
'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[2]/div/div/div/article'
'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[6]/div/div/div/article'
"""