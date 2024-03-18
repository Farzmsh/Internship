from behave import when


@when ("Click on Secondary option at the left side menu")
def click_secondary_option(self):
    self.app.main_page.click_secondary_option()