from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# valid user.
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# wrong password.
driver.find_element(By.ID, "password").send_keys("secret_s")
driver.find_element(By.ID, "login-button").click()

assert driver.find_element(By.XPATH, "//*[contains(text(), 'Epic sadface: Username and password do not match any user in this service')]").is_displayed()

driver.quit()