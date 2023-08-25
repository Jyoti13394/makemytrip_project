import time

import pytest as pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)


@pytest.fixture(autouse=True)
def setup(browser):
    if browser == 'Chrome':
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == 'Edge':
        driver = webdriver.Edge(options=edge_options)
    else:
        print("Please enter valid browser name")
    driver.get("https://makemytrip.com")
    driver.maximize_window()
    time.sleep(2)
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope='class', autouse=True)
def browser(request):
    return request.config.getoption("--browser")