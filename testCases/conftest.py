import pytest
from appium import webdriver

@pytest.fixture(scope="function")
def appium_driver_setup(request):
    desiredcap = {
        "platformName": "Android",
        "appium:platformVersion": "11.0",
        "appium:deviceName": "Poco X3 NFC",
        "appium:appPackage": "com.example.demo_news",
        "appium:appActivity": "com.example.demo_news.MainActivity",
        "no:sign": "true",
        "noReset": "true"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredcap)
    yield driver
    driver.quit()