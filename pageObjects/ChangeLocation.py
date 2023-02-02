import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChangeLocation:
    # variable to store the class name of the location icon element
    click_location_icon_class = "android.widget.Button"
    # variable to store the xpath of the location element
    click_location_xpath = '//android.widget.Button[@content-desc="ae"]'
    # variable to store location text
    get_selected_location_text_xpath= '//android.widget.Button[@content-desc="AE"]'

    def __init__(self, driver):
        # store the webdriver instance
        self.driver = driver

    def clickIcon(self):
        # wait for visibility of all elements with the specified class name
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, self.click_location_icon_class)))
        # click the first element in the list of elements
        element[0].click()

    def clickLocation(self):
        # initialize the element variable
        element = None
        # keep scrolling until the location element is found
        while element is None:
            try:
                # try to find the location element
                element = self.driver.find_element(By.XPATH, self.click_location_xpath)
            except:
                # if the location element is not found, swipe up the screen
                size = self.driver.get_window_size()
                x1 = size['width'] * 0.5
                y1 = size['height'] * 0.8
                y2 = size['height'] * 0.2
                self.driver.swipe(x1, y1, x1, y2)
                # wait for 5 seconds before trying again
                time.sleep(5)

        # click the location element
        element.click()

    def getlocationText(self):

        # wait for visibility of element with the specified xpath
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.get_selected_location_text_xpath)))
        location_name= self.driver.find_element(By.XPATH, self.get_selected_location_text_xpath)
        tag_name = location_name.tag_name
        return tag_name