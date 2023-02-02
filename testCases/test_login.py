from pageObjects.LoginPage import LoginPage
from Configurations.Config import testdata
import time
import pytest

class Test_Login:

    email= testdata.user_email
    password= testdata.user_password

    @pytest.fixture(scope="function")
    def setup(self, appium_driver_setup):
        self.driver = appium_driver_setup

    def test_login(self, setup):

        self.lp = LoginPage(self.driver)

        self.lp.enterEmail(self.email)

        self.lp.enterPassword(self.password)

        self.lp.clickLoginbtn()

        time.sleep(2)

        self.lp.elementVisible()