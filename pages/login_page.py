import time

from pages.base_page import BasePage
from utilities import test_data


class LoginPage(BasePage):
    def type_username_password(self, username_value, password_value):
        #type username
        self.action_type_and_enter(test_data.signin.USERNAME, username_value)
        #type password
        self.action_type_and_enter(test_data.signin.PASSWORD, password_value)
        #click login
        self.wait_clickable(test_data.signin.LOGIN_BTN).click()

    def get_invalid_password_error(self):
        return self.get_text(test_data.signin.INVALID_PASSWORD_ERROR)

    def get_locked_user_error(self):
        return self.get_text(test_data.signin.ACCOUNT_LOCKED_ERROR)

    def login_with_valid_credentials(self):
        self.type_username_password(test_data.USER_CREDENTIALS["username"],
                                    test_data.USER_CREDENTIALS["password"])
        time.sleep(2)
        return self.home_page_is_loaded("https://bstackdemo.com/?signin=true")

    def login_with_invalid_password(self):
        self.type_username_password(test_data.USER_CREDENTIALS["username"],
                                    test_data.USER_CREDENTIALS["invalid_password"])
        return self.get_invalid_password_error()

    def login_with_locked_user(self):
        self.type_username_password(test_data.USER_CREDENTIALS["username_lock"],
                                    test_data.USER_CREDENTIALS["password"])
        return self.get_locked_user_error()

    def home_page_is_loaded(self, url):
        return self.get_url(url)
