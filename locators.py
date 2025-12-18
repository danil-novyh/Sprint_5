from selenium.webdriver.common.by import By

#Ссылки
REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
HEADING_REGISTER = (By.XPATH, "//h2[text()='Регистрация']")
LINK_REGISTER = (By.LINK_TEXT, "Зарегистрироваться")
LINK_PROFILE = (By.XPATH, "//a[@href='/account']")
LINK_ALREADY_ACCOUNT = (By.XPATH, "//a[contains(text(), 'Войти')]")
LINK_RECOVERY = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")

#Поля ввода
INPUT_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
INPUT_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')

#Кнопки
BUTTON_REG = (By.XPATH, '//button[text()="Зарегистрироваться"]')
BUTTON_LOGIN_REG = (By.XPATH, ".//a[text()='Войти']")
BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")
BUTTON_PAGE_LOGIN = (By.XPATH, ".//h2[text()='Вход']")
BUTTON_MAIN_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
BUTTON_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')
BUTTON_LOGOUT_PAGE = (By.XPATH, '//button[text()="Выход"]') 
BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
BUTTON_FORGOT_PASSWORD = (By.XPATH, '//a[text()="Восстановить пароль"]')
BUTTON_RECOVERY = (By.XPATH, '//button[text()="Восстановить"]')

ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

#Разделы конструктора
SECTION_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
SECTION_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div")
SECTION_FILLINGS = (By.XPATH, "//span[text()='Начинки']/parent::div")
ACTIVE_TAB_CLASS = "tab_tab_type_current"

#Прочие элементы
LOGO = (By.CSS_SELECTOR, "div[class*='AppHeader_header__logo']")
MENU_PROFILE = (By.XPATH, "//a[@href='/account']")
ERROR_INPUT = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
SUCCESS_REGISTRATION = (By.CLASS_NAME, "registration-success")