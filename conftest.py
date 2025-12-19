import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from urls import url_main_page

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