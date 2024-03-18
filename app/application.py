from pages.base_page import BasePage
from pages.login import LoginPage
from pages.main_page import MainPage
from pages.secondary_page import Secondary


class Application:
    def __init__(self,driver):
        self.base_page = BasePage(driver)
        self.login = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.secondary_page = Secondary(driver)




