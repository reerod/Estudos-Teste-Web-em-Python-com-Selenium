from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(12)

browser.maximize_window()
browser.get('https://getbootstrap.com.br/docs/4.1/components/dropdowns/')

# inicializando inspeção do dropdown
btn_dropdown = Select(browser.find_element(By.ID, "dropdownMenuButton"))
btn_dropdown.select_by_visible_text("Alguma ação")

