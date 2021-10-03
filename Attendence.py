# Webdriver For Firefox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://mgit.winnou.net/")
elem = driver.find_element_by_name('username')
elem1 = driver.find_element_by_name('passwd')
elem.send_keys('your_user_id' )
elem1.send_keys('your_password',Keys.RETURN )
driver.implicitly_wait(3000)
attendence = driver.find_element_by_class_name("tiles")
attendence.click()


