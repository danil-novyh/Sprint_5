import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import url_register_page
from locators import (
    INPUT_EMAIL,
    BUTTON_REG_LOGIN,
    INPUT_PASSWORD,
    ORDER_BUTTON,
    BUTTON_LOGIN,
)
from data import Credential

class TestLoginFromRegistration:

    def test_login_from_registration(self, driver):
        """Вход из формы регистрации (переход к форме входа)."""
        #Исправлено: переход на страницу регистрации
        #1. Ожидание загрузки страницы регистрации
        driver.get(url_register_page)
        #2. Переход по ссылке "Войти" со страницы регистрации
        driver.find_element(*BUTTON_REG_LOGIN).click()
        #3. Ввод данных
        driver.find_element(*INPUT_EMAIL).send_keys(Credential.email)
        driver.find_element(*INPUT_PASSWORD).send_keys(Credential.password)
        #4. Клик по кнопке "Войти"
        driver.find_element(*BUTTON_LOGIN).click()
        #5. Проверка успешного входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))
        assert driver.find_element(*ORDER_BUTTON).is_displayed()