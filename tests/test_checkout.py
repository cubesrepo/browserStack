import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from tests.conftest import driver, login_driver

@pytest.mark.checkout
class TestCheckout:
    @pytest.fixture
    def checkout_page(self, login_driver, delay):
        return CheckoutPage(login_driver, delay)
    @pytest.fixture
    def cart_page(self, login_driver, delay):
        return CartPage(login_driver, delay)

    def test_checking_out_with_valid_details(self, checkout_page, cart_page):
        cart_page.verify_add_to_cart_count_subtotal()
        current_result_url,  current_result_order_placed_message = (
            checkout_page.verify_checking_out_with_valid_details())

        expected_result_url = "https://bstackdemo.com/confirmation"
        expected_result_order_placed_message = "Your Order has been successfully placed."

        assert current_result_url == expected_result_url, \
            f"Expected result url to be {expected_result_url} but got {current_result_url} instead."

        assert current_result_order_placed_message == expected_result_order_placed_message, \
            f"Expected result to be {expected_result_order_placed_message}, but got {current_result_order_placed_message} instead."

    def test_checking_out_with_space_in_details(self, checkout_page, cart_page):
        cart_page.verify_add_to_cart_count_subtotal()
        checkout_page.proceed_to_checkout()
        current_result_url, current_result_order_placed_message = (
            checkout_page.verify_checking_out_with_space_in_details())

        expected_result_url = "https://bstackdemo.com/confirmation"
        expected_result_order_placed_message = "Your Order has been successfully placed."

        assert current_result_url == expected_result_url, \
            f"Expected result url to be {expected_result_url} but got {current_result_url} instead."

        assert current_result_order_placed_message == expected_result_order_placed_message, \
            f"Expected result to be {expected_result_order_placed_message}, but got {current_result_order_placed_message} instead."

    def test_checking_out_without_details(self, checkout_page, cart_page):
        cart_page.verify_add_to_cart_count_subtotal()
        checkout_page.proceed_to_checkout()
        current_url, current_result_please_fill_out_this_field =  checkout_page.verify_checking_out_without_details()

        expected_result_please_fill_out_this_field = "Please fill out this field."
        expected_result_url = "https://bstackdemo.com/checkout"

        assert current_result_please_fill_out_this_field == expected_result_please_fill_out_this_field, \
            f"Expected result url to be {expected_result_please_fill_out_this_field} but got {current_result_please_fill_out_this_field} instead."

        assert current_url == expected_result_url, \
            f"Expected result to be {expected_result_url}, but got {current_url} instead."

