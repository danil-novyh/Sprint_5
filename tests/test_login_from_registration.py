import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import url_main_page, url_register_page
from locators import (
    LINK_REGISTER,
    LINK_ALREADY_ACCOUNT,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_LOGIN,
    MENU_PROFILE
)
from data import Credential

@pytest.fixture
def user_data():
    return {
        "email": Credential.email,
        "password": Credential.password
    }

class TestLoginFromRegistration:
    def test_login_from_registration(driver, wait, user_data):
        """Вход из формы регистрации (переход к форме входа)."""
        
        driver.get(url_main_page)
        #1. Переход на страницу регистрации
        wait.until(EC.element_to_be_clickable(LINK_REGISTER)).click()

        #2. Переход на страницу входа по ссылке "Уже есть аккаунт?"
        wait.until(EC.element_to_be_clickable(LINK_ALREADY_ACCOUNT)).click()
        
        wait.until(EC.url_contains("/login"))
    
        #3. Ввод данных
        driver.find_element(*INPUT_EMAIL).send_keys(user_data["email"])
        driver.find_element(*INPUT_PASSWORD).send_keys(user_data["password"])
        
        #4. Клик по кнопке "Войти"
        wait.until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()
        
        #5. Проверка успешного входа
        wait.until(EC.url_to_be(url_main_page + '/'))
        profile_menu = wait.until(EC.visibility_of_element_located(MENU_PROFILE))
        
        assert profile_menu.is_displayed(), "Меню 'Профиль' не отображается после входа"