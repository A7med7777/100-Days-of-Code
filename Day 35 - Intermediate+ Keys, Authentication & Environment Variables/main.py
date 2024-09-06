import requests
import os
from twilio.rest import Client

OWM = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

params = {
    "lat": os.getenv("LAT"),
    "lon": os.getenv("LON"),
    "appid": os.getenv("APPID"),
    "cnt": 4
}

try:
    response = requests.request("GET", OWM, params=params)
    response.raise_for_status()
    print(response.status_code)

    weather_list = response.json()["list"]

    for weather in weather_list:
        if weather["weather"][0]["id"] < 700:
            message = client.messages.create(
                from_=f"whatsapp:+{os.getenv('FROM')}",
                body="It's going to rain today. Remember to bring an ☔️",
                to=f"whatsapp:+{os.getenv('TO')}",
            )

            print(message.sid)
            break
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
except KeyError as e:
    print(f"Unexpected response format: missing {e}")
except Exception as e:
    print(f"Error sending message: {e}")
