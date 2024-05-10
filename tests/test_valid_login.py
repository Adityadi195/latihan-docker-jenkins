import time
from selenium import webdriver
from selenium.webdriver.common.by import By

hub_url = "http://172.17.0.3:4444"

capabilities = {
    "browserName": "chrome"
}

driver = webdriver.Remote(
    command_executor=hub_url,
    options=webdriver.ChromeOptions(),
)

time.sleep(5)

driver.get("https://www.saucedemo.com/")

time.sleep(5)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(5)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(5)
driver.find_element(By.ID, "login-button").click()

assert driver.find_element(By.XPATH, "//span[contains(text(), 'Products')]").is_displayed()

driver.quit()
