from .base_page import BasePage
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

    def name_in_main_page(self):
        """Find out the name of the product in the shopping cart"""
        product_name = self.browser.find_element(*MainPageLocators.FIND_NAME)
        text_name1 = product_name.text
        print("\n\tThe product name on the main page: ", text_name1)
        return text_name1



