from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    # XPath locator for the main signup button
    signup_btn_xpath= '//android.widget.Button[@content-desc="Signup"]'
    # Class name locator for the input fields
    input_field_class= "android.widget.EditText"

    def __init__(self, driver):
        # Store the WebDriver instance in an instance variable
        self.driver = driver

    def clickMainSignup(self):

        # Use the WebDriverWait to wait for the element to be clickable
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.signup_btn_xpath)))
        # Click the element
        element.click()

    def enterName(self, name):

        # Find all the elements with the given class name
        name_field = self.driver.find_elements(By.CLASS_NAME, self.input_field_class)
        # Click the first element
        name_field[0].click()
        # Send the given name to the name input field
        name_field[0].send_keys(name)

    def enterEmail(self, email):

        # Find all the elements with the given class name
        email_field = self.driver.find_elements(By.CLASS_NAME, self.input_field_class)
        # Click the second element (assumed to be the email input field)
        email_field[1].click()
        # Send the given email to the email input field
        email_field[1].send_keys(email)

    def enterPassword(self, password):

        # Find all the elements with the given class name
        password_field = self.driver.find_elements(By.CLASS_NAME, self.input_field_class)
        # Click the third element (assumed to be the password input field)
        password_field[2].click()
        # Send the given password to the password input field
        password_field[2].send_keys(password)

    def clickSignup(self):

        # Find the signup button using the XPath locator and click it
        signup_btn = self.driver.find_element(By.XPATH, self.signup_btn_xpath).click()