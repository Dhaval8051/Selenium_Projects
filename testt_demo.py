import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


driver = webdriver.Chrome()
driver.get('http://demo.openemr.io/b/openemr/')
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"#authUser").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"#clearPass").send_keys("pass")

select_lang=Select(driver.find_element(By.XPATH,"//select[@name='languageChoice']"))
select_lang.select_by_visible_text("English (Indian)")

driver.find_element(By.CSS_SELECTOR,"#login-button").click()

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@name='pat']"))
driver.find_element(By.ID,"form_fname").send_keys("john")
driver.find_element(By.XPATH,"//input[@id='form_lname']").send_keys("wick")

select_gender=Select(driver.find_element(By.XPATH,"//select[@id='form_sex']"))
select_gender.select_by_visible_text("Male")

driver.find_element(By.XPATH,"//input[@id='form_DOB']").send_keys("2023-03-01")

driver.find_element(By.ID, "create").click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()
driver.switch_to.default_content()