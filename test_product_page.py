import pytest
import time
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """Создаем пользователя и проверяем, что он вошел"""
        self.registration_ulr = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        registration_page = LoginPage(browser, self.registration_ulr)
        registration_page.go_to_site()
        email = str(time.time()) + "@fakemail.org"
        registration_page.register_new_user(email=email, password='afafhh9131k')
        registration_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.go_to_site()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.go_to_site()
        page.get_product_name()
        page.get_product_price()
        page.add_product_to_cart()
        page.should_be_product_added_message()
        page.should_be_basket_price()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_form_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.go_to_site()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.go_to_site()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_product_form_in_basket()
    basket_page.should_be_basket_empty_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.go_to_site()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.go_to_site()
    page.get_product_name()
    page.get_product_price()
    page.add_product_to_cart()
    page.should_be_product_added_message()
    page.should_be_basket_price()


@pytest.mark.xfail
def test_guest_can_see_success_message_after_product_adding(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.go_to_site()
    page.add_product_to_cart()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.go_to_site()
    page.add_product_to_cart()
    page.should_be_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.go_to_site()
    page.should_be_login_link()
