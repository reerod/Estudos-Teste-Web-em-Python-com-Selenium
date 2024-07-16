# O assert sempre verifica se o retorno da condição é True
assert True

# assert numbers
# num_esperado = 1
# num_obtido = 2
#
# assert num_esperado != num_obtido, f"Esperado {num_esperado}. Obtido {num_obtido}"

# assert text
# text_esperado = "Selenium Webdriver"
# text_obtido = "SELENIUM WEBDRIVER"
#
# assert text_esperado.lower() == text_obtido.lower()

# assert text in string
text_esperado = "Selenium"
text_obtido = "selenium webdriver"
assert text_esperado.lower() in text_obtido.lower(), f"O texto esperado: {text_esperado} não corresponde ao texto obtido: {text_obtido}"

# assert is_displayed/is_enable/is_selected
