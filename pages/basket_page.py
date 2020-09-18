from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_product_form_in_basket(self):
        """Ожидаем, что в корзине нет товаров"""
        assert self.is_not_element_present(BasketPageLocators.BASKET_PRODUCT_FORM)

    def should_be_basket_empty_message(self):
        assert self.is_present_element(BasketPageLocators.BASKET_EMPTY_MESSAGE)