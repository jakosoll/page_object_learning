from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_FORM_EMAIL_INPUT = (By.CSS_SELECTOR, 'input[type="email"]')
    LOGIN_FORM_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type="password"]')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
