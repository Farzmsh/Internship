from behave import when,then


@when("Verify the Secondary page opens")
def secondary_page_open(self):
    self.app.secondary_page.secondary_page_open("Listings")


@then("Filter the products by want to buy")
def filter_products_by_to_buy(self):
    self.app.secondary_page.click_filter()
    self.app.secondary_page.click_want_to_buy()
    self.app.secondary_page.click_apply_filter()


@then("Verify all cards have “want to buy” tag")
def all_cards_have_want_to_buy_tag(self):
    self.app.secondary_page.all_cards_have_want_to_buy_tag()
