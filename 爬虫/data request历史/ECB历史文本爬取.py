"""
european central bank 欧洲中央银行
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

date = pd.read_csv(r"D:\pachong\历史文本发布日期\ECB_date.csv", usecols=["date"])

date_lis = date["date"].tolist()
date_list=[]
for i in date_lis:
    year,month,day=str(i).split("/")
    if len(month)==1:
        new_month="0"+month
    else:
        new_month=month
    if len(day)==1:
        new_day="0"+day
    else:
        new_day=day[:2]
    date_list.append(year+"-"+new_month+"-"+new_day)

print(date_list)
def main_2(website):
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
    main_text = driver.find_element(By.XPATH, '//*[@id="main-wrapper"]/main/div[2]')
    return (main_text.text)

print(len(date_list))

web_list = [
    "https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.mp221027~df1d778b84.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.mp220908~c1b6839378.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.mp220721~53e5bdd317.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.mp220609~122666c272.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.mp220414~d1b76520c6.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.mp220310~2d19f8ba60.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.mp220203~90fbe94662.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2021/html/ecb.mp211216~1b6d3a1fd8.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2021/html/ecb.mp211028~85474438a4.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2021/html/ecb.mp210909~2c94b35639.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2021/html/ecb.mp210722~48dc3b436b.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2021/html/ecb.mp210610~b4d5381df0.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2021/html/ecb.mp210422~f075ebe1f0.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2021/html/ecb.mp210311~35ba71f535.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2021/html/ecb.mp210121~eb9154682e.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2020/html/ecb.mp201210~8c2778b843.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2020/html/ecb.mp201029~4392a355f4.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2020/html/ecb.mp200910~f4a8da495e.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2020/html/ecb.mp200716~fc5fbe06d9.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2020/html/ecb.mp200604~a307d3429c.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2020/html/ecb.mp200430~1eaa128265.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2020/html/ecb.mp200312~8d3aec3ff2.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2020/html/ecb.mp200123~ae33d37f6e.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2019/html/ecb.mp191212~06d84240ae.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2019/html/ecb.mp191024~438769bd4f.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2019/html/ecb.mp190912~08de50b4d2.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2019/html/ecb.mp190725~52d3766c9e.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2019/html/ecb.mp190606~1876cad9a5.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2019/html/ecb.mp190410~3df2ed8a4c.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2019/html/ecb.mp190307~7d8a9d2665.en.html",
    "https://www.ecb.europa.eu/press/pr/date/2019/html/ecb.mp190124~5c00d09d5d.en.html",
    ""
]

web_list_18="https://www.ecb.europa.eu/press/pr/date/2018/html/ecb.mp181213.en.html"

#2019年到2022年后缀无法预测，只能用网页抓取。
def main_3(website):
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
    main_text = driver.find_element(By.XPATH, '//*[@id="main-wrapper"]/main/div[4]')
    return (main_text.text)


for i in date_list:
    if i<="2018-12-20" and i>="2018-09-13":
        website="https://www.ecb.europa.eu/press/pr/date/{}/html/ecb.mp{}{}{}.en.html".format(i[:4],i[2:4],i[5:7],i[8:10])
        print(website)
        main_text = main_3(website)
        full_name = "../ECB历史文本/"+"ECB "+str(i)+".txt"
        print(full_name)
        with open(full_name, 'w+', encoding="utf-8") as f:
            f.write(main_text)  # 录入实际发布文本的信息
"""


for i in date_list:
    if i<"2016-03-10":
        website="https://www.ecb.europa.eu/press/pr/date/{}/html/pr{}{}{}.en.html".format(i[:4],i[2:4],i[5:7],i[8:10])
        print(website)
        main_text = main_3(website)
        full_name = "../ECB历史文本/"+"ECB "+str(i)+".txt"
        print(full_name)
        with open(full_name, 'w+', encoding="utf-8") as f:
            f.write(main_text)  # 录入实际发布文本的信息

"""