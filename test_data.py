from selenium.webdriver.common.by import By

BASE_URL = "https://bstackdemo.com/signin"

USERNAME = "demouser"
PASSWORD = "testingisfun99"
class signin:
    USERNAME = By.XPATH, "//div[@class=' css-2b097c-container' and @id='username']"
    PASSWORD = By.XPATH, "//div[@class=' css-2b097c-container' and @id='password']"
    LOGIN_BTN = By.XPATH, "//button[@id='login-btn']"


class homepage:

    FAVOURITES_MENU = By.XPATH, "//a[@href='/favourites']"


class favourites:
    PRODUCTS_FOUND = By.XPATH, "//small[@class='products-found']/span"



class cart:
    SUB_TOTAL_PRICE = By.XPATH, "//p[@class='sub-price__val']"
    CLOSE_BTN = By.XPATH, "//div[@class='float-cart__close-btn']"
    CART_QUANTITY = By.XPATH, "//span[@class='bag__quantity']"
    CHECK_OUT = By.XPATH, "//div[@class='buy-btn' and text() ='Checkout']"
    CONTINUE_BTN_TEXT = By.XPATH, "//div[@class='float-cart__footer']/div[@class='buy-btn']"
    SHELF_EMPTY = By.XPATH, "//p[@class='shelf-empty']"
    REMOVE_CART_PRODUCTS = By.XPATH, "(//div[@class='shelf-item__del'])[1]"

    CART_CLOSED = By.XPATH, "//span[@class='bag bag--float-cart-closed']"
class checkout:
    FIRST_NAME = By.XPATH, "//input[@id='firstNameInput']"
    LAST_NAME = By.XPATH, "//input[@id='lastNameInput']"
    ADDRESS = By.XPATH, "//input[@id='addressLine1Input']"
    PROVINCE = By.XPATH, "//input[@id='provinceInput']"
    POSTAL = By.XPATH, "//input[@id='postCodeInput']"
    SUBMIT = By.XPATH, "//button[@id='checkout-shipping-continue']"
    NUMBER_OF_ITEMS = By.CSS_SELECTOR, ".cart-section-heading.optimizedCheckout-contentPrimary"
    CONTINUE_SHOP = By.XPATH, "//button[normalize-space()='Continue Shopping »']"