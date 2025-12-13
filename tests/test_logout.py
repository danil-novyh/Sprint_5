import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import url_login_page, url_main_page
from locators import BUTTON_LOGOUT, LINK_PROFILE
# Добавлен класс
class TestLogout:
    """Тесты выхода из аккаунта."""

    def test_explicit_logout(self, driver, logged_in_user):
        """
        Проверяет выход из аккаунта по кнопке 'Выход' в Личном кабинете.
        logged_in_user обеспечивает вход перед тестом.
        """
        #1. Переход в Личный кабинет
        driver.get(url_main_page)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK_PROFILE)).click()
        
        #2. Клик по кнопке "Выход"
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGOUT))
        logout_button.click()
    
        #3. Проверка редиректа на страницу входа
        WebDriverWait(driver, 10).until(EC.url_to_be(url_login_page))
    
        assert driver.current_url == url_login_page, "Выход не привел на страницу входа"