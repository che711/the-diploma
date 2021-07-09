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

    def add_product(self):
        """Adding product to cart"""
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()
        print("\n\tAdding to cart")

    def check_product(self):
        """Check Product"""
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE)
        product.click()







