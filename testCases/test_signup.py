from pageObjects.SignupPage import SignupPage
from Configurations.Config import testdata
import pytest

class Test_Signup:

    name= testdata.user_name
    email = testdata.user_email
    password = testdata.user_password

    @pytest.fixture(scope="function")
    def setup(self, appium_driver_setup):
        self.driver = appium_driver_setup
    def test_signup(self, setup):
        self.lp = SignupPage(self.driver)
        self.lp.clickMainSignup()
        self.lp.enterName(self.name)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickSignup()