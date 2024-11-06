from selenium import webdriver
from selenium.webdriver.common.by import By

chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option(name="detach", value=True)

chrome_driver = webdriver.Chrome(options=chrom_options)
chrome_driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = chrome_driver.find_element(By.NAME, value="fName")
last_name = chrome_driver.find_element(By.NAME, value="lName")
email = chrome_driver.find_element(By.NAME, value="email")
submit = chrome_driver.find_element(By.TAG_NAME, value="button")

first_name.send_keys("Ahmed")
last_name.send_keys("Hussein")
email.send_keys("ahmedhessian56@gmail.com")
submit.click()
