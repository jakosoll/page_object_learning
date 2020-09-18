import pytest
from .data import LINKS

from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', LINKS)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.go_to_site()
    page.get_product_name()
    page.get_product_price()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_message()
    page.should_be_basket_price()

