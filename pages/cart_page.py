from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):

    def name_cart(self):
        '''The transition to the cart'''
        assert self.is_element_present(*CartPageLocators.HEADER_CART), "The cart is not opened"
        print("\n\tCart page is opened")