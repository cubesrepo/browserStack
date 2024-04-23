import time

import test_data
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def add_valid_shipping_address(self):
        time.sleep(2)

        #checking the page url
        assert self.url_is("https://bstackdemo.com/checkout")

        #maximum scroll up
        self.driver.execute_script("window.scrollTo(0, 0);")

        #assert number of items in checkout
        assert self.get_text(test_data.checkout.NUMBER_OF_ITEMS) == "25 item(s)"

        #input first name
        self.send_keys(test_data.checkout.FIRST_NAME, "Auto")
        time.sleep(0.5)
        # input last name
        self.send_keys(test_data.checkout.LAST_NAME, "Mation")
        time.sleep(0.5)
        # input address
        self.send_keys(test_data.checkout.ADDRESS, "Automation address")
        time.sleep(0.5)
        # input province
        self.send_keys(test_data.checkout.PROVINCE, "Automation province")
        time.sleep(0.5)
        # input postal
        self.send_keys(test_data.checkout.POSTAL, "1235")
        time.sleep(0.5)

        #click submit
        self.wait_clickable(test_data.checkout.SUBMIT).click()

        time.sleep(0.5)
        #click continue shopping
        self.wait_clickable(test_data.checkout.CONTINUE_SHOP).click()