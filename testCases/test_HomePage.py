from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from Configurations.Config import testdata
import pytest

class Test_HomePage:

    email= testdata.user_email
    password= testdata.user_password

    @pytest.fixture(scope="function")
    def setup(self, appium_driver_setup):

        self.driver = appium_driver_setup

    def test_HomePage(self, setup):

        self.lp = LoginPage(self.driver)

        self.lp.enterEmail(self.email)

        self.lp.enterPassword(self.password)

        self.lp.clickLoginbtn()

        self.hp = HomePage(self.driver)

        self.hp.clickNews()