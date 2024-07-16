import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://demo.applitools.com/")

# sessão de mapeamento dos elementos
username = browser.find_element(By.ID, "username")
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@type = 'checkbox']")

# is_displayed()
print("Teste prático com is_displayed()")
print(username.is_displayed())
assert username.is_displayed()
print(checkbox_remember_me.is_displayed())
assert checkbox_remember_me.is_displayed()

# is_enabled()
print("Teste prático com is_enabled()")
print(username.is_enabled())
assert username.is_enabled()
print(checkbox_remember_me.is_enabled())
assert checkbox_remember_me.is_enabled()

# is_selected()
print("Teste prático com is_selected() retornando False")
print(checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected()


# criando um click no checkbox
checkbox_remember_me.click()

print("Teste prático com is_selected() retornando True")
print(checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected()

browser.quit()
