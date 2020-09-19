from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        form_email = self.find_element(LoginPageLocators.REGISTRATION_FORM_EMAIL)
        form_email.send_keys(email)
        form_password_1 = self.find_element(LoginPageLocators.REGISTRATION_FORM_PASSWORD_1)
        form_password_1.send_keys(password)
        form_password_2 = self.find_element(LoginPageLocators.REGISTRATION_FORM_PASSWORD_2)
        form_password_2.send_keys(password)
        button = self.find_element(LoginPageLocators.REGISTRATION_FORM_BUTTON)
        button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_string = self.browser.current_url.find('login')
        assert login_string != -1, 'No find "login" in url address'

    def should_be_login_form(self):
        try:
            login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        except NoSuchElementException:
            assert False, 'Login form not found'
        assert True

    def should_be_register_form(self):
        try:
            registration_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        except NoSuchElementException:
            assert False, 'Registration form not found'
        assert True
