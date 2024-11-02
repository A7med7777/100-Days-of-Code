import os
import requests
import smtplib

from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

USER_EMAIL = os.getenv("EMAIL_ADDRESS")
USER_PASS = os.getenv("EMAIL_PASSWORD")
BUY_PRICE = 100

# url = "https://appbrewery.github.io/instant_pot/"
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 "
                  "Safari/537.36",

    "Accept-Language": "en-US,en;q=0.9",
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.select_one("span#productTitle").get_text().strip()
    price = soup.select_one("span.a-price > span").get_text()
    float_price = float(price.split("$")[1])
except (AttributeError, IndexError, ValueError, requests.exceptions.RequestException):
    print("Error: Unable to retrieve product details.")
else:
    if float_price <= BUY_PRICE:
        with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), port=587) as connection:
            message = f"{title} is on sale for {price}!"

            connection.starttls()
            connection.login(user=USER_EMAIL, password=USER_PASS)
            connection.sendmail(
                from_addr=USER_EMAIL,
                to_addrs=USER_EMAIL,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
            )
