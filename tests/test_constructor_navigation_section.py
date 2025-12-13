import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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

    def test_default_tab_is_buns(self, driver):
        """
        Проверяет, что при открытии страницы активен таб 'Булки'.
        """
        driver.get(url_main_page)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGO))

        buns_tab = driver.find_element(*SECTION_BUNS)
        classes = buns_tab.get_attribute("class").split()
        assert "tab_tab_type_current" in classes, (
            f"Таб 'Булки' не активен по умолчанию. Классы: {classes}"
        )

        active_tab_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACTIVE_TAB_NAME)).text
        assert active_tab_text == "Булки", "Активный таб по умолчанию не 'Булки'"

    @pytest.mark.parametrize(
    ("tab_locator, section_name"), [
        (SECTION_SAUCES, "Соусы"),
        (SECTION_FILLINGS, "Начинки"),
    ])

    def test_constructor_tab_navigation(self, driver, tab_locator, section_name):
        """
        Проверяет переключение между табами в конструкторе (с таба 'Булки' на другие табы).
        """
        driver.get(url_main_page)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGO))

        #Клик по табу (неактивному)
        tab_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(tab_locator))
        tab_element.click()

        #Проверка, что таб стал активным — по полному имени класса
        classes = tab_element.get_attribute("class").split()
        assert "tab_tab_type_current" in classes, (
        f"Таб '{section_name}' не получил класс 'tab_tab_type_current'. "
        f"Фактические классы: {classes}"
        )
        #Проверка текста активной вкладки
        active_tab_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACTIVE_TAB_NAME)).text
        assert active_tab_text == section_name, (
            f"Текст активного таба не соответствует ожидаемому: '{section_name}'"
            )
   
    #ИСПРАВЛЕНО: Отредактирован добавленный тест
    def test_navigate_away_and_back_to_buns(self, driver):
        """
        Проверяет, что таб 'Булки' становится активным при клике на него после переключения на другой таб.
        Это подтверждает, что активация происходит именно при переключении, а не только при загрузке страницы.
        """
        driver.get(url_main_page)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGO))
    
        #1. Убедимся, что изначально активны "Булки"
        assert "tab_tab_type_current" in driver.find_element(*SECTION_BUNS).get_attribute("class"), "Булки не активны при открытии"     
       
        #2. Перейти на "Соусы"
        sauces_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SECTION_SAUCES))
        sauces_tab.click()

        #Убедимся, что "Соусы" активны
        WebDriverWait(driver, 10).until(
        lambda d: "tab_tab_type_current" in d.find_element(*SECTION_SAUCES).get_attribute("class")
        )
        assert "tab_tab_type_current" not in driver.find_element(*SECTION_BUNS).get_attribute("class"), \
        "Таб 'Булки' всё ещё активен после перехода на 'Соусы'"

        #3. Кликаем на "Булки"
        buns_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SECTION_BUNS))
        buns_tab.click()

        WebDriverWait(driver, 10).until(
        lambda d: "tab_tab_type_current" in d.find_element(*SECTION_BUNS).get_attribute("class")
        )

        #4. Проверить, что "Булки" стали активными после клика
        active_tab_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACTIVE_TAB_NAME)).text
        assert active_tab_text == "Булки", f"Ожидался активный таб 'Булки', но получено: '{active_tab_text}'"