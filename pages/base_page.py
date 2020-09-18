from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.browser.implicitly_wait(self.timeout)

    def go_to_site(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def find_element(self, locator, timeout=4):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator),
                                                          message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=4):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Can't find elements by locator {locator}")

    def is_present_element(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_present_element(BasePageLocators.LOGIN_LINK), "Login link is not presented"
