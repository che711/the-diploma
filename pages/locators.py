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
