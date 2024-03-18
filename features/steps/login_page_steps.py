from behave import given, when, then


@given("Open the main page")
def open_login_page(context):
    context.app.login.open_login_page()


@given("Log in to the page")
def login_steps(context):
    context.app.login.user_user_name()
    context.app.login.user_password()
    context.app.login.click_login_button()


