from typing import Type
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    browser: Type[webdriver.Chrome]

    def __init__(self, browser: Type[webdriver.Chrome], url, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_present_element(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
