from datetime import datetime

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities import test_data


class OrderPage(BasePage):
    def click_order_menu(self):
        self.wait_clickable(test_data.order.ORDER_BUTTON_MENU).click()
    def get_no_order_found(self):
        return self.get_text(test_data.order.NO_ORDERS_FOUND).text
    def get_orders_url(self, url):
        return self.get_url(url)
    def get_total_price(self, price):
        locator = By.XPATH, f"(//span[normalize-space()='{price}'])[1]"
        return self.get_text(locator)
    def get_ship_to(self, user):
        locator = By.XPATH, f"(//span[@class='a-color-secondary value'][normalize-space()='{user}'])[1]"
        return self.get_text(locator)
    def get_order_placed_date(self):
        date = datetime.now().strftime("%B %d, %Y")
        locator = By.XPATH, f"(//span[@class='a-color-secondary value'][normalize-space()='{date}'])[1]"
        return self.get_text(locator)

    def verify_order_page_without_existing_order(self):
        self.click_order_menu()
        current_url = self.get_orders_url("https://bstackdemo.com/orders")
        current_result_no_order = self.get_no_order_found()
        return current_url, current_result_no_order

    def verify_order_details(self):
        self.click_order_menu()
        price = "$7590"
        user = "demouser"
        current_result_date = self.get_order_placed_date()
        current_total_price =self.get_total_price(price)
        current_result_ship_to = self.get_ship_to(user)

        return current_result_date, current_total_price, current_result_ship_to


