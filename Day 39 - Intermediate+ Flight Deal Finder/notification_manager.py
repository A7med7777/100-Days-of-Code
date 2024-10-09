from twilio.rest import Client
import smtplib
import os

MY_EMAIL = os.getenv("EMAIL")
MY_PASS = os.getenv("PASS")


class NotificationManager:
    def __init__(self):
        self.account_sid = os.getenv("ACCOUNT_SID")
        self.auth_token = os.getenv("AUTH_TOKEN")

    def send_message(self, cheapest_flight):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            from_=f'whatsapp:+{os.getenv("FROM_")}',
            body=f"Low price alert! Only £{cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to "
                 f"{cheapest_flight.destination_airport}, on {cheapest_flight.out_date} until "
                 f"{cheapest_flight.return_date}.",
            to=f'whatsapp:+{os.getenv("TO")}'
        )

        print(message.sid)

    def send_email(self, to_email, flight, city):
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASS)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=to_email,
                    msg=f"Subject:New Low Price Flight to {city}!\n\n"
                        f"Lowest price to {flight.destination} is £{flight.price}".encode('utf-8')
                )

            print("Email sent!")
        except Exception as e:
            print(f"Error sending email: {e}")
