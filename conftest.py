import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# pytest -s -v --browser_name=chrome test_main_page.py
# pytest -s -v --browser_name=firefox test_main_page.py

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',
                     help="Choose lang")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    #browser.maximize_window()
    time.sleep(5)
    yield browser
    time.sleep(5)
    browser.quit()

