import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',
                     help="Choose lang")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    #browser.maximize_window()
    time.sleep(5)
    yield browser
    time.sleep(5)
    browser.quit()

