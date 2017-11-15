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
driver.get('https://www.skyscanner.com.tw/transport/d/tpe/2018-04-07/kix/tak/2018-04-14/tpe?adults=2&children=1&adultsv2=2&childrenv2=5&infants=0&cabinclass=economy&ref=day-view&seo_airline=dd#results')

sleep(15)
soup = BeautifulSoup(driver.page_source, 'lxml')
articles = soup.select('.day-list-item')

i = 0
data = []
for article in articles:
    if i < 3:
        #去程時刻
        tripTogo = article.select('.card-main')[0].getText()
        tripTogo_ST = re.findall(r"\d{2}:\d{2}", tripTogo)[0]
        tripTogo_ET = re.findall(r"\d{2}:\d{2}", tripTogo)[1]
        #回程時刻
        tripReturn = article.select('.card-main')[1].getText()
        tripReturn_ST = re.findall(r"\d{2}:\d{2}", tripReturn)[0]
        tripReturn_ET = re.findall(r"\d{2}:\d{2}", tripReturn)[1]
        #價格
        tripPrice = article.select('.mainquote-group-price')[0].getText()
        tripPrice = re.search(r"\d+,\d+", tripPrice).group().replace(',','')
        
        data.append({
                        'tripTogo_ST':tripTogo_ST,
                        'tripTogo_ET':tripTogo_ET,
                        'tripReturn_ST':tripReturn_ST,
                        'tripReturn_ET':tripReturn_ET,
                        'tripPrice':tripPrice
                    })
        i += 1
    else:
        break

print(data)

sleep(10)
driver.quit()
