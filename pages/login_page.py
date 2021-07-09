from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators

class LoginPage(BasePage):

    def inter_username(self):
        '''Enter username in form`s user'''
        user_form = self.browser.find_element(*LoginPageLocators.USER_FORM)
        user_form.send_keys(*LoginPageLocators.USER_NAME)
        print("\n\tEntering username")

    def inter_password(self):
        '''Enter password in form`s password'''
        password_form = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password_form.send_keys(*LoginPageLocators.PASSWORD)
        print("\n\tEnter password")

    def login_button(self):
        '''Enter login'''
        log_but = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        log_but.click()
        print("\n\tClick 'LOGIN'")

    def should_be_login_form(self):
        """Checking the presence of the login form"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def add_cart(self):
        """Checking the add to cart function"""
        add = self.browser.find_element(*MainPageLocators.ADD_BACKPACK)
        add.click()
        print("\n\tClick 'Add to cart'")

