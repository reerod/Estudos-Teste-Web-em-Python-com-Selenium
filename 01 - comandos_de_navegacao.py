from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()

# get()
browser.get('https://google.com/') # abrir navegador
sleep(2)

# maximize_window()
browser.maximize_window() # maximiza a tela
browser.minimize_window()
browser.maximize_window()
sleep(2)

# refresh()
browser.refresh() # atualiza a página do navegador
sleep(2)

# get()
browser.get('https://saucedemo.com/') # abrir navegador
sleep(2)

# back()
browser.back() # retorna para a página anterior do navegador
sleep(2)

# forward()
browser.forward() # retorna para a pagina do site pesquisado
sleep(2)

# # switch_to.new_window()
# browser.switch_to.new_window("tab")
# sleep(2)
#
# # close()
# browser.close() # fecha a aba que estiver ativa
# sleep(2)

# switch_to.new_window()
browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
sleep(2)

# quit()
browser.quit() # finaliza toda a operação realizada no navegador

