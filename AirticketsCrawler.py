from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

<<<<<<< HEAD
options = webdriver.ChromeOptions()

# 设置中文
#options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
aaoptions.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

browser = webdriver.Chrome("C:/Users/Alan/Downloads/chromedriver_win32/chromedriver.exe",chrome_options=options)
browser.get('https://www.skyscanner.com.tw/transport/d/tpe/2018-04-07/kix/tak/2018-04-14/tpe?adults=2&children=1&adultsv2=2&childrenv2=5&infants=0&cabinclass=economy&ref=day-view&seo_airline=dd#results')

"""
element = browser.find_element_by_id("i0116")
=======
driver = webdriver.Chrome()
driver.get('https://www.google.com.tw')
driver.maximize_window()

# by id
element = driver.find_element_by_id('lst-ib')

# key in
>>>>>>> bb69b8013c80b96e7a6b802221ccf4c21bfcc4b0
element.send_keys("hddsom")

# enter
element.send_keys(Keys.RETURN)
<<<<<<< HEAD
"""
=======

sleep(10)
driver.quit()
>>>>>>> bb69b8013c80b96e7a6b802221ccf4c21bfcc4b0
