import os
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

ACCOUNT_EMAIL = "my_email@test.com"  # The email you registered with
ACCOUNT_PASSWORD = "my_password"  # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"

options = webdriver.ChromeOptions()

options.add_argument("--disable-password-manager-reauthentication")
options.add_argument("--disable-features=VizDisplayCompositor")
options.add_argument("--disable-save-password-bubble")
options.add_argument("--disable-password-generation")
options.add_argument("--disable-password-manager")
options.add_argument("--password-store=basic")

options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.default_content_setting_values.notifications": 2,
    "profile.default_content_settings.popups": 0,
    "autofill.profile_enabled": False,
    "autofill.credit_card_enabled": False,
    "profile.password_manager_leak_detection": False
})

# Exclude automation switches that might interfere
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=options)


def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")

        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

    return None


def list_bookings(section, card_name, wait):
    section_name = "Confirmed Bookings" if section == "confirmed-bookings-section" else "Waitlist"

    try:
        confirmed = wait.until(ec.presence_of_element_located((By.ID, f"{section}")))
        cards = confirmed.find_elements(By.CSS_SELECTOR, f"div[id^='{card_name}']")

        print(f"_____{section_name}_____")

        for card_op in cards:
            print(card_op.text)
            print("_" * 20)
    except TimeoutException:
        print(f"No _____{section_name}_____")


def main():
    driver.get(GYM_URL)

    wait = WebDriverWait(driver, timeout=10)
    login_button = wait.until(ec.presence_of_element_located((By.ID, "login-button")))

    login_button.click()

    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))

    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = wait.until(ec.presence_of_element_located((By.ID, "password-input")))

    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_button = wait.until(ec.presence_of_element_located((By.ID, "submit-button")))

    submit_button.click()

    day_groups = wait.until(
        ec.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "[id^='day-group'][id*='tue'], [id^='day-group'][id*='thu']")
        )
    )

    for day_group in day_groups:
        class_cards = day_group.find_elements(By.CSS_SELECTOR, "div[id$='1800']")

        if class_cards:
            for card in class_cards:
                button = card.find_element(By.TAG_NAME, "button")

                if button.text in ["Book Class", "Join Waitlist"]:
                    button.click()
                    print(card.text)
                    print("_" * 20)

    my_bookings_link = wait.until(ec.presence_of_element_located((By.ID, "my-bookings-link")))

    my_bookings_link.click()
    list_bookings("confirmed-bookings-section", "booking-card", wait)
    list_bookings("waitlist-section", "waitlist-card", wait)


if __name__ == "__main__":
    retry(main, description="GYM_URL")
