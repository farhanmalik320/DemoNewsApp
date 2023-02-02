from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    input_field_class= "android.widget.EditText"
    login_btn_xpath= '//android.widget.Button[@content-desc="Login"]'

    def __init__(self, driver):
        self.driver = driver

    def enterEmail(self, email):
        """
        Enter email address into the email field
        """
        email_field = self.driver.find_elements(By.CLASS_NAME, self.input_field_class)
        email_field[0].click()
        email_field[0].send_keys(email)

    def enterPassword(self, password):
        """
        Enter password into the password field
        """
        password_field = self.driver.find_elements(By.CLASS_NAME, self.input_field_class)
        password_field[1].click()
        password_field[1].send_keys(password)

    def clickLoginbtn(self):
        """
        Click on the login button
        """
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def elementVisible(self):
        """
        Check if the element with the xpath "//android.view.View[@content-desc='Top Headlines']" is visible.
        If the element is visible, print "Loggined successfully".
        If the element is not visible, print "User not loggined".
        If the element is not found, print "Element not found".
        """
        try:
            element = self.driver.find_element(By.XPATH, "//android.view.View[@content-desc='Top Headlines']")
            if element.is_displayed():
                print("Loggined successfully")
            else:
                print("User not loggined")
        except:
            print("Element not found")
