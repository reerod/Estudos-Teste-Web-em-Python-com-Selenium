import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.loginInvalido
class TestCT02:
    def test_ct02_login_invalido(self):
        msg_esperada = "Epic sadface: Username and password do not match any user in this service"

        # Login
        # Instancia os objetos a serem usados no teste
        login_page = LoginPage()

        # Faz o login
        login_page.fazer_login("standard_user", "senha_incorreta")

        # Verifica se o login nao foi realizado e se a mensagem de erro apareceu
        login_page.verficar_msg_erro_login()

        login_page.verificar_texto_da_msg_de_login_invalido(msg_esperada)
