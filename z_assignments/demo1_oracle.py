import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get()
driver.get("https://www.oracle.com/in/database/")
driver.find_element(By.ID,"acctBtnLabel").click()
driver.find_element(By.LINK_TEXT,"Sign-In").click()
time.sleep(5)
print(driver.title)
actual_header=driver.find_element(By.XPATH,"//div[contains(tect(),'invalid') ]").text
print()
driver.find_element()
