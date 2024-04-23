import pytest

from pages.signin_page import SigninPage
from tests.base_test import BaseTest

@pytest.mark.order(1)
class Testsignin(BaseTest):

    def test_valid_signin(self, driver):
        signinpage = SigninPage(driver)
        signinpage.valid_signin()