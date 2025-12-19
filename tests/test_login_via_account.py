import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import url_main_page
from locators import (
    LINK_PROFILE,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_LOGIN,
    MENU_PROFILE
)
from data import Credential
#Добавлен класс
class TestLoginViaAccount:
    """Тесты входа через ссылку 'Личный кабинет' на главной странице."""

    def test_login_via_profile(self, driver):
        """Вход через «Личный кабинет»."""
        driver.get(url_main_page)
        # Ожидание загрузки страницы и элемента
        profile_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located(LINK_PROFILE))
        # Прокрутка к элементу (на случай, если он вне видимости)
        driver.execute_script("arguments[0].scrollIntoView(true);", profile_link)
        #1. Клик по ссылке "Личный кабинет" и ожидание формы входа
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK_PROFILE)).click()
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_EMAIL))
        #2. Ввод данных
        email_input.clear()
        email_input.send_keys(Credential.email)
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_PASSWORD))
        password_input.clear()
        password_input.send_keys(Credential.password)
        #3. Клик по кнопке "Войти"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()
        #4. Проверка успешного входа
        profile_menu = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MENU_PROFILE))
        WebDriverWait(driver, 10).until(lambda d: d.current_url.rstrip('/') == url_main_page.rstrip('/'))
        assert profile_menu.is_displayed(), "Меню 'Профиль' не отображается после входа"