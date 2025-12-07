import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import url_main_page, url_profile_page
from locators import (
    LOGO,
    SECTION_BUNS,
    SECTION_SAUCES,
    SECTION_FILLINGS,
    ACTIVE_TAB_NAME
)

class TestConstructorNavigation:
    """Тесты для проверки переключения между табами в конструкторе."""

    @pytest.mark.parametrize(
    ("tab_locator, section_name"), [
        (SECTION_BUNS, "Булки"),
        (SECTION_SAUCES, "Соусы"),
        (SECTION_FILLINGS, "Начинки"),
    ])

    def test_constructor_tab_navigation(self, driver, wait, tab_locator, section_name):
        """
        Проверяет переключение между табами в конструкторе.
        """
        driver.get(url_main_page)
        wait.until(EC.visibility_of_element_located(LOGO))

        #Клик по табу
        tab_element = wait.until(EC.element_to_be_clickable(tab_locator))
        tab_element.click()

        #Проверка активности таба (наличие класса активности)
        assert "current" in tab_element.get_attribute("class"), (
            f"Таб '{section_name}' не стал активным"
        )

        #Проверка видимости контента таба через текст активной вкладки
        active_tab_text = wait.until(EC.visibility_of_element_located(ACTIVE_TAB_NAME)).text
        assert active_tab_text == section_name, f"Текст активного таба не соответствует '{section_name}'"