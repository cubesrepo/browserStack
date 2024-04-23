import pytest

from pages.home_page import HomePage
from tests.base_test import BaseTest

@pytest.mark.order(2)
class Testhomepage(BaseTest):


    def test_add_to_cart_all_products(self, driver):
        homepage = HomePage(driver)
        homepage.add_to_cart_all_products()

    def test_remove_all_products_in_cart(self, driver):
        homepage = HomePage(driver)
        homepage.remove_all_product_in_cart()

    def test_clicking_all_products_favorite_icon(self, driver):
        homepage = HomePage(driver)
        homepage.verify_favorites_functionalities()