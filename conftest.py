import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import url_main_page, url_login_page
from data import Credential
from locators import (
    BUTTON_MAIN_LOGIN,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_LOGIN,
    MENU_PROFILE,
    LINK_PROFILE
)

@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и закрытия драйвера Chrome (scope='function')."""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    driver.get(url_main_page)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_user(driver):
    """
    Фикстура для входа в аккаунт.
    """
    #Вход
    driver.get(url_main_page)
    
    #Клик по кнопке для перехода на страницу входа
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_MAIN_LOGIN)).click()
    
    WebDriverWait(driver, 10).until(EC.url_to_be(url_login_page))

    email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INPUT_EMAIL))
    email_input.clear()
    email_input.send_keys(Credential.email)

    password_input = driver.find_element(*INPUT_PASSWORD)
    password_input.clear()
    password_input.send_keys(Credential.password)

    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN))
    login_button.click()
    
    #Ожидание успешного входа
    WebDriverWait(driver, 10).until(EC.url_to_be(url_main_page + '/')) 
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LINK_PROFILE))

    yield driver