from pages.main_page import MainPage
from pages.login_page import LoginPage


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
    link = "https://www.saucedemo.com/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.inter_username()
    login_page.should_be_login_form
    login_page.inter_password()
    login_page.login_button()
    main_page = MainPage(browser, link)
    main_page.main_page()
   # main_page.to_product_page()


#
# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
# def test_login_form(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
#     page = LoginPage (browser, link)
#     page.open()
#     page.should_be_login_form
#
# def test_should_be_login_url(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_url()
#
# def test_register_form(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_register_form
#
# def test_should_be_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_page
#
