import os
import pandas
import datetime
import random
import smtplib

EMAIL = os.getenv("MY_EMAIL")
PASS = os.getenv("MY_PASSWORD")

birthdays = pandas.read_csv("./birthdays.csv")
today = datetime.datetime.today()

for index, row in birthdays.iterrows():
    if row.month == today.month and row.day == today.day:
        try:
            with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as file:
                letter = file.read().replace("[NAME]", row['name'])

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASS)
                connection.sendmail(from_addr=EMAIL, to_addrs=row.email, msg=f"Subject:Happy Birthday!\n\n{letter}")
                print(f"Email sent to {row['name']} at {row.email}")
        except FileNotFoundError:
            print(f"Template file not found.")
        except Exception as e:
            print(f"Failed to send email: {e}")
