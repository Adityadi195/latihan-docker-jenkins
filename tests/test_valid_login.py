import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(50)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

time.sleep(2)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()

assert driver.find_element(By.XPATH, "//span[contains(text(), 'Products')]").is_displayed()

driver.quit()