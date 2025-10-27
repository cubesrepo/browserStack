import pytest
from datetime import datetime
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_page import OrderPage

@pytest.mark.order
class TestOrder:
    @pytest.fixture
    def cart_page(self, login_driver, delay):
        return CartPage(login_driver, delay)

    @pytest.fixture
    def checkout_page(self, login_driver, delay):
        return CheckoutPage(login_driver, delay)

    @pytest.fixture
    def order_page(self, login_driver, delay):
        return OrderPage(login_driver, delay)

    @pytest.mark.skip
    def test_order_page_without_existing_order(self, order_page):
        current_url, current_result_no_order = order_page.get_no_order_found()

        expected_url = "https://bstackdemo.com/orders"
        expected_result_no_order = "No orders found"

        assert current_url == expected_url, \
            f"Expected URL to be {expected_url}, but got {current_url} instead"

        assert current_result_no_order == expected_result_no_order, \
            f"Expected result to be {expected_result_no_order}, but got {current_result_no_order} instead"

    def test_order_page_details(self, cart_page, checkout_page, order_page):
        cart_page.verify_add_to_cart_count_subtotal()
        checkout_page.verify_checking_out_with_valid_details()

        current_result_date, current_total_price, current_result_ship_to = order_page.verify_order_details()

        expected_result_date = datetime.now().strftime("%B %d, %Y")
        expected_result_total_price = "$7590"
        expected_result_ship_to = "demouser"

        assert current_result_date == expected_result_date, \
            f"Expected result to be {expected_result_date}, but got {current_result_date} instead."

        assert current_total_price == expected_result_total_price, \
            f"Expected result to be {expected_result_total_price}, but got {current_total_price} instead."

        assert current_result_ship_to == expected_result_ship_to, \
            f"Expected result to be {expected_result_ship_to}, but got {current_result_ship_to} instead."