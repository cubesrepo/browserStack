import time

from selenium.webdriver.common.by import By

import test_data
from pages.base_page import BasePage


class FavouritesPage(BasePage):


    def verify_lists_of_favourites(self):

        #click favorites menu
        favourites_menu = self.wait_clickable(test_data.homepage.FAVOURITES_MENU)
        self.action_click(favourites_menu)

        time.sleep(2)

        #assert page url
        assert self.url_is("https://bstackdemo.com/favourites")

        #assert number of products found
        assert self.get_text(test_data.favourites.PRODUCTS_FOUND) == "25 Product(s) found."


    def add_to_cart_and_check_out_all_products_in_favourites(self):
        time.sleep(2)
        #check if the add to cart badge is zero
        assert self.get_text(test_data.cart.CART_QUANTITY) == "0"

        #loop for clicking add to cart btn for all products
        for i in range(1, 26):

            add_to_cart_product = By.CSS_SELECTOR, f"div[id='{i}'] div[class='shelf-item__buy-btn']"
            print(add_to_cart_product)
            #wait for presence of addtocart
            try:
                add_to_cart_btn = self.wait_presence(add_to_cart_product)
            except:

                add_to_cart_btn = self.wait_clickable(add_to_cart_product)


            #move to element addtocart btn
            self.hover(add_to_cart_btn)
            #click add to cart btn
            add_to_cart_btn.click()

            time.sleep(0.2)

            #close the cart panel after clicking the 3rd product in each row
            if i % 4 == 3:
                self.wait_clickable(test_data.cart.CLOSE_BTN).click()
                time.sleep(0.3)

            #scroll to the add to cart btn
            if i % 4 == 0:
                self.scroll_by_amount(0, 310)
            time.sleep(0.3)

        #assertion  if the sub total price is correct
        assert self.get_text(test_data.cart.SUB_TOTAL_PRICE) == "$ 20105.00"

        time.sleep(1)

        #click checkout
        checkout = self.wait_clickable(test_data.cart.CHECK_OUT)
        self.action_click(checkout)


