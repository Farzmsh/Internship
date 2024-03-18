from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait( self.driver, 15 )

    def open_home_page(self, url):
        self.driver.get(url)

    def find_element(self,*locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click_button(self,*locator):
        self.find_element(*locator).click()

    def wait_element_clickable(self,*locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        message = f"Element {locator} is not clickable").click()






