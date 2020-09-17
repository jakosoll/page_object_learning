from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_FORM_EMAIL_INPUT = (By.CSS_SELECTOR, 'input[type="email"]')
    LOGIN_FORM_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type="password"]')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color')
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADDED_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BASKET_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')