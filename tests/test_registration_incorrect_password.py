import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import url_main_page
from locators import (
    LINK_REGISTER,
    INPUT_NAME,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_REGISTER,
    ERROR_INPUT
)

def test_registration_short_password(driver, wait, user_data):
    """Ошибка при пароле менее 6 символов."""
    driver.get(url_main_page)
    
    #1. Переход на страницу регистрации
    wait.until(EC.element_to_be_clickable(LINK_REGISTER)).click()

    #2. Ввод данных с коротким паролем
    driver.find_element(*INPUT_NAME).send_keys("Тест Пользователь")
    driver.find_element(*INPUT_EMAIL).send_keys(user_data["email"])
    driver.find_element(*INPUT_PASSWORD).send_keys("12345")

    #3. Клик по кнопке "Зарегистрироваться"
    wait.until(EC.element_to_be_clickable(BUTTON_REGISTER)).click()

    #4. Проверка появления сообщения об ошибке
    error_msg = wait.until(EC.visibility_of_element_located(ERROR_INPUT))
    
    assert error_msg.text == "Некорректный пароль", "Сообщение о некорректном пароле не отобразилось или неверно"