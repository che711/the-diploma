from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//*[@id="login_button_container"]')
    USER_NAME = "standard_user"
    USER_FORM = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD = "secret_sauce"
    PASSWORD_FORM = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')

class MainPageLocators():
    HEADER = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    ADD_TO_PRODUCT = (By.XPATH, '//*[@id="item_4_title_link"]')

class CartPageLocators():
    HEADER_CART = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    ADD_TO_CART = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    EMPTY_CART = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    FULL_CART = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    IN_CART = (By.XPATH, '//*[@id="shopping_cart_container"]')

class ProductPageLocators():
    PRODUCT_NAME = (By.XPATH,'//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    PRODUCT_AVAILABILITY = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')

