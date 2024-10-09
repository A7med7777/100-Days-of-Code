from twilio.rest import Client
import os


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
