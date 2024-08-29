import requests
from datetime import datetime, timezone
import smtplib
import os
import time

EMAIL = os.getenv("MY_EMAIL")
PASS = os.getenv("MY_PASSWORD")
MY_LAT = float(os.getenv("MY_LAT"))
MY_LONG = float(os.getenv("MY_LONG"))

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_over_head():
    try:
        r = requests.get(url="http://api.open-notify.org/iss-now.json")
        r.raise_for_status()
    except requests.exceptions.RequestException as re:
        print(f"Error fetching ISS data: {re}")

        return False

    iss_data = r.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    return MY_LAT + 5 >= iss_latitude >= MY_LAT - 5 and MY_LONG + 5 >= iss_longitude >= MY_LONG - 5


def at_night():
    try:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
    except requests.exceptions.RequestException as re:
        print(f"Error fetching sunrise/sunset data: {re}")

        return False

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now(timezone.utc)

    return time_now.hour >= sunset or time_now.hour <= sunrise


while True:
    if is_over_head() and at_night():
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASS)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=EMAIL,
                    msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
                )

            print("Email sent!")
            break
        except Exception as e:
            print(f"Error sending email: {e}")

    time.sleep(60)
