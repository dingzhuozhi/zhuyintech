"""
New Zealand dollar
reserve bank of new zealand
 NZD/USD
http://www.rbnz.govt.nz/hub/news/2022/10/continued-monetary-tightening
新西兰比中国快4小时
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

date=pd.read_csv("../RBNZ_date.csv",usecols=["date"])
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
print(len(date_index))

def main_1(website):
    options = webdriver.ChromeOptions()
    """
    options.page_load_strategy = 'normal'
    options.add_argument("--window-size=1920,1080")  # 界面大小
    options.add_argument("--headless")  # 无界面显示
    options.add_argument("--disable-gpu")  # 禁止gpu
    options.add_argument("--disable-software-rasterizer")  # 无界面
    options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片
    options.add_argument("--disable-extensions")  # 禁用插件加载
    """
    driver = webdriver.Chrome(options=options)
    driver.get(website)
    next_website_list = []
    #content = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="coveo-result-list1"]/div/div[{}]/a'.format(i))))
    for i in range(1,11):
        content=driver.find_element(by=By.XPATH,value='//*[@id="coveo-result-list1"]/div/div[{}]/a'.format(i))
        next_website=content.get_attribute("href")
        next_website_list.append(next_website)
    return next_website_list


def main_2(website):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片
    """
    options.add_argument("--window-size=1920,1080")  # 界面大小
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


second_website_list=[
    "https://www.rbnz.govt.nz/hub/news/2022/10/continued-monetary-tightening",
    "https://www.rbnz.govt.nz/hub/news/2022/08/ongoing-monetary-tightening",
    "https://www.rbnz.govt.nz/hub/news/2022/07/monetary-tightening-continues",
    "https://www.rbnz.govt.nz/hub/news/2022/05/monetary-conditions-tighten-by-more-and-sooner",
    "https://www.rbnz.govt.nz/hub/news/2022/04/monetary-tightening-brought-forward",
    "https://www.rbnz.govt.nz/hub/news/2022/02/more-tightening-needed",
    "https://www.rbnz.govt.nz/hub/news/2021/11/mpc-continues-to-reduce-monetary-stimulus",
    "https://www.rbnz.govt.nz/hub/news/2021/10/monetary-stimulus-further-reduced-official-cash-rate-raised-to-050-percent",
    "https://www.rbnz.govt.nz/hub/news/2021/08/official-cash-rate-on-hold-at-025-percent",
    "https://www.rbnz.govt.nz/hub/news/2021/07/monetary-stimulus-reduced",
    "https://www.rbnz.govt.nz/hub/news/2021/05/monetary-support-continued",
    "https://www.rbnz.govt.nz/hub/news/2021/04/monetary-stimulus-continued",
    "https://www.rbnz.govt.nz/hub/news/2021/02/prolonged-monetary-stimulus-necessary",
    "https://www.rbnz.govt.nz/hub/news/2020/11/more-monetary-stimulus-provided",
    "https://www.rbnz.govt.nz/hub/news/2020/09/prolonged-monetary-support-necessary",
    "https://www.rbnz.govt.nz/hub/news/2020/08/further-easing-in-monetary-policy-delivered",
    "https://www.rbnz.govt.nz/hub/news/2020/06/monetary-policy-easing-to-continue",
    "https://www.rbnz.govt.nz/hub/news/2020/05/large-scale-asset-purchases-expanded",
    "https://www.rbnz.govt.nz/hub/news/2020/03/ocr-reduced-to-025-percent-for-next-12-months",
    "https://www.rbnz.govt.nz/hub/news/2020/02/official-cash-rate-remains-at-1-percent",
    "https://www.rbnz.govt.nz/hub/news/2019/11/official-cash-rate-unchanged-at-1-percent",
    "https://www.rbnz.govt.nz/hub/news/2019/09/official-cash-rate-unchanged-at-1-percent",
    "https://www.rbnz.govt.nz/hub/news/2019/08/official-cash-rate-reduced-to-1-percent",
    "https://www.rbnz.govt.nz/hub/news/2019/06/official-cash-rate-unchanged-at-1-5-percent",
    "https://www.rbnz.govt.nz/hub/news/2019/05/official-cash-rate-reduced-to-1-5-percent",
    "https://www.rbnz.govt.nz/hub/news/2019/03/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2019/02/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2018/11/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2018/09/ocr-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2018/08/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2018/06/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2018/05/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2018/03/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2018/02/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2017/11/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2017/09/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2017/08/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2017/06/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2017/05/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2017/03/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2017/02/official-cash-rate-unchanged-at-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2016/11/official-cash-rate-reduced-to-1-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2016/09/official-cash-rate-unchanged-at-2-percent",
    "https://www.rbnz.govt.nz/hub/news/2016/08/official-cash-rate-reduced-to-2-percent",
    "https://www.rbnz.govt.nz/hub/news/2016/06/official-cash-rate-unchanged-at-2-25-percent",
    "https://www.rbnz.govt.nz/hub/news/2016/04/official-cash-rate-unchanged-at-2-25-percent",
    "https://www.rbnz.govt.nz/hub/news/2016/03/official-cash-rate-reduced-to-2-25-percent",
    "https://www.rbnz.govt.nz/hub/news/2016/01/official-cash-rate-unchanged-at-2-5-percent",
    "https://www.rbnz.govt.nz/hub/news/2015/12/official-cash-rate-reduced-to-two-and-a-half-percent",
    "https://www.rbnz.govt.nz/hub/news/2015/10/official-cash-rate-unchanged-at-2-75-percent",
    "https://www.rbnz.govt.nz/hub/news/2015/09/news-release-announcing-mps-for-september-2015",
    "https://www.rbnz.govt.nz/hub/news/2015/07/official-cash-rate-reduced-to-3-0-percent",
    "https://www.rbnz.govt.nz/hub/news/2015/06/news-release-announcing-mps-for-june-2015",
    "https://www.rbnz.govt.nz/hub/news/2015/04/ocr-unchanged-at-3-5-percent",
    "https://www.rbnz.govt.nz/hub/news/2015/03/news-release-announcing-mps-for-march-2015",
    "https://www.rbnz.govt.nz/hub/news/2015/01/ocr-unchanged-at-3-5-percent",
    "https://www.rbnz.govt.nz/hub/news/2014/12/news-release-announcing-mps-for-december-2014",
    "https://www.rbnz.govt.nz/hub/news/2014/10/ocr-unchanged-at-3-5-percent",
    "https://www.rbnz.govt.nz/hub/news/2014/09/news-release-announcing-mps-for-september-2014",
    "https://www.rbnz.govt.nz/hub/news/2014/07/rbnz-raises-ocr-to-3-5-percent",
    "https://www.rbnz.govt.nz/hub/news/2014/06/news-release-announcing-mps-for-june-2014",
    "https://www.rbnz.govt.nz/hub/news/2014/04/reserve-bank-raises-ocr-to-3-percent",
    "https://www.rbnz.govt.nz/hub/news/2014/03/news-release-announcing-mps-for-march-2014",
    "https://www.rbnz.govt.nz/hub/news/2014/01/ocr-unchanged-at-2-5-percent",
    "https://www.rbnz.govt.nz/hub/news/2013/12/news-release-announcing-mps-for-december-2013",
    "https://www.rbnz.govt.nz/hub/news/2013/10/ocr-unchanged-at-2-5-percent",
    "https://www.rbnz.govt.nz/hub/news/2013/09/news-release-announcing-mps-for-september-2013",
    "https://www.rbnz.govt.nz/hub/news/2013/07/ocr-unchanged-at-2-5-percent",
    "https://www.rbnz.govt.nz/hub/news/2013/06/news-release-announcing-mps-for-june-2013",
    "https://www.rbnz.govt.nz/hub/news/2013/04/ocr-unchanged-at-2-5-percent",
    "https://www.rbnz.govt.nz/hub/news/2013/03/news-release-announcing-mps-for-march-2013",
    "https://www.rbnz.govt.nz/hub/news/2013/01/ocr-unchanged-at-2-5-percent"
]




if __name__ == '__main__':

    for website in second_website_list:
        print(website)
        main_text=main_2(website)
        full_name = "../RBNZ历史文本/" + "RBNZ " + website.split("/")[5]+website.split("/")[6] + ".txt"
        print(full_name)
        with open(full_name, 'w+', encoding="utf-8") as f:
            f.write(main_text)







