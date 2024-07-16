comandos de navegação:

get()
maximize_window()
refresh()
back()
forward()
close()
quit()

===================================
comandos da aplicação:

title
current_url
page_source

===================================
comando para localizar elementos:

find_element()
find_elements()

===================================
comandos para dropdown
# começamos importanto a função Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
# depois que ja tivermos as funções necessarias de mapeamento
# faremos as devidas interações com o dropdown
# usaremos o exemplo de um dropdown chamado products e animals
dropdown_products = Select("aqui chamamos nossa função para mapeamento de elementos, p. ex. By.XPATH, //input[@class='nome_da_classe'")
dropdown_products.select_by_visible_text("E aqui passamos o nome da opção que queremos selecionar do dropdown ")
dropdown_products.select_by_value("passamos o valor do atribute value")
dropdown_products.select_by_index("passamos o index da opção que desejamos marcar")
# a outra maneira de usarmos o by_visible_text é quando desejamos testar um dropdown de multiplas opções
# basta chamarmos ele o numero de vezes que desejamos marcar as opções no dropdown
dropdown_products.select_by_visible_text("opçao1")
dropdown_products.select_by_visible_text("opçao2")
dropdown_products.select_by_visible_text("opçao3")
