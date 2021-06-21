from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def inter_username(self):
        '''Enter username in form`s user'''
        user_form = self.browser.find_element(*LoginPageLocators.USER_FORM)
        user_form.send_keys(*LoginPageLocators.USER_NAME)

    def inter_password(self):
        '''enter password in form`s password'''
        password_form = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password_form.send_keys(*LoginPageLocators.PASSWORD)

    def login_button(self):
        '''Enter login'''
        log_but = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        log_but.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"


    # def should_be_login_url(self):
    #     assert (self.url in self.browser.current_url), "Login is not found in current url"
    #

    #
    # def should_be_register_form(self):
    #     assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not found"
    #
