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
                error_text=driver.find_element(By.XPATH,'//*[@id="error_content"]/h1').text
                print(error_text)
            except:
                error_text="找到了"
                #print("find it ")
            if (error_text == '404 - file not found'):  # 则为未更新的页面或者不存在的页面
                print("此时未更新,继续查询")
                count = count + 1
                time.sleep(random.randint(10, 15) / 1000)
            else:
                main_text = driver.find_element(By.CLASS_NAME, 'post-content')
                #print(time.time()-start)
                return main_text.text

        else:
            count = 0
            driver.refresh()

if __name__ == '__main__':
    #date="2022-10-26"
    date="2022-12-07"
    website="https://www.bankofcanada.ca/{}/{}/fad-press-release-{}/".format(date[:4], date[5:7], date)
    print(website)
    text=main(website)
    #print("-"*100)
    print(text)



