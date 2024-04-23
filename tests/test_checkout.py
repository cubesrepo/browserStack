import pytest

from pages.checkout_page import CheckoutPage
from tests.base_test import BaseTest

@pytest.mark.order(4)
class Testcheckout(BaseTest):
    def test_added_valid_shipping_address(self, driver):
        checkoutpage = CheckoutPage(driver)
        checkoutpage.add_valid_shipping_address()