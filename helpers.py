from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import INPUT_EMAIL, INPUT_PASSWORD, BUTTON_LOGIN

def perform_login(driver, email, password):
    driver.find_element(*INPUT_EMAIL).send_keys(email)
    driver.find_element(*INPUT_PASSWORD).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUTTON_LOGIN)).click()