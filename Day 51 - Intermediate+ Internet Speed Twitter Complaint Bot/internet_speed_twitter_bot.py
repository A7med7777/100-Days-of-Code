import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 20


class InternetSpeedTwitterBot:
    def __init__(self):
        self.speedtest_website = "https://fast.com/"
        self.login = "https://x.com/i/flow/login"
        self.driver = webdriver.Chrome()
        self.speed_value = 0
        self.speed_units = ""

    def get_internet_speed(self):
        self.driver.get(self.speedtest_website)
        time.sleep(60)
        self.speed_value = float(self.driver.find_element(By.ID, value="speed-value").text)
        self.speed_units = self.driver.find_element(By.ID, value="speed-units").text

    def tweet_at_provider(self):
        if PROMISED_DOWN < self.speed_value:
            self.driver.get(self.login)
            self.driver.implicitly_wait(5.0)

            login = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div['
                      '4]/label/div/div[2]/div/input'
            )

            login.send_keys("a7med_7ussein7")
            login.send_keys(Keys.RETURN)

            password = self.driver.find_element(
                By.XPATH,
                value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div['
                      '1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
            )

            password.send_keys(os.getenv("PASS"))
            password.send_keys(Keys.RETURN)

            tweet = (f"Hey Internet Provider, why is my internet speed {self.speed_value} {self.speed_units} down "
                     f"when I pay for {PROMISED_DOWN} down?")

            tweet_input = self.driver.find_element(
                By.XPATH,
                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div['
                      '1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div['
                      '1]/div/div/div/div/div/div[2]/div/div/div/div'
            )

            tweet_input.send_keys(tweet)
            tweet_input.send_keys(Keys.RETURN)
