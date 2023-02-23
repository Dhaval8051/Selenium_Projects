import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
#ele=driver.find_element(By.ID,"email")
#ele.send_keys("hello123444@gmail.com")
#driver.find_element(By.ID,"email").send_keys("dhavalk01@yahoo.com")  //user id for login
#driver.find_element(By.ID,"pass").send_keys("123456789")             //user id for pwd
#driver.find_element(By.NAME,"login").click()
#driver.find_element(By.LINK_TEXT,"Create new account").click()
#time.sleep(5)
#driver.find_element(By.NAME,"firstname").send_keys("Dhaval")
#driver.find_element(By.NAME, "lastname").send_keys("khatri")
#driver.implicitly_wait(10)
#driver.find_element(By.NAME, "reg_passwd__").send_keys("helloworld")
#driver.implicitly_wait(10)
#driver.find_element(By.NAME,"lastname").send_keys("Dh")
#time.sleep(5)

driver.find_element(By.LINK_TEXT, "Create new account").click()
time.sleep(5)
driver.find_element(By.NAME, "firstname").send_keys("Dhaval")
time.sleep(5)
driver.find_element(By.NAME,"lastname").send_keys("Khatri")
time.sleep(5)
driver.find_element(By.NAME,"reg_email__").send_keys("abc@gmail.com")
time.sleep(5)
driver.find_element(By.ID,"password_step_input").send_keys("welcome@123")
time.sleep(5)
