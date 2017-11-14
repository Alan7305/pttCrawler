from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://outlook.com/')
driver.maximize_window()

element = driver.find_element_by_css_selector('.buttonLargeBlue')
element.send_keys(Keys.RETURN)

element = driver.find_element_by_id('i0116')
element.send_keys("hdd525@msn.com")
element.send_keys(Keys.RETURN)
sleep(1)
element = driver.find_element_by_id('i0118')
element.send_keys("@lan9879665")
element.send_keys(Keys.RETURN)
sleep(1)
element = driver.find_element_by_id('22')
element.click()
sleep(1)
element = driver.switch_to_active_element()
element.send_keys("julie_shie@carrefour.com")
sleep(1)
element = driver.find_element_by_id('TextField419')
element.send_keys("自動發信給謝筑涵老婆兒~")
element.send_keys("自動的啦")

sleep(5)
driver.quit()

"""
driver = webdriver.Chrome()
driver.get('https://www.google.com.tw')
driver.maximize_window()

# by id
element = driver.find_element_by_id('lst-ib')

# key in
element.send_keys("hddsom")

# enter
element.send_keys(Keys.RETURN)

sleep(5)
driver.quit()
"""