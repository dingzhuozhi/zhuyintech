import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
import sys
import pandas
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
from tqdm import *

def main(website,date): # 向网页发送请求并保存为pdf
    url = website
    r = requests.get(url, stream=True)
    with open(r"D:\pachong\FOMC_projection_pdf历史文本\FOMC_Projection_Materials_{}.pdf".format(date.replace("/",".")), 'wb') as fd:
        for chunk in r.iter_content(4):
            fd.write(chunk)

if __name__ == '__main__':
    df=pd.read_csv(r"D:\pachong\历史文本发布日期\fomc_date_time_america.csv")
    date_list=df.date.tolist()

    for date in tqdm(date_list[::-1]):
        year,month,day=date.split("/")
        if len(month)==1:
            month="0"+month
        if len(day)==1:
            day="0"+day
        website="https://www.federalreserve.gov/monetarypolicy/files/fomcprojtabl{}{}{}.pdf".format(year,month,day)
        website_2="https://www.federalreserve.gov/monetarypolicy/files/fomcprojtable{}{}{}.pdf".format(year,month,day)
        print(website)
        print(date)
        try:
            main(website,date)
        except:
            try:
                main(website_2,date)
            except:
                pass
