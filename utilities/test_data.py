from selenium.webdriver.common.by import By

BASE_URL = "https://bstackdemo.com/signin"

USER_CREDENTIALS = {
    "username": "demouser",
    "username_lock": "locked_user",
    "password": "testingisfun99",
    "invalid_password": "invalid password"
}
class signin:
    USERNAME = By.XPATH, "//div[@class=' css-2b097c-container' and @id='username']"
    PASSWORD = By.XPATH, "//div[@class=' css-2b097c-container' and @id='password']"
    LOGIN_BTN = By.XPATH, "//button[@id='login-btn']"

    INVALID_PASSWORD_ERROR = By.XPATH, "//h3[normalize-space()='Invalid Password']"
    ACCOUNT_LOCKED_ERROR = By.XPATH, "//h3[normalize-space()='Your account has been locked.']"


class favourites:
    FAVOURTIES_BUTTON_MENU = By.XPATH, "//strong[normalize-space()='Favourites']"
    PRODUCTS_FOUND = By.XPATH, "//small[@class='products-found']"


class cart:
    ADD_TO_CART_BTN = By.XPATH, "(//div[@class='shelf-item__buy-btn'][normalize-space()='Add to cart'])"
    CLOSE_BTN = By.XPATH, "//div[@class='float-cart__close-btn']"

    SUB_TOTAL_PRICE = By.XPATH, "//p[@class='sub-price__val']"
    CART_QUANTITY = By.XPATH, "//span[@class='bag__quantity']"
    ADD_QUANTITY = By.XPATH, "//button[normalize-space()='+']"
    CHECK_OUT = By.XPATH, "//div[@class='buy-btn' and text() ='Checkout']"
    CONTINUE_BTN_TEXT = By.XPATH, "//div[@class='float-cart__footer']/div[@class='buy-btn']"
    SHELF_EMPTY = By.XPATH, "//p[@class='shelf-empty']"
    REMOVE_CART_PRODUCTS = By.XPATH, "(//div[@class='shelf-item__del'])[1]"

    CART_CLOSED = By.XPATH, "//span[@class='bag bag--float-cart-closed']"
class checkout:
    FIRST_NAME = By.XPATH, "//input[@id='firstNameInput']"
    LAST_NAME = By.XPATH, "//input[@id='lastNameInput']"
    ADDRESS = By.XPATH, "//input[@id='addressLine1Input']"
    STATE = By.XPATH, "//input[@id='provinceInput']"
    POSTAL = By.XPATH, "//input[@id='postCodeInput']"
    SUBMIT = By.XPATH, "//button[@id='checkout-shipping-continue']"
    NUMBER_OF_ITEMS = By.CSS_SELECTOR, ".cart-section-heading.optimizedCheckout-contentPrimary"
    CONTINUE_SHOPPING = By.XPATH, "//button[normalize-space()='Continue Shopping »']"

    SUCCESSFULLY_PLACED = By.XPATH, "//legend[@id='confirmation-message']"

class order:
    ORDER_BUTTON_MENU = By.XPATH, "//strong[normalize-space()='Orders']"
    NO_ORDERS_FOUND = By.XPATH, "//h2[normalize-space()='No orders found']"
    TOTAL_PRICE = By.CSS_SELECTOR, "div[id='32'] div[class='a-box a-color-offset-background order-info'] div[class='a-row'] div:nth-child(1) div:nth-child(1) span:nth-child(1)"
    ORDER_PLACED_DATE = By.CSS_SELECTOR, "div[id='32'] div[class='a-column a-span3'] span[class='a-color-secondary value']"
    SHIP_TO = By.CSS_SELECTOR, "div[id='32'] div[class='a-box a-color-offset-background order-info'] div[class='a-row'] div:nth-child(1) div:nth-child(1) span:nth-child(1)"
