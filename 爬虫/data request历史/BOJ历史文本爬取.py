"""
BOJ 爬虫 USD/JPY  美元对日元 Japaneseyen
爬取的内容为pdf格式
直接向pdf网站发送请求，下载为pdf，再读取pdf
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import pandas as pd

#url="https://www.boj.or.jp/en/announcements/release_2022/k221028a.pdf"
#url="https://www.boj.or.jp/en/announcements/release_2022/k220922a.pdf"
#r=requests.get(url,stream=True,)


"""
for
with open('../BOJ历史文本/{}.pdf'.format(), 'wb') as fd:
    for chunk in r.iter_content(4):
        fd.write(chunk)
"""

df=pd.read_csv("BOJ_date.csv")
date_list=df["date"].tolist()
date_list=[str(i) for i in date_list]
print(date_list)

"""
for i in date_list:
    url="https://www.boj.or.jp/en/announcements/release_{}/k{}a.pdf".format(i[0:4],i[2:])
    print(url)
    r=requests.get(url,stream=True)
    with open('../BOJ历史文本/{}.pdf'.format(i), 'wb') as fd:
        for chunk in r.iter_content(4):
            fd.write(chunk)
"""
