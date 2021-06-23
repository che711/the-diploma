from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def product_name(self):
        '''Checking the availability of the product name on the page'''
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "The cart is not opened"
        print("\n\tProduct page is open")

    def product_availability(self):
        '''Product availability on the page'''
        assert self.is_element_present(*ProductPageLocators.PRODUCT_AVAILABILITY), "Product is not found"
        print("\n\tProduct is on the page")


