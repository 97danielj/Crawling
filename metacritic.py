import warnings
warnings.filterwarnings('ignore')
import time
from bs4 import BeautifulSoup
from selenium import webdriver
#브라우저버전에 적합한 엣지드라이버 설치
import edgedriver_autoinstaller
edgedriver_autoinstaller.install()

from selenium.webdriver.common.keys import Keys
import json
b = webdriver.Edge()
b.maximize_window()
b.get('https://www.metacritic.com/game')
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/div[2]/div/ul/li[11]/div/span/a').click()
b.implicitly_wait(10)
data = []