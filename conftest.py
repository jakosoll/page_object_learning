import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store', default="False", help="Choose headless mode: True or False")
    parser.addoption('--language', action='store', default="en", help="Choose language of testing site")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")
    language = request.config.getoption("language")

    if browser_name == 'chrome':
        options = ChromeOptions()
        if headless == "True":
            options.add_argument("headless")
            print("Chrome will start in headless mode")
        if language:
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            print(f'Accept language is "{language}"')
        print('\n Starting Chrome for test...')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        if headless == "True":
            options.add_argument("--headless")
            print("Firefox will start in headless mode")
        if language:
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", language)
            browser = webdriver.Firefox(firefox_profile=fp, options=options)
            print(f'Accept language is "{language}"')
        else:
            browser = webdriver.Firefox(options=options)
            print('\n Starting Firefox for test...')
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    # browser.wait = WebDriverWait(browser, 15)
    # browser.implicitly_wait(15)
    yield browser
    print("\nQuit browser...")
    browser.quit()
