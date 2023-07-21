import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    browser_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=browser_service)
    print("\nstart browser for test..")
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()
