import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT01:
    def test_ct01_login(self):
        # instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage()

        # faz o login
        login_page.fazer_login("standard_user", "secret_sauce")

        # verificar elemento na tela
        home_page.verificar_login_com_sucesso()
