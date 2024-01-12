import pytest
from selenium import webdriver
from utilities.logger_config import logger_setup

log = logger_setup(__name__)

@pytest.fixture(scope="class")
def browser_setup_and_teardown(request, browser):
    log.info("Starting browser setup")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Invalid browser option")
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver
    yield driver
    log.info("Ending with browser teardown")
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
