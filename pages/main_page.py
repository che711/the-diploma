from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):

    def main_page(self):
        '''Test main page'''
        assert self.is_element_present(*MainPageLocators.HEADER), "Main page is not opened"
        print("\n\tMain page is open")

    def to_product_page(self):
        '''The transition to the product page'''
        add = MainPageLocators.ADD_TO_PRODUCT
        add.click()


    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

