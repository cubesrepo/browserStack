import time

import test_data
from pages.base_page import BasePage


class SigninPage(BasePage):

    def valid_signin(self):
        time.sleep(2)

        assert self.title_is("StackDemo"), "invalid page title"

        #input username
        username = self.wait_visibility(test_data.signin.USERNAME)
        self.action_send_keys_with_enter(username, test_data.USERNAME)

        #input password
        password = self.wait_visibility(test_data.signin.PASSWORD)
        self.action_send_keys_with_enter(password, test_data.PASSWORD)

        #click login btn
        login_btn = self.wait_presence(test_data.signin.LOGIN_BTN)
        self.action_click(login_btn)