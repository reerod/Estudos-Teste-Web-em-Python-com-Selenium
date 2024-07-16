import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
    #     organizando os locators
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_msg_login = (By.XPATH, "//*[@data-test='error']")

    # Definindo o metodo de login
    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

    # metodo para login invalido
    def verficar_msg_erro_login(self):
        self.verificar_se_elemento_existe(self.error_msg_login)

    #  metodo para verificar texto da msg de login invalido
    def verificar_texto_da_msg_de_login_invalido(self, txt_esperado):
        txt_encontrado = self.valida_txt(self.error_msg_login)
        assert txt_encontrado == txt_esperado, f"O texto encontrado foi '{txt_encontrado}', mas era esperado o texto '{txt_esperado}'"
