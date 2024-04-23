import pytest

from pages.favourites_page import FavouritesPage
from tests.base_test import BaseTest

@pytest.mark.order(3)
class Testfavouritespage(BaseTest):

    def test_favourites_page_lists(self, driver):
        favouritespage = FavouritesPage(driver)
        favouritespage.verify_lists_of_favourites()
        favouritespage.add_to_cart_and_check_out_all_products_in_favourites()
