from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

"""
config
"""

website='https://cn.investing.com/economic-calendar/core-pce-price-index-905'
txt_form=r"美国核心个人消费支出平减指数(PCE)年化季率"
click_time=80

"""
excute
"""

options = webdriver.ChromeOptions()
mobileEmulation = {"deviceName": "iPad"}
options.page_load_strategy = 'eager'
options.add_experimental_option("mobileEmulation", mobileEmulation)
options.add_argument("--headless")  # 无界面显示
options.add_argument("--disable-gpu")  # 禁止gpu
options.add_argument("--disable-software-rasterizer")  # 无界面
options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片
options.add_argument("--disable-extensions")  # 禁用插件加载

driver = webdriver.Chrome(options=options)

driver.get(website)
xpath_num=website.split("-")[-1]
print(xpath_num)
click_element=driver.find_element(By.XPATH,'//*[@id="showMoreHistory{}"]/a'.format(xpath_num))
for i in range(click_time):
    try:
        click_element.click()
    except:
        break
data_element=driver.find_element(By.XPATH,'//*[@id="eventTabDiv_history_0"]')
text=data_element.text


month = [
    " (一月)",
    " (二月)",
    " (三月)",
    " (四月)",
    " (五月)",
    " (六月)",
    " (七月)",
    " (八月)",
    " (九月)",
    " (十月)",
    " (十一月)",
    " (十二月)"
]
for i in month:
    text=text.replace(i,"")

season=[" (第一季度)",
        " (第二季度)",
        " (第三季度)",
        " (第四季度)"
]

for i in season:
    text=text.replace(i,"")

text=text.replace("   ","  ")
text=text.replace("    ","   ")
text=text.replace(" ","\t")
text='\n'.join(text.split('\n')[:-1]).strip()
with open("网页数据.txt".format(txt_form),"w+",encoding="utf-8") as tx:
    tx.write(text)



df=pd.read_csv("网页数据.txt",sep="\t")
df.to_csv(r"{}.csv".format(txt_form),index=False)




