from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# realizar login invalido
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("senhainvalida")
driver.find_element(By.ID, "login-button").click()

assert driver.find_element(By.XPATH, "//h3[@data-test='error' and text()='Epic sadface: Username and password do not match any user in this service']")
