from selenium.webdriver.common.by import By

# Ссылки
LINK_REGISTER = (By.LINK_TEXT, "Зарегистрироваться")
LINK_PROFILE = (By.PARTIAL_LINK_TEXT, "Личный кабинет")
LINK_ALREADY_ACCOUNT = (By.LINK_TEXT, "Уже есть аккаунт?")
LINK_RECOVERY = (By.LINK_TEXT, "Восстановить пароль")
LINK_RETURN_TO_LOGIN = (By.LINK_TEXT, "Войти") # ИСПРАВЛЕНО: В форме восстановления пароля ссылка называется "Войти"

# Поля ввода
INPUT_NAME = (By.NAME, "name")
INPUT_EMAIL = (By.NAME, "email")
INPUT_PASSWORD = (By.NAME, "password")
PROFILE_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # Точный локатор
PROFILE_EMAIL_INPUT = (By.XPATH, "//label[text()='Логин']/following-sibling::input") # Точный локатор

# Кнопки
BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")
BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
BUTTON_MAIN_LOGIN = (By.XPATH, "//button[text()='Войти в аккаунт']") # Упрощенный локатор для главной
BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выйти']")
BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
BUTTON_LOGO = (By.CSS_SELECTOR, "header [class*='logo']")

# Разделы конструктора
SECTION_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
SECTION_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div")
SECTION_FILLINGS = (By.XPATH, "//span[text()='Начинки']/parent::div")
ACTIVE_TAB_NAME = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span") # Добавлен для проверки активного таба

# Прочие элементы
LOGO = (By.CSS_SELECTOR, "header [class*='logo']")
MENU_PROFILE = (By.PARTIAL_LINK_TEXT, "Профиль")
ERROR_INPUT = (By.XPATH, "//p[text()='Некорректный пароль']") # Уточненный локатор
SUCCESS_REGISTRATION = (By.CLASS_NAME, "registration-success")