from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser, url, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.browser.implicitly_wait(self.timeout)

    def go_to_site(self):
        self.browser.get(self.url)

    def is_present_element(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return element

    def find_element(self, locator):
        return WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located(locator),
                                                               message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return WebDriverWait(self.browser, self.timeout).until(EC.presence_of_all_elements_located(locator),
                                                               message=f"Can't find elements by locator {locator}")
