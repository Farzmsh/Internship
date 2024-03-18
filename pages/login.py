from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class LoginPage(BasePage):
    user_name = (By.XPATH,"//input[@data-name='Email 2']")
    my_username = "farzmsh@gmail.com"
    password = (By.XPATH,"//input[@data-name='Password']")
    my_password = "Reelly"
    login_button = (By.CSS_SELECTOR,"a[class = 'login-button w-button']")

    def open_login_page(self):
        self.open_home_page("https://soft.reelly.io/sign-in")

    def user_user_name(self):
        self.find_element(*self.user_name).send_keys(*self.my_username)
        sleep(5)

    def user_password(self):
        self.find_element(*self.password).send_keys(*self.my_password)
        sleep(5)

    def click_login_button(self):
        self.click_button(*self.login_button)
        sleep(5)




