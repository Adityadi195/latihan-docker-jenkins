import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# URL untuk Selenium Grid Hub
hub_url = "http://172.17.0.5:4444"

# Konfigurasi capability untuk browser yang akan dijalankan
capabilities = {
    "browserName": "chrome"
}

# Inisialisasi WebDriver dengan menggunakan URL Selenium Grid Hub dan capability
driver = webdriver.Remote(
    command_executor=hub_url,
    options=webdriver.ChromeOptions(), # options argument is mandatory
)

# Jeda untuk memberikan waktu kepada Selenium Grid Node untuk menjalankan browser
time.sleep(5)

driver.get("https://www.saucedemo.com/")

time.sleep(2)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()

assert driver.find_element(By.XPATH, "//span[contains(text(), 'Products')]").is_displayed()

driver.quit()
