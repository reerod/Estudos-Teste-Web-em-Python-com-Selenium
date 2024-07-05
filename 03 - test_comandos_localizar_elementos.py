import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()

browser.get("https://www.saucedemo.com/")

# find_element(): encontra um elemento por vez. Usamos o código-fonte do website para encontrarmos esses elementos
# username = browser.find_element(By.ID, "user-name")
# password = browser.find_element(By.ID, "password")

# extra: comando send_keys(): serve para digitar alguma coisa
# username.send_keys("standard_user")
# password.send_keys("secret_sauce")

auth_fields = browser.find_elements(By.XPATH, "//*[@class = 'input_error form_input']")
print(auth_fields)
print(len(auth_fields))
assert len(auth_fields) == 2, "o numero de elementos encontrados é diferente do esperado" # msg caso dê erro

time.sleep(4)
browser.quit()

