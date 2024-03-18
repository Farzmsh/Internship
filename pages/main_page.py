from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class MainPage(BasePage):
    secondary = (By.XPATH, '//div[text()="Secondary"]')

    def click_secondary_option(self):
        self.click_button(*self.secondary)
        sleep(5)