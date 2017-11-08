from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:/Users/Alan/Downloads/chromedriver_win32/chromedriver.exe")
browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1510133860&rver=6.7.6640.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3frealm%3dmsn.com%26RpsCsrfState%3d83913b4a-51a3-43ab-a6fe-d0448192a6f4&id=292841&whr=msn.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015#wa=wsignin1.0')

element = browser.find_element_by_id("i0116")
element.send_keys("hddsom")
element = browser.find_element_by_id("idSIButton9")
element.send_keys(Keys.RETURN)
element = browser.find_element_by_id("i0118")
element.send_keys("@XXXXXXXX")
element = browser.find_element_by_id("idBtn_Back")
element.send_keys(Keys.RETURN)
