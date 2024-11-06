from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = chrome_driver.find_element(By.CSS_SELECTOR, value="div#cookie")
timer = time.time()
timeout = time.time() + 60*5   # 5 minutes from now

while time.time() < timeout:
    cookie.click()

    if time.time() - 5 >= timer:
        cookie.click()
        timer = time.time()
        store = chrome_driver.find_elements(By.CSS_SELECTOR, value="div#store > div")

        for div in store[::-1]:
            cookie.click()

            if "grayed" not in div.get_attribute("class"):
                cookie.click()
                div.click()
                break

cps = chrome_driver.find_element(By.CSS_SELECTOR, value="div#cps").text.strip()
print(cps)
