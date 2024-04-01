from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage


#  pytest -s -vv --alluredir=results tests.py

def test_login_page(browser):
    '''Сhecking the login page'''
    link = "https://www.saucedemo.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
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
    login_page.should_be_login_form()
    login_page.inter_password()
    login_page.login_button()
    mainpage = MainPage(browser, link)
    mainpage.main_page()

def test_cart_page(browser):
    '''Checking the transition to the page`s cart'''
    link = "https://www.saucedemo.com/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.inter_username()
    login_page.should_be_login_form()
    login_page.inter_password()
    login_page.login_button()
    add_to_cart = CartPage(browser, link)
    add_to_cart.in_cart()
    add_to_cart.name_cart()


def test_product_page(browser):
    '''Checking the transition to the page`s product'''
    link = "https://www.saucedemo.com/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.inter_username()
    login_page.should_be_login_form()
    login_page.inter_password()
    login_page.login_button()
    product = MainPage(browser, link)
    product.main_page()
    product = ProductPage(browser, link)
    product.check_product()
    product_page = ProductPage(browser, link)
    product_page.product_name()
    product = ProductPage(browser, link)
    product.product_availability()

def test_add_to_cart(browser):
    '''Checking add to cart'''
    link = "https://www.saucedemo.com/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.inter_username()
    login_page.should_be_login_form()
    login_page.inter_password()
    login_page.login_button()
    add_to_cart = LoginPage(browser, link)
    add_to_cart.add_cart()
    check_add_to_cart = CartPage(browser, link)
    check_add_to_cart.full_cart()

def test_identical_names(browser):
    '''Checking prooduct name in cart'''
    link = "https://www.saucedemo.com/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.inter_username()
    login_page.should_be_login_form()
    login_page.inter_password()
    login_page.login_button()
    product_name = MainPage(browser, link)
    product_name.name_in_main_page()
    add_to_cart = ProductPage(browser, link)
    add_to_cart.add_product()
    check_add_to_cart = CartPage(browser, link)
    check_add_to_cart.full_cart()
    name = CartPage(browser, link)
    name.in_cart()
    cart_product_name = CartPage(browser, link)
    cart_product_name.product_name_in_cart()
    assert (product_name.name_in_main_page() == cart_product_name.product_name_in_cart()), 'Different names'



