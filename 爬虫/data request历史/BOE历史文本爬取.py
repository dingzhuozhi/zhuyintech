"""
bank of england
我们爬取的是：Monetary Policy Summary
示范网站为：https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2022/november-2022
可修改的格式：年份，月份
22,21,20,19,18,17年份格式为：https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2022/november-2022
16,15,14年份格式为：https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2016/mpc-january-2016
13年份格式为：https://www.bankofengland.co.uk/minutes/2013/monetary-policy-committee-january-2013

需要更改定位xpath，还要改年份格式,具体xpath定位的代码在下面
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

month_dict={
    1 : "january",
    2 : "february",
    3 : "march",
    4 : "april",
    5 : "may",
    6 : "june",
    7 : "july",
    8 : "august",
    9 : "september",
    10 : "october",
    11 : "november",
    12 : "december"}

def main_1(website): #适用于2021年8月到2022年整年
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
    main_text = driver.find_element(By.XPATH, '//*[@id="output"]/section[1]')
    return (main_text.text)
    # 后续需要增加端口去即时传输main_text.text

def main_2(website): #适用于2020年6月到2021年6月
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
    main_text = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[2]/div/div[1]/div[2]/div')

    return (main_text.text)

def main_3(website): #适用于2020年5月到2020年5月
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
    main_text = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[2]/div/div[2]/div/div')

    return (main_text.text)

def main_4(website): #适用于2020年3月
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
    main_text = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[2]/div[2]/div[1]/div[2]/div')
    return (main_text.text)

def main_5(website): #适用于2020年1月
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
    main_text = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[3]/div/div[2]/div[2]/div')
    return (main_text.text)

def main_6(website):
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
    main_text = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[2]/div[2]/div[1]/div/div')
    return (main_text.text)

def main_7(website):
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
    main_text = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[4]/div/div[1]/div[2]/div')
    return (main_text.text)

def main_8(website):
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
    main_text = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[3]/div/div[1]/div/div')
    return (main_text.text)


data=pd.read_csv(r"D:\pachong\历史文本发布日期\BOE_date.csv")
year_list=data["date"].tolist()
month_list=data["month"].tolist()


for year,month in zip(year_list,month_list):
    if year==2018 and month >=9 and month<=9:
        website="https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/{}/{}-{}".format(year,month_dict[month],year)
        print(website)
        try:
            main_text=main_8(website)
        except:
            main_text=main_8(website)
        print("-"*100)
        full_name= "../BOE历史文本/"+"BOE "+str(year)+str(month)+".txt"
        print(full_name)
        with open(full_name, 'w+', encoding="utf-8") as f:
            f.write(main_text)  # 录入实际发布文本的信息


