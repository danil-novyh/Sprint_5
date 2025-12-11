import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import url_main_page
from locators import (
    BUTTON_MAIN_LOGIN,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_LOGIN,
    MENU_PROFILE
)
from data import Credential

#ИСПРАВЛЕНО: добавил класс
class TestLoginMainButton:
    """Тесты входа через главную страницу"""

    #Добавлен метод для вывод логики логина в один метод
    def test_perform_login(self, driver, wait, email, password):
        """Вспомогательный метод для выполнения входа."""
        driver.find_element(*INPUT_EMAIL).send_keys(email)
        driver.find_element(*INPUT_PASSWORD).send_keys(password)
        wait.until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()

    def test_login_via_main_button(self, driver, wait):
        """Вход через кнопку «Войти в аккаунт» на главной."""
        driver.get(url_main_page)
        
        #1. Клик по кнопке "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(BUTTON_MAIN_LOGIN)).click()
        wait.until(EC.visibility_of_element_located(INPUT_EMAIL))

        #Ввод данных
        #driver.find_element(*INPUT_EMAIL).send_keys(Credential.email)
        #driver.find_element(*INPUT_PASSWORD).send_keys(Credential.password)
        #Клик по кнопке "Войти"
        #wait.until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()
        #2. Вход
        self._perform_login(driver, wait, Credential.email, Credential.password)

        #3. Проверка успешного входа
        wait.until(EC.url_to_be(url_main_page + '/'))
        profile_menu = wait.until(EC.visibility_of_element_located(MENU_PROFILE))
    
        assert profile_menu.is_displayed(), "Меню 'Профиль' не отображается после входа"