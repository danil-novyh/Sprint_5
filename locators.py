from selenium.webdriver.common.by import By

#Ссылки
LINK_REGISTER = (By.LINK_TEXT, "Зарегистрироваться")
LINK_PROFILE = (By.XPATH, "//a[@href='/account']")
LINK_ALREADY_ACCOUNT = (By.XPATH, "//a[contains(text(), 'Войти')]")
LINK_RECOVERY = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
LINK_RETURN_TO_LOGIN = (By.XPATH, "//a[contains(text(), 'Войти')]")

#Поля ввода
INPUT_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
INPUT_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
PROFILE_NAME_INPUT = (By.XPATH, "//label[normalize-space(.)='Имя']/following-sibling::input")
PROFILE_EMAIL_INPUT = (By.XPATH, "//label[text()='Логин']/following-sibling::input")

#Кнопки
BUTTON_REGISTER = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
BUTTON_REG = (By.XPATH, '//button[text()="Зарегистрироваться"]')
BUTTON_REG_LOGIN = (By.XPATH, "//a[text()='Войти']")
BUTTON_LOGIN_REG = (By.XPATH, ".//a[text()='Войти']")
BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")
BUTTON_LOGIN_PAGE = (By.XPATH, '//button[text()="Войти"]')
BUTTON_PAGE_LOGIN = (By.XPATH, ".//h2[text()='Вход']")
BUTTON_MAIN_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
BUTTON_ACCOUNT = By.XPATH, '//p[text()="Личный Кабинет"]'
BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выход')]")
BUTTON_LOGOUT_PAGE = (By.XPATH, '//button[text()="Выход"]') 
BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
BUTTON_LOGO = (By.CSS_SELECTOR, "div[class*='AppHeader_header__logo']")
BUTTON_FORGOT_PASSWORD = [By.XPATH, '//a[text()="Восстановить пароль"]']
BUTTON_RECOVERY = (By.XPATH, '//button[text()="Восстановить"]')

ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

#Разделы конструктора
SECTION_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
SECTION_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div")
SECTION_FILLINGS = (By.XPATH, "//span[text()='Начинки']/parent::div")
# ИСПРАВЛЕНО: локатор для активного таба (замечание #7)
ACTIVE_TAB_NAME = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span")

#Прочие элементы
LOGO = (By.CSS_SELECTOR, "div[class*='AppHeader_header__logo']")
MENU_PROFILE = (By.XPATH, "//a[@href='/account']")
ERROR_INPUT = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
SUCCESS_REGISTRATION = (By.CLASS_NAME, "registration-success")