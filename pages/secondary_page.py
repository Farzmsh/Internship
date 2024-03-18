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
    all_cards = (By.XPATH, "//div[@wized='saleTagMLS']")
    want_to_buy_tag = (By.XPATH, "//div[text()='Want to buy']")
    next_page = (By.XPATH, "//a[@wized='nextPageMLS']")
    last_page = (By.XPATH, "//div[@wized='totalPageProperties' and @class='page-count']/text()")
    first_page = (By.XPATH, "//div[@wized='currentPageProperties' and @class='page-count']/text()" )

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

    # def all_cards_have_want_to_buy_tag(self):
    #     want_to_buy = []
    #     while True:
    #
    #         if self.first_page <= self.last_page:
    #             print(self.first_page)
    #             print(self.last_page)
    #             self.driver.execute_script("window.scrollBy(0,2000)", "")
    #             sleep(2)
    #             want_to_buy_all_pages = self.driver.find_elements(*self.want_to_buy_tag)
    #             want_to_buy.extend(want_to_buy_all_pages)
    #             self.click_button(*self.next_page)
    #             sleep(5)
    #         else:
    #             break
    #     print(want_to_buy)
    #     for element in want_to_buy:
    #         tag_text = element.text
    #         print(tag_text)
    #         assert tag_text, f"want to buy is not in {tag_text}"

    def all_cards_have_want_to_buy_tag(self):

        for card in self.all_cards:
            tags = self.find_elements(*self.want_to_buy_tag)
            print(tags.text)
            want_to_buy_tag_present = False
            for tag in tags:
                if tag.text == "want to buy":
                    want_to_buy_tag_present = True
                    break
            if not want_to_buy_tag_present:
                print("Not all cards have 'want to buy' tag.")
                break
        else:
            print("All cards have 'want to buy' tag.")





