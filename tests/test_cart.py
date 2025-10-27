import pytest

from pages.cart_page import CartPage

@pytest.mark.cart
class TestCart:
    @pytest.fixture
    def cart_page(self, login_driver, delay):
        return CartPage(login_driver, delay)

    def test_add_to_cart_count_subtotal(self, cart_page):
        current_result_sub_total_price, expected_result_sub_total_price, \
            current_result_cart_quantity, expected_result_cart_quantity= cart_page.verify_add_to_cart_count_subtotal()

        assert current_result_sub_total_price == expected_result_sub_total_price, \
            f"Expected result to be {expected_result_sub_total_price}, but got {current_result_cart_quantity} instead."

        assert current_result_cart_quantity == expected_result_cart_quantity, \
            f"Expected result to be {expected_result_cart_quantity} but got {current_result_cart_quantity} instead"

    def test_removing_items_in_cart(self, cart_page):
        current_result_cart_empty, current_result_subtotal_empty = cart_page.verify_remove_products_cart()

        expected_result_cart_empty = "Add some products in the bag :)"
        expected_result_subtotal_empty = "$ 0.00"

        assert  current_result_cart_empty == expected_result_cart_empty,\
            f"Expected result to be {expected_result_cart_empty} but got {current_result_cart_empty}"

        assert current_result_subtotal_empty == expected_result_subtotal_empty,\
            f"Expected result to be {expected_result_subtotal_empty} but got {current_result_subtotal_empty}"

    def test_adding_quantity_multiple_times(self, cart_page):
        current_result_bag_quantity, current_result_total_price = cart_page.verify_adding_quantity_multiple_times()

        expected_result_bag_quantity = 20
        expected_result_total_price = "$ 15980.00"

        assert expected_result_bag_quantity == expected_result_bag_quantity, \
            f"Expected result to be {expected_result_bag_quantity}, but got {current_result_bag_quantity} instead"

        assert current_result_total_price == expected_result_total_price, \
            f"Expected result to be {expected_result_total_price}, but got {current_result_total_price} instead"