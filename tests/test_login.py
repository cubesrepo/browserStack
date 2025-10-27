import pytest

from pages.login_page import LoginPage

@pytest.mark.login
class TestLogin:
    @pytest.fixture
    def login_page(self, driver, delay):
        loginpage =LoginPage(driver, delay)
        return loginpage

    def test_valid_login(self, login_page):
        current_result = login_page.login_with_valid_credentials()
        expected_result = "https://bstackdemo.com/?signin=true"
        assert current_result == expected_result,\
            f"Expected url to be {expected_result}, but got {current_result} url instead"

    def test_login_without_password(self, login_page):
        current_result = login_page.login_with_invalid_password()
        expected_result = "Invalid Password"

        assert current_result == expected_result,\
            f"Expected error to be displayed is {expected_result}, but got {current_result} error instead"

    def test_login_with_locked_user(self, login_page):
        current_result = login_page.login_with_locked_user()

        expected_result = "Your account has been locked."

        assert current_result == expected_result,\
            f"Expected error to be displayed is {expected_result}, but got {current_result} error instead"