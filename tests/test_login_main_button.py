import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import url_main_page
from locators import (
    BUTTON_MAIN_LOGIN,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_LOGIN,
    MENU_PROFILE,
    ORDER_BUTTON
)
from data import Credential
from helpers import perform_login

#ИСПРАВЛЕНО: добавил класс
class TestLoginMainButton:
    """Тесты входа через главную страницу"""
#Вынес вспомогательный метод в отдельный модуль (helpers.py)
    def test_login_via_main_button(self, driver):
        """Вход через кнопку «Войти в аккаунт» на главной."""
        driver.get(url_main_page)
        
        #1. Клик по кнопке "Войти в аккаунт"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_MAIN_LOGIN)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_EMAIL))

        #2. Вход
        perform_login(driver, Credential.email, Credential.password)

        #3. Проверка успешного входа
        WebDriverWait(driver, 10).until(EC.url_to_be(url_main_page + '/'))
        profile_menu = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MENU_PROFILE))
    
        assert profile_menu.is_displayed(), "Меню 'Профиль' не отображается после входа"