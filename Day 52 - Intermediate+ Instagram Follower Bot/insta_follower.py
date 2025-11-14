import time
from typing import Any

from selenium import webdriver
from selenium.common import (
    ElementNotInteractableException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)  # type: ignore
        # Add these options to appear less bot-like
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # type: ignore
        chrome_options.add_experimental_option("useAutomationExtension", False)  # type: ignore

        self.driver = webdriver.Chrome(options=chrome_options)
        errors: list[Any] = [NoSuchElementException, ElementNotInteractableException]

        self.wait = WebDriverWait(
            self.driver, timeout=10, poll_frequency=0.5, ignored_exceptions=errors
        )

    def login(self, phone: str, password: str):
        """Login to Instagram via Facebook"""
        self.driver.get("https://www.instagram.com/accounts/login/")

        # Wait for page to load
        time.sleep(3)

        try:
            # Try to find and click "Log in with Facebook" button
            log_in_with_facebook = self.wait.until(
                ec.element_to_be_clickable(
                    (By.XPATH, '//span[contains(text(), "Log in with Facebook")]')
                )
            )
            log_in_with_facebook.click()

            # Wait for Facebook login page
            time.sleep(2)

            # Enter Facebook credentials
            facebook_email = self.wait.until(
                ec.presence_of_element_located((By.ID, "email"))
            )
            facebook_password = self.wait.until(
                ec.presence_of_element_located((By.ID, "pass"))
            )

            facebook_email.send_keys(phone)
            facebook_password.send_keys(password)

            # Click login button
            facebook_loginbutton = self.wait.until(
                ec.element_to_be_clickable((By.ID, "loginbutton"))
            )
            facebook_loginbutton.click()

            print(
                "Login submitted. Please complete any manual verification if prompted..."
            )

            # Wait for potential reCAPTCHA or 2FA
            time.sleep(60)  # Give time for manual intervention if needed

        except TimeoutException as e:
            print(f"Timeout error during login: {e}")
            print("Current URL:", self.driver.current_url)
            print("Consider solving CAPTCHA manually or using direct Instagram login")

    def login_direct(self, username: str, password: str):
        """Alternative: Direct Instagram login (may be more reliable)"""
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        try:
            # Find username and password fields
            username_input = self.wait.until(
                ec.presence_of_element_located((By.NAME, "username"))
            )
            password_input = self.wait.until(
                ec.presence_of_element_located((By.NAME, "password"))
            )

            # Enter credentials
            username_input.send_keys(username)
            password_input.send_keys(password)

            # Click login button
            login_button = self.wait.until(
                ec.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
            )
            login_button.click()

            print("Login submitted. Waiting for page to load...")
            time.sleep(5)

            # Handle "Save Your Login Info" prompt if it appears
            try:
                not_now_button = self.driver.find_element(
                    By.XPATH, '//button[contains(text(), "Not now")]'
                )
                not_now_button.click()
            except NoSuchElementException:
                pass

            # Handle notifications prompt if it appears
            try:
                not_now_button = self.driver.find_element(
                    By.XPATH, '//button[contains(text(), "Not Now")]'
                )
                not_now_button.click()
            except NoSuchElementException:
                pass

            print("Login completed!")

        except TimeoutException as e:
            print(f"Timeout error during direct login: {e}")
            print("Current URL:", self.driver.current_url)

    def find_followers(self, account_url: str):
        """Navigate to an account and find its followers"""
        self.driver.get(account_url)
        time.sleep(3)

        try:
            # Click on any <a> tag that contains "followers" in its href
            followers_link = self.wait.until(
                ec.element_to_be_clickable(
                    (By.XPATH, '//a[contains(@href, "/followers")]')
                )
            )
            followers_link.click()
            time.sleep(2)

            print("Opened followers list")

            modal_xpath = "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
            modal = self.wait.until(
                ec.presence_of_element_located((By.XPATH, modal_xpath))
            )
            for _ in range(10):
                # In this case we're executing some Javascript, that's what the execute_script() method does.
                # The method can accept the script as well as an HTML element.
                # The modal in this case, becomes the arguments[0] in the script.
                # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
                self.driver.execute_script(  # type: ignore
                    "arguments[0].scrollTop = arguments[0].scrollHeight", modal
                )
                time.sleep(2)

        except TimeoutException:
            print("Could not find followers link")

    def follow(self):
        """Follow users from the followers list"""
        try:
            # Find all "Follow" buttons in the modal
            follow_buttons = self.wait.until(
                ec.presence_of_all_elements_located(
                    (By.XPATH, '//div[text()="Follow"]')
                )
            )

            print(f"Found {len(follow_buttons)} users to follow")

            for button in follow_buttons:
                try:
                    button.click()
                    time.sleep(2)  # Delay to avoid rate limiting
                    print("Followed a user")
                except Exception as e:
                    print(f"Could not follow user: {e}")

        except Exception as e:
            print(f"Error during following: {e}")

    def close(self):
        """Close the browser"""
        self.driver.quit()
