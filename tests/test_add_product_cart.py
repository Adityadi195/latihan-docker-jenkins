from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# login.

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# succses login.
assert driver.find_element(By.XPATH, "//span[contains(text(), 'Products')]").is_displayed()

# add product in cart.
driver.find_element(By.ID, "item_4_title_link").click()
assert driver.find_element(By.ID, "back-to-products").is_displayed()
driver.find_element(By.ID, "add-to-cart").click()

# go to cart.
driver.find_element(By.ID, "shopping_cart_container").click()

# verify products.
assert driver.find_element(By.ID, "item_4_title_link").is_displayed()

# continue shopping.
driver.find_element(By.ID, "continue-shopping").click()

# add product in cart.
driver.find_element(By.ID, "item_0_title_link").click()
assert driver.find_element(By.ID, "back-to-products").is_displayed()
driver.find_element(By.ID, "add-to-cart").click()

# go to cart.
driver.find_element(By.ID, "shopping_cart_container").click()

# verify products.
assert driver.find_element(By.ID, "item_4_title_link").is_displayed()
assert driver.find_element(By.ID, "item_0_title_link").is_displayed()

driver.quit()