from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#driver_path=ChromeDriverManager().install()
#driver = webdriver.Chrome(service=Service(driver_path))


from webdriver_manager.core.utils import get_browser_version_from_os

from webdriver_manager.chrome import ChromeDriverManager
import requests,re,time,os

browserVersion=get_browser_version_from_os("google-chrome") # 获取当前系统chrome浏览器的版本号
print("当前系统chrome浏览器的版本号:",browserVersion)

ChromeDriverManager(path=r"C:\Users\Dell\anaconda3\Drivers").install() #指定我们的安装路径

mainBrowserVersion=browserVersion.split(".")[0] # 获取浏览器的主版本号
print("当前系统Chrome浏览器的主版本号:",mainBrowserVersion)
resp=requests.get(url="https://chromedriver.storage.googleapis.com/")
content=resp.text

availableVersionList=re.search(f"({mainBrowserVersion}\.\d+\.\d+\.\d+)/chromedriver\_win32\.zip.*?",content,re.S)
if availableVersionList==None:
    print(f"镜像网站上没有找到主版本号为{mainBrowserVersion}的chromedriver文件，请核实！")
    time.sleep(10)
    os.exit(0)
else:
    availableVersion=availableVersionList.group(1)
driver_path=ChromeDriverManager(version=availableVersion).install() # 找到镜像网站中主版本号与chrome主版本一致的，将匹配到的第一个完整版本号的chromedriver下载使用
