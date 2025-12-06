import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import LOGIN_PAGE, BASE_URL
from locators import BUTTON_LOGOUT, LINK_PROFILE

# !!!!logout @теперь@ вызывается явно внутри теста
def test_explicit_logout(driver, wait, logged_in_user):
    """
    Проверяет явный выход из аккаунта по кнопке 'Выход' в Личном кабинете.
    logged_in_user обеспечивает вход перед тестом.
    """
    # 1. Переход в Личный кабинет
    driver.get(BASE_URL)
    wait.until(EC.element_to_be_clickable(LINK_PROFILE)).click()
    
    # 2. Клик по кнопке "Выход"
    wait.until(EC.url_contains("/account/profile"))
    logout_button = wait.until(EC.element_to_be_clickable(BUTTON_LOGOUT))
    logout_button.click()
    
    # 3. Проверка редиректа на страницу входа
    wait.until(EC.url_to_be(LOGIN_PAGE))
    
    assert driver.current_url == LOGIN_PAGE, "Выход не привел на страницу входа"