import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Используем правильные импорты
from urls import BASE_URL, LOGIN_PAGE
from data import TEST_USER
from locators import (
    BUTTON_MAIN_LOGIN,
    INPUT_EMAIL,
    INPUT_PASSWORD,
    BUTTON_LOGIN,
    MENU_PROFILE,
    BUTTON_LOGOUT,
    LINK_PROFILE
)

@pytest.fixture(scope="function") # ИСПРАВЛЕНО: Сменено на scope="function" для атомарности
def driver():
    """Фикстура для инициализации и закрытия драйвера Chrome (scope='function')."""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")
    
    # Рекомендуется использовать webdriver-manager для автоматического управления драйвером
    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit() # driver.quit() в конце каждой функции, как того требует атомарность

@pytest.fixture
def wait(driver):
    """Фикстура для явного ожидания (WebDriverWait)."""
    return WebDriverWait(driver, 10)

@pytest.fixture
def logged_in_user(driver, wait):
    """
    ИСПРАВЛЕНО: Заменяет 'login' и 'logout'. Выполняет авторизацию (setup)
    и выход (teardown) после теста.
    """
    # Setup: Логинимся
    driver.get(BASE_URL)
    
    # Клик по кнопке для перехода на страницу входа
    wait.until(EC.element_to_be_clickable(BUTTON_MAIN_LOGIN)).click()
    
    wait.until(EC.url_to_be(LOGIN_PAGE))

    email_input = wait.until(EC.visibility_of_element_located(INPUT_EMAIL))
    email_input.clear()
    email_input.send_keys(TEST_USER["email"])

    password_input = driver.find_element(*INPUT_PASSWORD)
    password_input.clear()
    password_input.send_keys(TEST_USER["password"])

    login_button = wait.until(EC.element_to_be_clickable(BUTTON_LOGIN))
    login_button.click()
    
    # Ожидание успешного входа
    wait.until(EC.url_to_be(BASE_URL + '/')) 
    wait.until(EC.element_to_be_clickable(LINK_PROFILE))

    yield driver

    # !!!!!Выход из аккаунта
    try:
        # Переход в Личный кабинет, затем выход
        driver.get(BASE_URL)
        wait.until(EC.element_to_be_clickable(LINK_PROFILE)).click()
        wait.until(EC.url_contains("/account/profile"))
        
        logout_button = wait.until(EC.element_to_be_clickable(BUTTON_LOGOUT))
        logout_button.click()
        wait.until(EC.url_to_be(LOGIN_PAGE))
    except Exception:
        pass