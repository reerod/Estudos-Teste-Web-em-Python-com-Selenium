import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://chercher.tech/practice/explicit-wait")
wait = WebDriverWait(browser, 30)

# Alert is present
# browser.find_element(By.ID, "alert").click()
# wait.until(ec.alert_is_present())

# text_to_be_present_in_element
# browser.find_element(By.ID, "populate-text").click()
# wait.until(ec.text_to_be_present_in_element((By.XPATH, "//*[@id='h2']"), "Selenium Webdriver"))
# h2 = browser.find_element(By.XPATH, "//*[@id='h2']").text
# assert h2 == "Selenium Webdriver"

# element_to_be_clickable
# browser.find_element(By.ID, "display-other-button").click()
# wait.until(ec.element_to_be_clickable((By.ID, "hidden")))

# browser.find_element(By.ID, "enable-button").click()
# wait.until(ec.element_to_be_clickable((By.ID, "disable")))

# element_to_be_selected
checkbox = browser.find_element(By.ID, "ch")
browser.find_element(By.ID, "checkbox").click()
wait.until(ec.element_to_be_selected(checkbox))


time.sleep(2)
