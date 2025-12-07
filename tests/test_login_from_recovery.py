import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import url_login_page, url_forgot_password
from locators import LINK_RECOVERY, LINK_RETURN_TO_LOGIN, INPUT_EMAIL, BUTTON_LOGIN


class TestLoginFromRecovery:
    """Тесты для проверки возврата из формы восстановления пароля в форму входа."""

    def test_return_to_login_from_recovery(self, driver, wait):
        """Проверяет переход из восстановления пароля обратно на страницу входа."""
        driver.get(url_login_page)

        recovery_link = wait.until(EC.element_to_be_clickable(LINK_RECOVERY))
        recovery_link.click()
        #Ожидаем страницу восстановления пароля
        wait.until(EC.url_to_be(url_forgot_password))
        wait.until(EC.visibility_of_element_located(LINK_RETURN_TO_LOGIN))

        return_link = wait.until(EC.element_to_be_clickable(LINK_RETURN_TO_LOGIN))
        return_link.click()

        wait.until(EC.url_to_be(url_login_page))

        email_input = wait.until(EC.visibility_of_element_located(INPUT_EMAIL))
        assert email_input.is_displayed(), "Поле email не отображается"

        #Завершение синтаксиса и добавление assert на видимость кнопки
        login_button = wait.until(EC.visibility_of_element_located(BUTTON_LOGIN))
        assert login_button.is_displayed(), "Кнопка 'Войти' не отображается"