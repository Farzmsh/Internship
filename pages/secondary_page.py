from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


class Secondary(BasePage):
    secondary = (By.XPATH, '//div[text()="Listings"]')
    filter_but = (By.CSS_SELECTOR, '.filter-text')
    want_to_buy = (By.XPATH,"//div[@class = 'tag-text-filters' and text()='Want to buy']")
    apply_filter = (By.XPATH, "//a[text()='Apply filter']")

    def secondary_page_open(self,secondary):
        secondary = self.find_element(*self.secondary).text
        assert secondary in "Listings",f"{secondary} is not in Listings"
        sleep(5)
        print(f'secondary page is opened')

    def click_filter(self):
        self.click_button(*self.filter_but)
        sleep(3)

    def click_want_to_buy(self):
        self.wait_element_clickable(*self.want_to_buy)
        sleep(3)

    def click_apply_filter(self):
        self.click_button(*self.apply_filter)
        sleep(3)

    def verify_want_to_buy_tag(self):
        tags = self.find_elements( By.XPATH, '//div[@wized="saleTagMLS" and text()="Want to buy"]' )
        cards = self.find_elements( By.CLASS_NAME, 'for-sale-block' )
        assert len( tags ) == len( cards ), "Number of tags does not match number of cards"
        return True

    def navigate_to_next_page(self):
        next_button = WebDriverWait( self.driver, 10 ).until(
            EC.element_to_be_clickable( (By.CSS_SELECTOR, 'a.pagination__button') ) )
        next_button.click()

    def all_cards_have_want_to_buy_tag(self):
        total_pages_element = self.find_element( By.XPATH, '//div[@wized="totalPageProperties"]' )
        total_pages = int( total_pages_element.text )
        print( 'Total pages:', total_pages )

        for page_number in range( 1, total_pages + 1 ):
            assert self.verify_want_to_buy_tag(), f"Not all cards have the 'Want to buy' tag on page {page_number}."
            self.navigate_to_next_page()

