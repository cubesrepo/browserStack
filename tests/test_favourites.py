import pytest

from pages.favourite_page import FavouritePage

@pytest.mark.favourites
class TestFavourites:
    @pytest.fixture
    def favourite_page(self, login_driver, delay):
        return FavouritePage(login_driver, delay)

    def test_total_favourites_product_found(self, favourite_page):
        current_url, current_result_product_found, expected_result_product_found = favourite_page.verify_total_favourites_product_found()
        expected_url = "https://bstackdemo.com/favourites"

        assert current_url == expected_url, \
            f"Expected URL to be {expected_url}, but got {current_url} instead."

        assert current_result_product_found == expected_result_product_found, \
            f"Expected result to be {expected_result_product_found}, but got {current_result_product_found} instead."


    def test_remove_favourites(self, favourite_page):
        current_result_product_found, expected_result_product_found = favourite_page.verify_remove_favourites()

        assert current_result_product_found == expected_result_product_found, \
            f"Expected result to be {expected_result_product_found}, but got {current_result_product_found} instead."