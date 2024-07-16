import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# add produto ao carrinho
driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click() # clica no produto
driver.find_element(By.ID, "add-to-cart").click() # adiciona no carrinho

# verificar carrinho
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click() # verifica o carrinho com o produto

# retorna para a pag principal de produtos
driver.find_element(By.ID, "continue-shopping").click() # volta para a pag principal dos produtos
assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed() # confirma o retorno a pag principal dos produtos

# add mais outro produto ao carrinho
driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click() # clica no produto
driver.find_element(By.ID, "add-to-cart").click() # adiciona no carrinho
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click() # verifica o carrinho com o produto
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed() # confirma o produto no carrinho
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed() # confirma o produto no carrinho
