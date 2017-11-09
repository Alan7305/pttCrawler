from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.google.com.tw')
driver.maximize_window()

# by id
element = driver.find_element_by_id('lst-ib')

# key in
element.send_keys("hddsom")

# enter
element.send_keys(Keys.RETURN)

sleep(10)
driver.quit()