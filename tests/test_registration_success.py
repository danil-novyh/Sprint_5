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
from data import TestData
#Добавил класс. Актуализировал тест без user_data
#Создал и добавил TestData(генерацию данных) с data.py чтобы не падал тест,
#Используя хардкорженные данные
class TestRegistration:
    """Тесты регистрации пользователя."""

    def test_registration_success(self, driver, wait):
        """Успешная регистрация с корректными данными."""
        driver.get(url_main_page)
        
        #1. Переход на страницу регистрации
        wait.until(EC.element_to_be_clickable(LINK_REGISTER)).click()
        wait.until(EC.visibility_of_element_located(INPUT_NAME))

        name = "Тест Пользователь"
        email = TestData.generate_email()
        password = TestData.generate_password()

        #2. Ввод корректных сгенерированных данных
        driver.find_element(*INPUT_NAME).send_keys(name)
        driver.find_element(*INPUT_EMAIL).send_keys(email)
        driver.find_element(*INPUT_PASSWORD).send_keys(password)
    
        #3. Клик по кнопке "Зарегистрироваться"
        wait.until(EC.element_to_be_clickable(BUTTON_REGISTER)).click()
    
        #4. Перенаправление на страницу входа
        wait.until(EC.url_to_be(url_login_page))
        
        assert driver.current_url == url_login_page, "Успешная регистрация не привела на страницу входа"