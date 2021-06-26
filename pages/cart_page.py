from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):

    def name_cart(self):
        '''The transition to the cart'''
        assert self.is_element_present(*CartPageLocators.HEADER_CART), "The cart is not opened"
        print("\n\tCart page is opened")

    def full_cart(self):
        '''Checking add to cart'''
        assert self.is_element_present(*CartPageLocators.FULL_CART), "Full cart"
        print("\n\tThe cart is not empty")

    def in_cart(self):
        '''Go to cart'''
        in_cart = self.browser.find_element(*CartPageLocators.IN_CART)
        in_cart.click()
        print("\n\tGo to cart")
