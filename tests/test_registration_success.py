import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import url_main_page, url_login_page
from locators import (
    LINK_REGISTER,
    INPUT_NAME,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_REGISTER
)

def test_registration_success(driver, wait, user_data):
    """Успешная регистрация с корректными данными."""
    driver.get(url_main_page)
    
    #1. Переход на страницу регистрации
    wait.until(EC.element_to_be_clickable(LINK_REGISTER)).click()

    #2. Ввод корректных данных
    driver.find_element(*INPUT_NAME).send_keys("Тест Пользователь")
    driver.find_element(*INPUT_EMAIL).send_keys(user_data["email"])
    driver.find_element(*INPUT_PASSWORD).send_keys(user_data["password"])

    #3. Клик по кнопке "Зарегистрироваться"
    wait.until(EC.element_to_be_clickable(BUTTON_REGISTER)).click()

    #4. Перенаправление на страницу входа
    wait.until(EC.url_to_be(url_login_page))
    
    assert driver.current_url == url_login_page, "Успешная регистрация не привела на страницу входа"