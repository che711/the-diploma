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

    def product_name_in_cart(self):
        """Find out the name of the product in the shopping cart"""
        cart_product_name = self.browser.find_element_by_xpath('//*[@id="item_4_title_link"]/div')
        text_name2 = cart_product_name.text
        print("\n\tThe product name on the cart: ", text_name2)
        return text_name2
