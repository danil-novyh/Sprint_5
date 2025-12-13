import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import url_main_page
from locators import (
    LINK_PROFILE,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_LOGIN,
    MENU_PROFILE
)
from data import Credential
#Добавлен класс
class TestLoginViaAccount:
    """Тесты входа через ссылку 'Личный кабинет' на главной странице."""

    def _perform_login(self, driver, email, password):
        """Выполняет стандартный вход через форму."""
        driver.find_element(*INPUT_EMAIL).send_keys(email)
        driver.find_element(*INPUT_PASSWORD).send_keys(password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()

    def test_login_via_profile(self, driver):
        """Вход через «Личный кабинет»."""
        driver.get(url_main_page)
    
        #1. Клик по ссылке "Личный кабинет"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK_PROFILE)).click()
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_EMAIL))
        
        #2. Ввод данных
        #driver.find_element(*INPUT_EMAIL).send_keys(Credential.email)
        #driver.find_element(*INPUT_PASSWORD).send_keys(Credential.password)
        #3. Клик по кнопке "Войти"
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()
        #2-3. Ввод данных и вход
        self._perform_login(driver, Credential.email, Credential.password)

        #4. Проверка успешного входа
        WebDriverWait(driver, 10).until(EC.url_to_be(url_main_page + '/'))
        profile_menu = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MENU_PROFILE))
    
        assert profile_menu.is_displayed(), "Меню 'Профиль' не отображается после входа"