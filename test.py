from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open the Sign-in Page
driver = webdriver.Chrome()
driver.get("https://soft.reelly.io/sign-in")

# Step 2: Log in to the page
my_username = "farzmsh@gmail.com"
my_password = "Reelly"

username_input = driver.find_element(By.XPATH,"//input[@data-name='Email 2']")
password_input = driver.find_element(By.XPATH,"//input[@data-name='Password']")
login_button = driver.find_element(By.CSS_SELECTOR,"a[class = 'login-button w-button']")

username_input.send_keys(my_username)
password_input.send_keys(my_password)
login_button.click()

# Adjust the timeout value
wait = WebDriverWait(driver, 20)

# Step 3: Click on Secondary option at the left side menu
secondary_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'menu-button-text' and text()='Secondary']")))
secondary_option.click()

# Step 4: Verify the right page opens
# You can add verification steps here

# Step 5: Filter the products by "want to buy"
# You can add code to select the "Want to buy" option from the filter/dropdown menu

# Step 6: Verify all cards have "want to buy" tag

cards = driver.find_elements(By.XPATH, '//div[@wized="saleTagMLS" and text()="Want to buy"]')
tags = driver.find_elements(By.CLASS_NAME, 'for-sale-block')

print(f'Total cards: {len(cards)}')

next_button = WebDriverWait(driver, 10 ).until(
    EC.element_to_be_clickable( (By.CSS_SELECTOR, 'a.pagination__button') ) )
next_button.click()

next_page = driver.find_element( By.XPATH, '//div[@wized="totalPageProperties"]' )
total_pages = int( next_page.text )
print( 'Total pages:', total_pages )

for page_number in range( 1, total_pages + 1 ):
    assert cards==tags, f"Not all cards have the 'Want to buy' tag on page {page_number}."
    next_page.click()



# Close the browser
driver.quit()
