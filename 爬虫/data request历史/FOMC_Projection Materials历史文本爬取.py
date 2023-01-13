import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import io
import sys
import pandas
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
from tqdm import *

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
    driver.get(website)  # 需要修改网址
    main_text = driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div')  # 可以通过f12定位元素后直接右键复制获取
    return main_text.text

if __name__ == '__main__':
    df=pd.read_csv(r"D:\pachong\历史文本发布日期\fomc_date_time_america.csv")
    date_list=df.date.tolist()

    for date in tqdm(date_list[::-1]):
        year,month,day=date.split("/")
        if len(month)==1:
            month="0"+month
        if len(day)==1:
            day="0"+day
        website="https://www.federalreserve.gov/monetarypolicy/fomcprojtabl{}{}{}.htm".format(year,month,day)
        website_2="https://www.federalreserve.gov/monetarypolicy/fomcprojtable{}{}{}.htm".format(year,month,day)
        print(website)
        try:
            text=main(website)
        except:
            try:
                text=main(website_2)
            except:
                text=""
        full_name = r"D:\pachong\FOMC_Projection Materials历史文本txt\FOMC_Projection_Materials_{}.txt".format(date.replace("/","."))
        print(full_name)
        with open(full_name, 'w+', encoding="utf-8") as f:
            f.write(text)  # 录入实际发布文本的信息

