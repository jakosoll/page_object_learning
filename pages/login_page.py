from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
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
