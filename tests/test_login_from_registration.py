import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import url_main_page, url_register_page
from locators import (
    LINK_REGISTER,
    LINK_ALREADY_ACCOUNT,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_LOGIN,
    MENU_PROFILE
)
from data import Credential


class TestLoginFromRegistration:
    def _perform_login(self, driver, wait, email, password):
        """Вспомогательный метод для выполнения входа."""
        driver.find_element(*INPUT_EMAIL).send_keys(email)
        driver.find_element(*INPUT_PASSWORD).send_keys(password)
        wait.until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()

    def test_login_from_registration(self, driver, wait):
        """Вход из формы регистрации (переход к форме входа)."""
        
        driver.get(url_main_page)
        #1. Переход на страницу регистрации
        wait.until(EC.element_to_be_clickable(LINK_REGISTER)).click()

        #2. Переход на страницу входа по ссылке "Уже есть аккаунт?"
        wait.until(EC.element_to_be_clickable(LINK_ALREADY_ACCOUNT)).click()
        wait.until(EC.url_contains("/login"))
    
        #3. Ввод данных
        #driver.find_element(*INPUT_EMAIL).send_keys(Credential.email)
        #driver.find_element(*INPUT_PASSWORD).send_keys(Credential.password)
        #4. Клик по кнопке "Войти"
        #wait.until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()
        
        #3-4. Ввод данных и вход
        self._perform_login(driver, wait, Credential.email, Credential.password)

        #5. Проверка успешного входа
        wait.until(EC.url_to_be(url_main_page + '/'))
        profile_menu = wait.until(EC.visibility_of_element_located(MENU_PROFILE))
        
        assert profile_menu.is_displayed(), "Меню 'Профиль' не отображается после входа"