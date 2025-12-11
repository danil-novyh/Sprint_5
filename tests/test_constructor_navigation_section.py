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
   
    #ИСПРАВЛЕНО: Добавлен тест

    def test_navigate_away_and_back_to_buns(self, driver, wait):
        """
        Проверяет, что после перехода на другой таб (например, 'Соусы')
        можно вернуться обратно на таб 'Булки' и он становится активным.
        """
        driver.get(url_main_page)
        wait.until(EC.visibility_of_element_located(LOGO))
    
        #1. Убедимся, что изначально активны "Булки"
        buns_tab = driver.find_element(*SECTION_BUNS)
        assert "tab_tab_type_current" in buns_tab.get_attribute("class"), "Булки не активны при открытии"

        #2. Перейти на "Соусы"
        sauces_tab = wait.until(EC.element_to_be_clickable(SECTION_SAUCES))
        sauces_tab.click()

        #Убедимся, что "Соусы" активны
        assert "tab_tab_type_current" in sauces_tab.get_attribute("class"), "Соусы не стали активными"

        #3. Вернуться на "Булки"
        buns_tab = wait.until(EC.element_to_be_clickable(SECTION_BUNS))
        buns_tab.click()

        #4. Проверить, что "Булки" снова активны
        classes = buns_tab.get_attribute("class").split()
        assert "tab_tab_type_current" in classes, f"Булки не вернулись в активное состояние. Классы: {classes}"

        active_tab_text = wait.until(EC.visibility_of_element_located(ACTIVE_TAB_NAME)).text
        assert active_tab_text == "Булки", "После возврата активный таб не 'Булки'"