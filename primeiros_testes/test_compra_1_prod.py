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

# clicar no item escolhido
driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Fleece Jacket']").click()

# clicar no botao de adicionar o item ao carrinho
driver.find_element(By.ID, "add-to-cart").click()

# clicar no carrinho
driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()
# verificar item dentro do carrinho
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Fleece Jacket']")

# clicar no botao checkout
driver.find_element(By.ID, "checkout").click()

# preencher informações de checkout
driver.find_element(By.ID, "first-name").send_keys("primeiro_nome")
driver.find_element(By.ID, "last-name").send_keys("ultimo_nome")
driver.find_element(By.ID, "postal-code").send_keys("606060")
driver.find_element(By.ID, "continue").click()

# clicar em finalizar compra e verificar mensagem de compra realizada com sucesso
driver.find_element(By.ID, "finish").click()
assert driver.find_element(By.CLASS_NAME, "complete-header")
