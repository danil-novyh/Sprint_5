import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import url_login_page, url_main_page
from locators import (
    BUTTON_LOGOUT_PAGE,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_MAIN_LOGIN,
    ORDER_BUTTON,
    BUTTON_ACCOUNT,
    BUTTON_PAGE_LOGIN, 
    BUTTON_LOGIN
)
from data import Credential
# Добавлен класс
class TestLogout:
    """Тесты выхода из аккаунта."""

    def test_explicit_logout(self, driver):
        """
        Проверяет выход из аккаунта по кнопке 'Выход' в Личном кабинете.
        """
        # Заходим на главную страницу
        driver.get(url_main_page)
        # На главной странице кнопка "Вход в аккаунт"
        driver.find_element(*BUTTON_MAIN_LOGIN).click()
        driver.find_element(*INPUT_EMAIL).send_keys(Credential.email)
        driver.find_element(*INPUT_PASSWORD).send_keys(Credential.password)
        # Нажимаем на кнопку Войти
        driver.find_element(*BUTTON_LOGIN).click()
        # Ждем когда станет видима кнопка "Оформить заказ"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))
        # Нажимаем кнопку "Личный кабинет"
        driver.find_element(*BUTTON_ACCOUNT).click()
        # Ждем когда станет видима кнопка "Выход"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUTTON_LOGOUT_PAGE))
        driver.find_element(*BUTTON_LOGOUT_PAGE).click()
        # Проверяем перенаправление
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUTTON_PAGE_LOGIN))
        assert driver.current_url == url_login_page