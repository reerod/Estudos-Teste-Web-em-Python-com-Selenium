# aqui revisarei alguns comandos aprendidos nas últimas 5 aulas do curso
# de automação de testes com selenium webdriver e python
import time

# passo 1: importar bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By

# passo 2: criar variavel browser para acessar o navegador web e fazer ajustes na janela de navegação
browser = webdriver.Chrome()
browser.maximize_window()

# passo 3: acessar url do site a ser testado
browser.get("https://www.facebook.com/")

# passo 4: mapear elementos para testar
# campo de digitar email/usuario e senha, utilizando variação entre método de mapeamento
# por XPTAH e ID
email = browser.find_element(By.XPATH, "//*[@id='email']")
password = browser.find_element(By.ID, "pass")
btn_login = browser.find_element(By.ID, "loginbutton")

# passo 5: preenchendo os campos mapeados no passo 4
# utilizando o comendo send_keys() para auto preenchimento
email.send_keys("renanrdepaula@outlook.com")
password.send_keys("R@199720123")

# passo 6: clicar no botão de login
btn_login.click()

browser.quit()
