import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import url_main_page
from locators import (
    LINK_PROFILE,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_LOGIN,
    MENU_PROFILE
)

def test_login_via_profile(driver, wait, user_data):
    """Вход через «Личный кабинет»."""
    driver.get(url_main_page)
    
    #1. Клик по ссылке "Личный кабинет"
    wait.until(EC.element_to_be_clickable(LINK_PROFILE)).click()

    #2. Ввод данных
    driver.find_element(*INPUT_EMAIL).send_keys(user_data["email"])
    driver.find_element(*INPUT_PASSWORD).send_keys(user_data["password"])
    
    #3. Клик по кнопке "Войти"
    wait.until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()

    #4. Проверка успешного входа
    wait.until(EC.url_to_be(url_main_page + '/'))
    profile_menu = wait.until(EC.visibility_of_element_located(MENU_PROFILE))
    
    assert profile_menu.is_displayed(), "Меню 'Профиль' не отображается после входа"