from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_not_be_success_message_two(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"




    def push_add_to_basket(self):
        '''Нажимаем на кнопку "Add to basket"'''
        add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        add_basket.click()
        promt = BasePage(self.browser, self.url)
        promt.solve_quiz_and_get_code()

    def name_book(self):
        '''Находим название книги'''
        name = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        book = name.text
        print(f"\n\tThe book`s name: {book}")

    def add_names_book(self):
        '''Находим называние, добавленной в корзину книги'''
        name2 = self.browser.find_element(*ProductPageLocators.ADD_NAME_BOOK)
        book2 = name2.text
        print(f"\n\tBook in basket: {book2}")

    def price_book(self):
        '''Находим цену книги'''
        css_price =  self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        price = css_price.text
        print(f"\n\tThe book`s price: {price}")

    def add_price_book(self):
        '''Находим цену книги, добавленной в корзину'''
        css_price = self.browser.find_element(*ProductPageLocators.ADD_PRICE_BOOK)
        price = css_price.text
        print(f"\n\tThe basket`s price: {price}")









