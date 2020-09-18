from typing import Type
from selenium import webdriver
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):

    def __init__(self, browser: Type[webdriver.Chrome], url, product_name=None, product_price=None):
        super().__init__(browser, url)
        self.product_name = product_name
        self.product_price = product_price

    def add_product_to_cart(self):
        button_add_to_cart = self.find_element(ProductPageLocators.BUTTON_ADD_TO_CART)
        button_add_to_cart.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_product_name(self):
        self.product_name = self.find_element(ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        self.product_price = self.find_element(ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_added_message(self):
        product_added_message = self.find_element(ProductPageLocators.ADDED_MESSAGE).text
        assert self.product_name == product_added_message, \
            'Product name != Product name in basket'

    def should_be_basket_price(self):
        basket_price = self.find_element(ProductPageLocators.BASKET_PRICE).text
        assert self.product_price == basket_price, 'Basket price != product price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(ProductPageLocators.ADDED_MESSAGE), \
            "Success message in not disappeared"
