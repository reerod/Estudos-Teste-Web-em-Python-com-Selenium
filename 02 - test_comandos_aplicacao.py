from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

browser.get('https://saucedemo.com/') # .get(): abre um navegador ou aplicação da web

# aplicação prática do title
print(f"o título da página é {browser.title}") # mostra o título de uma página web

# aplicação prática do current_url
print(f"a URL da página é {browser.current_url}") # mostra a URL da página

# aplicação prática do page_source
print(f"o código-fonte da página é {browser.page_source}") # mostra o código-fonte da página
