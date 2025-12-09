import pytest
from selenium.webdriver.support import expected_conditions as EC
from urls import url_main_page
from locators import (
    LOGO,
    SECTION_BUNS,
    SECTION_SAUCES,
    SECTION_FILLINGS,
    ACTIVE_TAB_NAME
)

class TestConstructorNavigation:
    """Тесты для проверки переключения между табами в конструкторе."""

    def test_default_tab_is_buns(self, driver, wait):
        """
        Проверяет, что при открытии страницы активен таб 'Булки'.
        """
        driver.get(url_main_page)
        wait.until(EC.visibility_of_element_located(LOGO))

        buns_tab = driver.find_element(*SECTION_BUNS)
        classes = buns_tab.get_attribute("class").split()
        assert "tab_tab_type_current" in classes, (
            f"Таб 'Булки' не активен по умолчанию. Классы: {classes}"
        )

        active_tab_text = wait.until(EC.visibility_of_element_located(ACTIVE_TAB_NAME)).text
        assert active_tab_text == "Булки", "Активный таб по умолчанию не 'Булки'"

    @pytest.mark.parametrize(
    ("tab_locator, section_name"), [
        (SECTION_SAUCES, "Соусы"),
        (SECTION_FILLINGS, "Начинки"),
    ])

    def test_constructor_tab_navigation(self, driver, wait, tab_locator, section_name):
        """
        Проверяет переключение между табами в конструкторе (с таба 'Булки' на другие табы).
        """
        driver.get(url_main_page)
        wait.until(EC.visibility_of_element_located(LOGO))

        #Клик по табу (неактивному)
        tab_element = wait.until(EC.element_to_be_clickable(tab_locator))
        tab_element.click()

        #Проверка, что таб стал активным — по полному имени класса
        classes = tab_element.get_attribute("class").split()
        assert "tab_tab_type_current" in classes, (
        f"Таб '{section_name}' не получил класс 'tab_tab_type_current'. "
        f"Фактические классы: {classes}"
        )
        #Проверка текста активной вкладки
        active_tab_text = wait.until(EC.visibility_of_element_located(ACTIVE_TAB_NAME)).text
        assert active_tab_text == section_name, (
            f"Текст активного таба не соответствует ожидаемому: '{section_name}'"
            )