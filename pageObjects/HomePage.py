from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    # class variable to store the class name of the card element
    card_class = "android.widget.ImageView"

    def __init__(self, driver):
        # store the webdriver instance
        self.driver = driver

    def clickNews(self):
        # wait for visibility of all elements with the specified class name
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, self.card_class)))
        # click the second element in the list of elements
        element[1].click()