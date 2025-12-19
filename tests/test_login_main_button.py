import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import url_main_page
from locators import (
    BUTTON_MAIN_LOGIN,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_LOGIN,
    ORDER_BUTTON
)
from data import Credential

#ИСПРАВЛЕНО: добавил класс
class TestLoginMainButton:
    """Тесты входа через главную страницу"""
    def test_login_via_main_button(self, driver):
        """Вход через кнопку «Войти в аккаунт» на главной."""
        driver.get(url_main_page)
        driver.find_element(*BUTTON_MAIN_LOGIN).click()
        driver.find_element(*INPUT_EMAIL).send_keys(Credential.email)
        driver.find_element(*INPUT_PASSWORD).send_keys(Credential.password)
        driver.find_element(*BUTTON_LOGIN).click()
        # Проверяем URL главной страницы
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))
        assert driver.find_element(*ORDER_BUTTON).is_displayed()