from django.test import TestCase

from selenium import webdriver
import time

try:
    link = 'http://127.0.0.1:8000/flyfe/'
    browser = webdriver.Chrome()
    browser.get(link)

    find_button = browser.find_element_by_id('main-button-start_page')
    find_button.click()

    time.sleep(5)

    text = browser.find_element_by_id('login-text')
    login_text = text.text

    assert "Login" == login_text

finally:
    time.sleep(5)
    browser.quit()

