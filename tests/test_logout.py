import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import url_login_page, url_main_page
from locators import BUTTON_LOGOUT, LINK_PROFILE

def test_explicit_logout(driver, wait, logged_in_user):
    """
    Проверяет выход из аккаунта по кнопке 'Выход' в Личном кабинете.
    logged_in_user обеспечивает вход перед тестом.
    """
    #1. Переход в Личный кабинет
    driver.get(url_main_page)
    wait.until(EC.element_to_be_clickable(LINK_PROFILE)).click()
    
    #2. Клик по кнопке "Выход"
    wait.until(EC.url_contains("/account/profile"))
    logout_button = wait.until(EC.element_to_be_clickable(BUTTON_LOGOUT))
    logout_button.click()
    
    #3. Проверка редиректа на страницу входа
    wait.until(EC.url_to_be(url_login_page))
    
    assert driver.current_url == url_login_page, "Выход не привел на страницу входа"