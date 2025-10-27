from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities import test_data

class FavouritePage(BasePage):
    def click_favourites_menu(self):
        self.wait_clickable(test_data.favourites.FAVOURTIES_BUTTON_MENU).click()
    def get_products_found(self):
        return self.get_text(test_data.favourites.PRODUCTS_FOUND)
    def get_favourite_url(self, url):
        return self.get_url(url)

    def count_favourites(self, favourite_count, increment):
        if increment:
            favourite_count +=1
            return favourite_count
        else:
            favourite_count -= 1
            return favourite_count

    def click_favourite_multiple_times(self, increment):
        favourite_count = 0 if increment else 15

        for index in range(1, 16):
            favourite_button = None
            try:
                if increment:
                    favourite_button = By.XPATH, f"(//button[@aria-label='delete'])[{index}]"
                else:
                    favourite_button = By.XPATH, f"(//button[@aria-label='delete'])[1]"

                self.action_click(favourite_button)
                favourite_count = self.count_favourites(favourite_count, increment)
            except Exception as e:
                print(f"Error clicking button {index}: {e}")
                if favourite_button:
                    try:
                        self.wait_clickable(favourite_button).click()
                        favourite_count = self.count_favourites(favourite_count, increment)
                    except Exception as retry_error:
                        print(f"Retry failed: {retry_error}")
        return favourite_count

    def verify_total_favourites_product_found(self):
        favourite_count = self.click_favourite_multiple_times(True)
        self.click_favourites_menu()

        current_url = self.get_favourite_url("https://bstackdemo.com/favourites")
        current_result_product_found = self.get_products_found()
        expected_result_product_found = f"{favourite_count} Product(s) found."

        return current_url, current_result_product_found, expected_result_product_found

    def verify_remove_favourites(self):
        self.click_favourite_multiple_times(True)
        self.click_favourites_menu()
        favourite_count =  self.click_favourite_multiple_times(False)

        current_result_product_found = self.get_products_found()
        expected_result_product_found = f"{favourite_count} Product(s) found."

        return  current_result_product_found, expected_result_product_found


