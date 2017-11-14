from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()

# 设置中文
#options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
aaoptions.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

browser = webdriver.Chrome("C:/Users/Alan/Downloads/chromedriver_win32/chromedriver.exe",chrome_options=options)
browser.get('https://www.skyscanner.com.tw/transport/d/tpe/2018-04-07/kix/tak/2018-04-14/tpe?adults=2&children=1&adultsv2=2&childrenv2=5&infants=0&cabinclass=economy&ref=day-view&seo_airline=dd#results')

"""
element = browser.find_element_by_id("i0116")
element.send_keys("hddsom")
element = browser.find_element_by_id("idSIButton9")
element.send_keys(Keys.RETURN)
element = browser.find_element_by_id("i0118")
element.send_keys("@XXXXXXXX")
element = browser.find_element_by_id("idBtn_Back")
element.send_keys(Keys.RETURN)
"""
