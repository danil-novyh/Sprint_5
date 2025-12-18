import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import url_main_page
from locators import (
    LOGO,
    SECTION_BUNS,
    SECTION_SAUCES,
    SECTION_FILLINGS,
    ACTIVE_TAB_CLASS
)

class TestConstructorNavigation:
    """Тесты для проверки переключения между табами в конструкторе."""

    def test_default_tab_is_buns(self, driver):
        """
        Проверяет, что при открытии страницы активен таб 'Булки'.
        """
        driver.get(url_main_page)
        #Ждем загрузки страницы (по логотипу)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGO))
        #Найти таб "Булки"
        buns_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located(SECTION_BUNS))
        tab_classes = buns_tab.get_attribute("class")
        # Исправлено замечание. Убрал ACTIVE_TAB_NAME
        assert ACTIVE_TAB_CLASS in tab_classes in tab_classes, (
            f"Таб 'Булки' не активен по умолчанию."
            f"Ожидается класс'{ACTIVE_TAB_CLASS}',"
            f"но найдены классы: {tab_classes}"
            )

    @pytest.mark.parametrize(
    ("tab_locator, section_name"), [
        (SECTION_SAUCES, "Соусы"),
        (SECTION_FILLINGS, "Начинки"),
    ],
    ids=["Соусы","Начинки"]
    )

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
        WebDriverWait(driver, 10).until(
        lambda d: ACTIVE_TAB_CLASS in
            d.find_element(*tab_locator).get_attribute("class"),
        message=f"Таб'{section_name}' не стал активным"
        )
        #Проверка, что таб стал активным — по полному имени класса
        classes = tab_element.get_attribute("class")
        assert ACTIVE_TAB_CLASS in classes, (
        f"Таб '{section_name}' не получил класс активности. "
        f"Ожидался '{ACTIVE_TAB_CLASS}',"
        f"но найдены классы: {classes}"
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
        assert "tab_tab_type_current" in ACTIVE_TAB_CLASS, (f"Булки не активны при открытии. Классы: {buns_classes}")
        #2. Перейти на "Соусы"
        sauces_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SECTION_SAUCES))
        sauces_tab.click()

        #Убедимся, что "Соусы" активны
        WebDriverWait(driver, 10).until(
        lambda d: ACTIVE_TAB_CLASS in d.find_element(*SECTION_SAUCES).get_attribute("class")
        )
        # Проверяем, что "Булки" теперь не активны
        buns_classes_after = driver.find_element(*SECTION_BUNS).get_attribute("class")
        assert ACTIVE_TAB_CLASS not in buns_classes_after, (
            f"Таб 'Булки' всё ещё активен после перехода на 'Соусы'."
            f"Классы:{buns_classes_after}"
        )

        #3. Кликаем на "Булки"
        buns_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SECTION_BUNS))
        buns_tab.click()
        #Ждем активации "Булки"
        WebDriverWait(driver, 10).until(
            lambda d: ACTIVE_TAB_CLASS in
                d.find_element(*SECTION_BUNS).get_attribute("class")
        )

        #4. Проверить, что "Булки" стали активными после клика
        final_buns_classes = driver.find_element(*SECTION_BUNS).get_attribute("class")
        assert ACTIVE_TAB_CLASS in final_buns_classes, (
            f"Таб 'Булки' не активен после клика."
            f"Ожидался класс '{ACTIVE_TAB_CLASS}',"
            f"но найдены классы: {final_buns_classes}"
        )