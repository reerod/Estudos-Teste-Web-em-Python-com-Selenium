from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(12)

browser.maximize_window()
browser.get('https://chercher.tech/practice/frames')

# inserir texto e clicar no checkbox
iframe1 = browser.find_elements(By.ID, "frame1")
browser.switch_to.frame(iframe1)
browser.find_element(By.XPATH, "//*[@id='topic']/following-sibling::input").send_keys("iframe1")

# mapeando o elemento 3 que está inserido após o elemento 1
iframe3 = browser.find_element(By.ID, "frame3")
browser.switch_to.frame(iframe3)
checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']").click()

# retornando ao conteudo padrao da pag
browser.switch_to.default_content() # isso faz retornar ao conteudo padrao

iframe2 = browser.find_elements(By.ID, "frame2")
browser.switch_to.frame(iframe2)
dropdown_animals = Select(browser.find_element((By.XPATH, "//select[@id='animals']")))
dropdown_animals.select_by_value("babycat")


