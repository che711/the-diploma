from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//*[@id="login_button_container"]')
    USER_NAME = "standard_user" #(By.XPATH, "//*[@id="login_credentials"]/text()[1]")
    USER_FORM = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD = "secret_sauce" #
    PASSWORD_FORM = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')

class MainPageLocators():
    HEADER = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    ADD_TO_PRODUCT = (By.XPATH, '//*[@id="item_4_title_link"]')

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn-lg:nth-child(3)")
    NAME_BOOK = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    ADD_NAME_BOOK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_BOOK = (By.CSS_SELECTOR, 'p.price_color:nth-child(2)')
    ADD_PRICE_BOOK = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
