from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

time.sleep(2)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()

assert driver.find_element(By.XPATH, "//span[contains(text(), 'Products')]").is_displayed()

time.sleep(2)
driver.find_element(By.ID, "item_4_title_link").click()
assert driver.find_element(By.ID, "back-to-products").is_displayed()
time.sleep(2)
driver.find_element(By.ID, "add-to-cart").click()

time.sleep(2)
driver.find_element(By.ID, "shopping_cart_container").click()

assert driver.find_element(By.ID, "item_4_title_link").is_displayed()

time.sleep(2)
driver.find_element(By.ID, "checkout").click()

time.sleep(2)
driver.find_element(By.ID, "first-name").send_keys("Geisson")
time.sleep(2)
driver.find_element(By.ID, "last-name").send_keys("Oliveira")
time.sleep(2)
driver.find_element(By.ID, "postal-code").send_keys("123456")

time.sleep(2)
driver.find_element(By.ID, "continue").click()
assert driver.find_element(By.XPATH, "//span[contains(text(), 'Checkout: Overview')]").is_displayed()

time.sleep(2)
driver.find_element(By.ID, "finish").click()

assert driver.find_element(By.XPATH, "//span[contains(text(), 'Checkout: Complete!')]").is_displayed()

driver.quit()