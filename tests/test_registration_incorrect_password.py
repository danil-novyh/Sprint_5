import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import url_main_page
from locators import (
    REGISTER_LINK,
    INPUT_NAME,
    INPUT_EMAIL,
    BUTTON_MAIN_LOGIN,
    INPUT_PASSWORD,
    BUTTON_REG,
    BUTTON_PAGE_LOGIN,
    HEADING_REGISTER,
    ERROR_INPUT
)
from data import Credential

class TestRegistrationIncorrectPassword:
    """Тесты регистрации пользователя."""

    def test_registration_short_password(self, driver):
        """Ошибка при пароле менее 6 символов."""
        driver.get(url_main_page)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_MAIN_LOGIN)).click()
        # Ждём загрузки страницы входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUTTON_PAGE_LOGIN))
        #1. Переход на страницу регистрации
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(REGISTER_LINK)).click()
        # Ждем загрузки страницы регистрации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HEADING_REGISTER))
        #2. Ввод данных с коротким паролем
        # Ввод имени (валидное)
        name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(INPUT_NAME)
        )
        name_input.clear()
        name_input.send_keys("Тест Пользователь")
        email_input = driver.find_element(*INPUT_EMAIL)
        email_input.clear()
        email_input.send_keys(Credential.email)
        password_input = driver.find_element(*INPUT_PASSWORD)
        password_input.clear()
        password_input.send_keys("12345")
        #3. Клик по кнопке "Зарегистрироваться"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_REG)).click()
        #4. Проверка появления сообщения об ошибке
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ERROR_INPUT), message="Сообщение об ошибке не появилось")
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        assert error_message.text == "Некорректный пароль", (
        f"Ожидалось сообщение 'Некорректный пароль',"
        f"но получено:'{error_message.text}'"
        )
        # URL не изменился (остались на странице регистрации)
        current_url = driver.current_url
        assert "/register" in current_url, (
            f"После ошибки валидации ожидалось остаться на странице регистрации,"
            f"но текущий URL: {current_url}"
        )