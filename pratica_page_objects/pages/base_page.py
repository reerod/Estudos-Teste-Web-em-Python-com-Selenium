import conftest


class BasePage:
    # chamar o metodo construtor e o conftest
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    # criar o metodo de verificação depois de fazer o metodo home_page
    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela."

    # metodo basico que encontra texto
    def valida_txt(self, locator):
        return self.encontrar_elemento(locator).text
