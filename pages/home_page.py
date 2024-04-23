import time

from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class HomePage(BasePage):
    def add_to_cart_all_products(self):
        time.sleep(4)
        # check the homepage url
        assert self.url_is("https://bstackdemo.com/?signin=true"), "invalid homepage url"

        # check if the add to cart badge is zero
        assert self.get_text(test_data.cart.CART_QUANTITY) == "0"

        # loop for clicking add to cart btn for all products
        for i in range(1, 26):

            add_to_cart_product = By.CSS_SELECTOR, f"div[id='{i}'] div[class='shelf-item__buy-btn']"
            print(add_to_cart_product)
            # wait for presence of addtocart
            try:
                add_to_cart_btn = self.wait_presence(add_to_cart_product)
            except:

                add_to_cart_btn = self.wait_clickable(add_to_cart_product)

            # click add to cart btn
            self.action_click(add_to_cart_btn)

            time.sleep(0.2)

            # check if the cart quantity is adding
            assert self.get_text(test_data.cart.CART_QUANTITY) == str(i)

            time.sleep(0.2)

            # close the cart panel after clicking the 2nd/3rd product in each row
            if i % 4 == 2 or i % 4 == 3:
                self.wait_clickable(test_data.cart.CLOSE_BTN).click()
                time.sleep(0.2)

            # scroll to the add to cart btn
            if i % 4 == 0:
                self.scroll_by_amount(0, 310)
            time.sleep(0.2)

        # assertion  if the sub total price is correct
        assert self.get_text(test_data.cart.SUB_TOTAL_PRICE) == "$ 20105.00"

    def remove_all_product_in_cart(self):
        time.sleep(2)

        #get how many products in the cart
        bag_quantity = self.get_text(test_data.cart.CART_QUANTITY)

        #loop for removing products in a cart
        for product in range(1, int(bag_quantity) + 1):
            remove_btn = self.wait_clickable(test_data.cart.REMOVE_CART_PRODUCTS)
            self.action_click(remove_btn)
            time.sleep(0.1)

        time.sleep(1)

        #checking when no products found in the cart it should show the below text
        assert self.get_text(test_data.cart.SUB_TOTAL_PRICE) in "$ 0.00"
        assert self.get_text(test_data.cart.SHELF_EMPTY).replace('<br>', '\n') in "Add some products in the bag\n:)"
        assert self.get_text(test_data.cart.CONTINUE_BTN_TEXT) in "CONTINUE SHOPPING"

        time.sleep(0.5)
        self.wait_clickable(test_data.cart.CLOSE_BTN).click()

    def verify_favorites_functionalities(self):
        time.sleep(2)


        #loop to click all products favorite icon
        for i in range(1, 26):
            FAVORITE_ICON_XPATH = By.CSS_SELECTOR, f"div[id='{i}'] button[aria-label='delete']"

            favorite_icon = self.wait_presence(FAVORITE_ICON_XPATH)

            #click the favorite icon
            self.action_click(favorite_icon)
            time.sleep(0.3)

            # Scroll after clicking the 4th product by row
            if i % 4 == 0:
                self.scroll_by_amount(0, 300)
                time.sleep(0.3)

        time.sleep(1)



