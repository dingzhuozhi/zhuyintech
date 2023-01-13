import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import socket
import sys
def send_udp(host,port,message):
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
        s.sendto(message.encode('utf-8'),(host,port))

def crawl(website,id_list):  # ip地址
    send_udp("192.168.7.113", 40001,'crawl') #向监控端口传输
    mobileEmulation = {'deviceName': 'iPad'}
    options = webdriver.ChromeOptions()  # 谷歌浏览器
    options.page_load_strategy = 'eager'
    options.add_argument("--window-size=1920,1080")  # 界面大小
    options.add_argument("--headless")  # 无界面显示
    options.add_argument("--disable-gpu")  # 禁止gpu
    options.add_argument("--disable-software-rasterizer")  # 无界面
    options.add_argument("blink-settings=imagesEnabled=false")  # 不加载图片
    options.add_argument("--disable-extensions")  # 禁用插件加载
    options.add_experimental_option("mobileEmulation", mobileEmulation)  # 添加模拟参数
    driver = webdriver.Chrome(options=options)  # 谷歌浏览器
    driver.get(website)  # 实时更新的网站
    while True:  # 跑2000个
        msg_list = []
        msg = ""
        for id in id_list:
            if len(driver.find_element(By.ID, id).text) == 1:
                print("{}数据尚未更新".format(datetime.now()))
                time.sleep(random.randint(5, 10) / 1000)
            else:
                print("捕捉{}成功,当前时间为:".format(id), datetime.now())
                msg_list.append(driver.find_element(By.ID, id).text)
        # 判断结果是否完全，防止部分数据尚未更新或者当前进程中未被抓取
        if len(msg_list) == len(id_list):
            for item in msg_list:
                msg += str(item) + ","
            print("抓取的{}条记录为:".format(len(msg_list)), msg)
            return msg

if __name__ == "__main__":
    """
crawler的依次为下面四个的预测值，前值
1.美国未季调核心居民消费价格指数(CPI)年率
2.美国核心居民消费价格指数(CPI)月率
3.美国居民消费价格指数(CPI)月率
4.美国未季调居民消费价格指数(CPI)年率
    """
    try:
        """
        crawl_website=input("输入网址")
        crawl_content1=input("美国未季调核心居民消费价格指数(CPI)年率预测值")
        crawl_content2 = input("美国未季调核心居民消费价格指数(CPI)年率前值")
        crawl_content3 = input("美国核心居民消费价格指数(CPI)月率预测值")
        crawl_content4 = input("美国核心居民消费价格指数(CPI)月率前值")
        crawl_content5 = input("美国居民消费价格指数(CPI)月率预测值")
        crawl_content6 = input("美国居民消费价格指数(CPI)月率前值")
        crawl_content7 = input("美国未季调居民消费价格指数(CPI)年率预测值")
        crawl_content8 = input("美国未季调居民消费价格指数(CPI)年率前值")
        ip=input("爬虫发送ip")
        port=int(input("爬虫发送端口"))
        """
        crawl_website=sys.argv[1]
        crawl_content1=sys.argv[2]
        crawl_content2 = sys.argv[3]
        crawl_content3 = sys.argv[4]
        crawl_content4 = sys.argv[5]
        crawl_content5 = sys.argv[6]
        crawl_content6 = sys.argv[7]
        crawl_content7 = sys.argv[8]
        crawl_content8 = sys.argv[9]
        ip= sys.argv[10]
        port= int(sys.argv[11])
        crawl_content=[crawl_content1,crawl_content2,crawl_content3,crawl_content4,crawl_content5,crawl_content6,crawl_content7,crawl_content8]
        crawl_data=crawl(crawl_website,crawl_content)
        #crawl_data=re.findall(r"\d+\.?\d*", crawl_data)  # Transfer to list
        send_udp(ip,port, crawl_data)  # 向监控端口传输
        output = os.popen('cpi.exe arg1 arg2 arg3 arg4 arg5 arg6 arg7 arg8 arg9 arg10,arg11').read()
    except Exception as e:
        print(e.args)
        print(str(e))
