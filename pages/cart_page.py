
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities import test_data


class CartPage(BasePage):

    def trimmed_price(self, item_price):
        price_text = self.get_text(item_price)
        price = price_text.replace("$",'')
        return price

    def check_cart_count(self, cart_count, add_to_cart_btn):
        get_cart_count = self.get_bag_quantity()

        if str(cart_count) != get_cart_count:
            self.action_click(add_to_cart_btn)
            self.action_click(test_data.cart.CLOSE_BTN)

    def count_total_price(self, price_lists):
        total_price = 0
        for price in price_lists:
            total_price += price

        formatted_price = "{:.2f}".format(total_price)
        return formatted_price

    def add_items_to_cart(self):
        price_lists = []
        cart_count = 0

        for index in range(1, 10 + 1):
            add_to_cart_btn = By.XPATH, f"(//div[@class='shelf-item__buy-btn'][normalize-space()='Add to cart'])[{index}]"

            try:
                self.action_click(add_to_cart_btn)
                self.action_click(test_data.cart.CLOSE_BTN)
                cart_count += 1
            except Exception as e:
                print(f"Unexpected error occurred: {e}")

            self.check_cart_count(cart_count, add_to_cart_btn)

            item_price = By.CSS_SELECTOR, f"div[id='{index}'] div[class='val']"
            price = self.trimmed_price(item_price)
            price_lists.append(float(price))

        return self.count_total_price(price_lists), cart_count

    def get_cart_empty(self):
        return self.get_text(test_data.cart.SHELF_EMPTY).replace('\n', ' ')

    def get_subtotal_price(self):
        return self.get_text(test_data.cart.SUB_TOTAL_PRICE)

    def get_bag_quantity(self):
        return self.get_text(test_data.cart.CART_QUANTITY)

    def verify_add_to_cart_count_subtotal(self):
        price_lists, cart_count = self.add_items_to_cart()

        current_result_sub_total_price = self.get_subtotal_price()
        expected_result_sub_total_price = price_lists

        current_result_cart_quantity = self.get_bag_quantity()
        expected_result_cart_quantity = cart_count

        return (current_result_sub_total_price, f"$ {expected_result_sub_total_price}",
                current_result_cart_quantity, str(expected_result_cart_quantity))

    def verify_remove_products_cart(self):
        self.add_items_to_cart()

        while True:
            bag_quantity = self.get_bag_quantity()
            if bag_quantity == "0":
                break
            self.action_click(test_data.cart.REMOVE_CART_PRODUCTS)

        current_result_cart_empty = self.get_cart_empty()
        current_result_subtotal_empty =  self.get_subtotal_price()

        return current_result_cart_empty, current_result_subtotal_empty

    def verify_adding_quantity_multiple_times(self):
        add_to_cart_btn_product1 = By.XPATH, "(//div[@class='shelf-item__buy-btn'][normalize-space()='Add to cart'])[1]"
        self.action_click(add_to_cart_btn_product1)

        cart_quantity = self.get_bag_quantity()
        if int(cart_quantity) != 1:
            self.wait_clickable(add_to_cart_btn_product1).click()

        bag_quantity = 0
        for quantity in range(1, 19+1):
            self.action_click(test_data.cart.ADD_QUANTITY)
            bag_quantity += 1

        current_result_bag_quantity = bag_quantity
        current_result_total_price = self.get_subtotal_price()

        return current_result_bag_quantity, current_result_total_price
