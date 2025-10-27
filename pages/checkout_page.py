from pages.base_page import BasePage
from utilities import test_data


class CheckoutPage(BasePage):

    def proceed_to_checkout(self):
        self.action_click(test_data.cart.CHECK_OUT)

    def fill_check_out_details(self, first_name, last_name, address, state, postal_code):

        #input first name
        self.type(test_data.checkout.FIRST_NAME, first_name)
        # input last name
        self.type(test_data.checkout.LAST_NAME, last_name)
        # input address
        self.type(test_data.checkout.ADDRESS, address)
        # input state
        self.type(test_data.checkout.STATE, state)
        # input postal code
        self.type(test_data.checkout.POSTAL, postal_code)
    def get_current_url(self, url):
        return self.get_url(url)

    def get_successfully_paid_message(self):
        return self.get_text(test_data.checkout.SUCCESSFULLY_PLACED)

    def verify_checking_out_with_valid_details(self):
        shipping_details = {
            "first_name": "John David",
            "last_name": "Harper",
            "address": "Address1234",
            "state": "Golden state",
            "postal_code": "55123"

        }

        self.proceed_to_checkout()
        self.fill_check_out_details(shipping_details["first_name"], shipping_details["last_name"],
                                    shipping_details["address"], shipping_details["state"], shipping_details["postal_code"])
        self.action_click(test_data.checkout.SUBMIT)

        current_result_url = self.get_current_url("https://bstackdemo.com/confirmation")
        current_result_order_placed_message = self.get_successfully_paid_message()

        self.wait_clickable(test_data.checkout.CONTINUE_SHOPPING).click()

        return current_result_url, current_result_order_placed_message

    def verify_checking_out_with_space_in_details(self):
        self.fill_check_out_details(" "," "," "," "," ")
        self.action_click(test_data.checkout.SUBMIT)

        current_result_order_placed_message = self.get_successfully_paid_message()
        current_url = self.get_current_url("https://bstackdemo.com/confirmation")

        return current_url, current_result_order_placed_message

    def verify_checking_out_without_details(self):

        self.action_click(test_data.checkout.SUBMIT)

        current_result_please_fill_out_this_field = self.validation_fillout_this_field(test_data.checkout.FIRST_NAME)
        current_url = self.get_current_url("https://bstackdemo.com/checkout")

        return current_url, current_result_please_fill_out_this_field

