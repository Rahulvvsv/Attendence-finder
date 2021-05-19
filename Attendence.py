# Webdriver For Firefox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://mgit.winnou.net/")
elem = driver.find_element_by_name('username')
elem1 = driver.find_element_by_name('passwd')
elem.send_keys('19261A05B9_p' )
elem1.send_keys('12345',Keys.RETURN )
driver.implicitly_wait(3000)
attendence = driver.find_element_by_class_name("tiles")
attendence.click()
# driver.implicitly_wait(3000)
# value = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/table[3]/tbody/tr[11]/th[8]")
# driver.implicitly_wait(3000)
# print(value.text)

