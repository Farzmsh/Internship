
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from app.application import Application
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

def browser_init(context):
    """
    :param context: Behave context
    """

    # # HEADLESS MODE ####

    # options = webdriver.ChromeOptions()
    # options.add_argument( 'headless' )
    # service = Service( ChromeDriverManager().install() )
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # # Chrome MODE ####
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)


    # # Firefox MODE ####
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'farzanehmashayek_sNmfcb'
    # bs_key = '19yEzSWU8myQtsquQGSA'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '11',
    #     'browserName': 'Chrome',
    #     'sessionName': "User can filter the Secondary deals by “want to buy” option"
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver,15)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()



