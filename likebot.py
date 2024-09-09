from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to your ChromeDriver executable
CHROMEDRIVER_PATH = '/path/to/chromedriver'

# Function to like a post using a TikTok account
def like_post(account, post_url):
    options = Options()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Open TikTok login page
        driver.get('https://www.tiktok.com/login')

        # Log in
        time.sleep(5)  # Wait for the page to load

        # Click on login method (e.g., email)
        login_method = driver.find_element(By.XPATH, '//button[text()="Use phone / email / username"]')
        login_method.click()
        time.sleep(3)

        email_field = driver.find_element(By.NAME, 'email')  # Adjust the selector as needed
        password_field = driver.find_element(By.NAME, 'password')
        email_field.send_keys(account['username'])
        password_field.send_keys(account['password'])
        password_field.send_keys(Keys.RETURN)

        # Wait for login to complete
        time.sleep(10)

        # Open the post page
        driver.get(post_url)
        time.sleep(5)  # Wait for the post to load

        # Click the like button
        like_button = driver.find_element(By.XPATH, '//div[@data-e2e="like-icon"]')  # Adjust XPath as needed
        like_button.click()
        time.sleep(2)

    finally:
        # Close the browser
        driver.quit()

# List of accounts
accounts = [
    {'username': 'email1@example.com', 'password': 'password1'},
    {'username': 'email2@example.com', 'password': 'password2'},
    # Add more accounts as needed
]

# URL of the post to like
post_url = 'https://www.tiktok.com/@user/video/1234567890'

# Iterate over accounts and like the post
for account in accounts:
    like_post(account, post_url)
    time.sleep(10)  # Wait between account interactions to avoid rate limits
