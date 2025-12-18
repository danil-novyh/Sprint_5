import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import url_main_page, url_login_page
from locators import (
    REGISTER_LINK,
    HEADING_REGISTER,
    BUTTON_PAGE_LOGIN,
    BUTTON_MAIN_LOGIN,
    INPUT_NAME,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_REG
)
from data import TestData
#Добавил класс. Актуализировал тест без user_data
#Создал и добавил TestData(генерацию данных) с data.py чтобы не падал тест,
#Используя хардкорженные данные
class TestRegistrationSuccess:
    """Тесты регистрации пользователя."""

    def test_registration_success(self, driver):
        """Успешная регистрация с корректными данными."""
        driver.get(url_main_page)
        
        #1. Переход на страницу регистрации
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_MAIN_LOGIN)).click()
        # Ждём загрузки страницы входа (проверка по заголовку)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUTTON_PAGE_LOGIN))
        # Теперь кликаем ссылку "Зарегистрироваться" (она есть на странице логина)        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(REGISTER_LINK)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HEADING_REGISTER))

        name = "Тест Пользователь"
        email = TestData.generate_email()
        password = TestData.generate_password()

        #2. Ввод корректных сгенерированных данных
        # Ввод имени
        name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_NAME))
        name_input.clear()
        name_input.send_keys(name)
        # Ввод email
        email_input = driver.find_element(*INPUT_EMAIL)
        email_input.clear()
        email_input.send_keys(email)
        # Ввод пароля
        password_input = driver.find_element(*INPUT_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)
    
        #3. Клик по кнопке "Зарегистрироваться"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_REG)).click()

        #4. Перенаправление на страницу входа
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))  
        
        # Проверяем точное совпадение URL
        current_url = driver.current_url.rstrip('/')  # Убираем слеш в конце
        expected_url = url_login_page.rstrip('/')
        assert current_url == expected_url, (
            f"После успешной регистрации ожидался переход на {expected_url}, "
            f"но получен {current_url}"
        )
        # Дополнительная проверка: заголовок страницы входа виден
        login_heading = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(BUTTON_PAGE_LOGIN) #!!!
        )
        assert login_heading.is_displayed(), "Заголовок страницы входа не отображается"
