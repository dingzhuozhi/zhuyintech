"""
bank of canda
https://www.bankofcanada.ca/2022/10/fad-press-release-2022-10-26/ 格式比较固定
main_text = driver.find_element(By.CLASS_NAME, 'post-content')
加拿大有13小时时差，但是都是中国时间晚上，所以还是在同一天
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

date=pd.read_csv("..\历史文本发布日期\BOC_date.csv",usecols=["date"])
index_date=date["date"].tolist()
date_index=[]

for i in index_date:
    year,month,day=str(i).split("/")
    if len(month)==1:
        new_month="0"+month
    else:
        new_month=month
    if len(day)==1:
        new_day="0"+day
    else:
        new_day=day[:2]
    date_index.append(year+"-"+new_month+"-"+new_day)

print(date_index)
date["date"]=date_index #更改日期格式


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
    driver.get(website)
    main_text = driver.find_element(By.CLASS_NAME, 'post-content')
    return (main_text.text)


text_list=[]
for date in date_index:
    website="https://www.bankofcanada.ca/{}/{}/fad-press-release-{}/".format(date[:4], date[5:7], date)
    print(website)
    text=main(website)
    print("-"*100)
    print(text)
    text_list.append(text)


df=pd.DataFrame({'date':date_index,"text":text_list})
df.to_csv("boc_data.csv",index=False,encoding='utf-8')

"""
DONE
"""