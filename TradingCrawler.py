from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import re

options = webdriver.ChromeOptions()

# set lang
options.add_argument('lang=zh_TW.UTF-8')
# set header
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"')

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY_AVG.html')

elem = driver.find_element_by_name("stockNo")
elem.send_keys("2330")
elem.send_keys(Keys.RETURN)



sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')
articles = soup.select('[role=row]')

data = []
for article in articles:
    paragraphs = article.find_all('td')
    
    print('-------')
    for p in paragraphs:
        print(p.text)
    



sleep(10)
driver.quit()
