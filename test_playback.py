import os
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    # adapted from https://www.blazemeter.com/blog/improve-your-selenium-webdriver-tests-with-pytest
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1024x800')
    web_driver = webdriver.Remote(
        command_executor='http://hub:4444/wd/hub',
        desired_capabilities=options.to_capabilities()
    )
    yield web_driver
    web_driver.quit()


def test_setup():
    assert True

def test_selenium(driver):
    driver.get("http://example.com")
    screenshot_path = os.path.join('./screenshots', "screenshot.png")
    driver.save_screenshot(screenshot_path)

