from pageObjects.ChangeLocation import ChangeLocation
from pageObjects.LoginPage import LoginPage
from Configurations.Config import testdata
import pytest

class Test_ChangeLocation:

    email= testdata.user_email
    password= testdata.user_password

    @pytest.fixture(scope="function")
    def setup(self, appium_driver_setup):

        self.driver = appium_driver_setup

    def test_ChangeLocation(self, setup):

        self.lp = LoginPage(self.driver)

        self.lp.enterEmail(self.email)

        self.lp.enterPassword(self.password)

        self.lp.clickLoginbtn()

        self.cl= ChangeLocation(self.driver)

        self.cl.clickIcon()

        self.cl.clickLocation()

        self.actual_text= self.cl.getlocationText()

        print(self.actual_text)

        self.expected_text= 'AE'

        if self.actual_text== self.expected_text:
            print("Test case passed")

        else:
            print("Test case fail")