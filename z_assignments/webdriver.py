import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")
#driver.switch_to.frame(driver.find_element(By.XPATH,"/frame[@name='login_page']"))
#driver.find_element(By.NAME."fldLoginuserId").send_keys("test123")

driver.find_element(By.NAME, "fldLoginUserId").send_keys("1234567890")
driver.find_element(By.XPATH, "//a[contains(text(),'CONTINUE')]").click(
driver.find_element(By.XPATH, "//a[contains(text(),'CONTINUE')]").click()

time.sleep(5)
driver.quit()
