import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import url_main_page
from locators import (
    LINK_REGISTER,
    INPUT_NAME,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_REGISTER,
    ERROR_INPUT
)
from data import Credential

class TestRegistrationIncorrectPassword:
    """Тесты регистрации пользователя."""

    def test_registration_short_password(self, driver):
        """Ошибка при пароле менее 6 символов."""
        driver.get(url_main_page)
    
        #1. Переход на страницу регистрации
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK_REGISTER)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_NAME))
        #2. Ввод данных с коротким паролем
        driver.find_element(*INPUT_NAME).send_keys("Тест Пользователь")
        driver.find_element(*INPUT_EMAIL).send_keys(Credential.email)
        driver.find_element(*INPUT_PASSWORD).send_keys("12345")

        #3. Клик по кнопке "Зарегистрироваться"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_REGISTER)).click()

        #4. Проверка появления сообщения об ошибке
        error_msg = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ERROR_INPUT))
    
        assert error_msg.text == "Некорректный пароль", "Сообщение о некорректном пароле не отобразилось или неверно"