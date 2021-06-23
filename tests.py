import time
from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage

def test_login_page(browser):
    '''Сhecking the login page'''
    link = "https://www.saucedemo.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form
    page.inter_username()
    page.inter_password()
    page.login_button()
    print("\n\tLogin form is here")

def test_main_page(browser):
    '''Checking the transition to the product page'''
    link = "https://www.saucedemo.com/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.inter_username()
    login_page.should_be_login_form
    login_page.inter_password()
    login_page.login_button()
    mainpage = MainPage(browser, link)
    mainpage.main_page()

def test_name_cart(browser):
    '''Checking the transition to the page`s cart'''
    link = "https://www.saucedemo.com/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.inter_username()
    login_page.should_be_login_form
    login_page.inter_password()
    login_page.login_button()
    time.sleep(2)
    add_to_cart = browser.find_element_by_xpath('//*[@id="shopping_cart_container"]')
    add_to_cart.click()
    name = CartPage(browser,link)
    name.name_cart()

def test_product_page(browser):
    '''Checking the transition to the page`s product'''
    link = "https://www.saucedemo.com/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.inter_username()
    login_page.should_be_login_form
    login_page.inter_password()
    login_page.login_button()
    product = browser.find_element_by_xpath('//*[@id="item_4_img_link"]/img')
    product.click()
    product = ProductPage(browser, link)
    product.product_name()

def test_add_to_cart(browser):
    '''Checking add to cart'''
    link = "https://www.saucedemo.com/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.inter_username()
    login_page.should_be_login_form
    login_page.inter_password()
    login_page.login_button()
    add_to_cart = browser.find_element_by_xpath('//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart.click()
    check_add_to_cart = CartPage(browser, link)
    check_add_to_cart.full_cart()




