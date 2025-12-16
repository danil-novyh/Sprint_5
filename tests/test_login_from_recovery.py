import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import url_main_page, url_login_page, url_forgot_password
from data import Credential
from locators import (
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_LOGIN_REG,
    BUTTON_LOGIN_PAGE,
    ORDER_BUTTON
)

class TestLoginFromRecovery:
    """Тесты для проверки возврата из формы восстановления пароля в форму входа."""

    def test_return_to_login_from_recovery(self, driver):
        """Проверяет переход из восстановления пароля обратно на страницу входа."""

        #1. Открыть страницу восстановления пароля
        driver.get(url_forgot_password)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN_REG)).click()

        #2. Убедиться, что перешли на страницу входа
        WebDriverWait(driver, 10).until(EC.url_to_be(url_login_page))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_EMAIL))

        #3. Ввести учетные данные
        driver.find_element(*INPUT_EMAIL).send_keys(Credential.email)
        driver.find_element(*INPUT_PASSWORD).send_keys(Credential.password)

        #4. Нажать "Войти"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN_PAGE)).click()

        #5. Проверить успешный вход
        WebDriverWait(driver, 10).until(EC.url_to_be(url_main_page))
        order_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ORDER_BUTTON))

        #6. Явный assert
        assert driver.current_url == url_main_page, "Не произошёл переход на главную страницу"
        assert order_button.text == "Оформить заказ", "Текст кнопки 'Оформить заказ' не совпадает"