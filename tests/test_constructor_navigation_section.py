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

        buns_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(SECTION_BUNS))
        tab_classes = buns_tab.get_attribute("class")
        assert "tab_tab_type_current" in tab_classes or ACTIVE_TAB_NAME in tab_classes, (f"Таб 'Булки' не активен по умолчанию. Классы: {tab_classes}")

    @pytest.mark.parametrize(
    ("tab_locator, section_name"), [
        (SECTION_SAUCES, "Соусы"),
        (SECTION_FILLINGS, "Начинки"),
    ])

    def test_constructor_tab_navigation(self, driver, tab_locator, section_name):
        """
        Проверяет переключение между табами в конструкторе (с таба 'Булки' на другие табы).
        """
        #Исправлено: Замечание - корректная проверка класса активного таба
        driver.get(url_main_page)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGO))

        #Клик по табу (неактивному)
        tab_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(tab_locator))
        tab_element.click()
        #Исправлено: Замечание - ожидание появления активного класса
        WebDriverWait(driver, 10).until(lambda d: "tab_tab_type_current" in d.find_element(*tab_locator).get_attribute("class"))
        #Проверка, что таб стал активным — по полному имени класса
        classes = tab_element.get_attribute("class")
        assert "tab_tab_type_current" in classes, (
        f"Таб '{section_name}' не получил класс активности. "
        f"Фактические классы: {classes}"
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
        buns_tab = driver.find_element(*SECTION_BUNS)
        buns_classes = buns_tab.get_attribute("class")
        #Замечание - корректная проверка класса
        assert "tab_tab_type_current" in buns_classes, (f"Булки не активны при открытии. Классы: {buns_classes}")
        #2. Перейти на "Соусы"
        sauces_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SECTION_SAUCES))
        sauces_tab.click()

        #Убедимся, что "Соусы" активны
        WebDriverWait(driver, 10).until(
        lambda d: "tab_tab_type_current" in d.find_element(*SECTION_SAUCES).get_attribute("class")
        )
        # Проверяем, что "Булки" теперь не активны
        buns_classes_after = driver.find_element(*SECTION_BUNS).get_attribute("class")
        assert "tab_tab_type_current" not in buns_classes_after, ("Таб 'Булки' всё ещё активен после перехода на 'Соусы'")

        #3. Кликаем на "Булки"
        buns_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SECTION_BUNS))
        buns_tab.click()

        WebDriverWait(driver, 10).until(
        lambda d: "tab_tab_type_current" in d.find_element(*SECTION_BUNS).get_attribute("class")
        )

        #4. Проверить, что "Булки" стали активными после клика
        final_buns_classes = driver.find_element(*SECTION_BUNS).get_attribute("class")
        assert "tab_tab_type_current" in final_buns_classes, (
            f"Таб 'Булки' не активен после клика. Классы: {final_buns_classes}"
        )