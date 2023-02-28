#script 2

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
driver.find_element(By.NAME, "UserFirstName").send_keys("Dhaval")
driver.find_element(By.NAME, "UserLastName").send_keys("Khatri")
driver.find_element(By.NAME, "UserEmail").send_keys("Dhaval@gmail.com")

select_job = Select(driver.find_element(By.NAME, "UserTitle"))
select_job.select_by_value("IT_Manager_AP")

select_employee = Select(driver.find_element(By.NAME, "CompanyEmployees"))
select_employee.select_by_value("250")

driver.find_element(By.CLASS_NAME, "checkbox-ui").click()
driver.find_element(By.NAME, "start my free trial").click()

time.sleep(5)
#form/signup/freetrial-sales/")driver.find_element(By.NAME, "UserFirstName").send_keys("padmakshi")driver.find_element(By.NAME, "UserLastName").send_keys("Jain")driver.find_element(By.NAME, "UserEmail").send_keys("padmakshi@gmail.com")select_job = Select(driver.find_element(By.NAME, "UserTitle"))select_job.select_by_value("IT_Manager_AP")select_employee = Select(driver.find_element(By.NAME, "CompanyEmployees"))select_employee.select_by_value("250")driver.find_element(By.CLASS_NAME, "checkbox-ui").click()driver.find_element(By.NAME, "start my free trial").click()time.sleep(5) import timefrom selenium import webdriverfrom selenium.webdriver.common.by import Byfrom selenium.webdriver.support.select import Selectdriver = webdriver.Chrome()driver.maximize_window()driver.implicitly_wait(30)driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")driver.find_element(By.NAME, "UserFirstName").send_keys("padmakshi")driver.find_element(By.NAME, "UserLastName").send_keys("Jain")driver.find_element(By.NAME, "UserEmail").send_keys("padmakshi@gmail.com")select_job = Select(driver.find_element(By.NAME, "UserTitle"))select_job.select_by_value("IT_Manager_AP")select_employee = Select(driver.find_element(By.NAME, "CompanyEmployees"))select_employee.select_by_value("250")driver.find_element(By.CLASS_NAM, "checkbox-ui").click()driver.find_element(By.NAME, "start my free trial").click()time.sleep(5) 