import requests
import os


class FlightSearch:
    def __init__(self):
        self.API_key = os.getenv("API_KEY")
        self.API_secret = os.getenv("API_SECRET")
        self.access_token = self.authorizing()

    def authorizing(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "grant_type": "client_credentials",
            "client_id": self.API_key,
            "client_secret": self.API_secret
        }

        response = requests.post(url, headers=headers, data=data)

        return response.json()["access_token"]

    def flight_offers_search(self, origin_city_code, destination_city_code, from_time, to_time):
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": 10,
        }

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.get(url, headers=headers, params=params)

        return response.json()

    def city_search(self, city):
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        params = {
            "keyword": city.upper(),
            "max": 2,
            "include": "AIRPORTS",
        }

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.get(url, headers=headers, params=params)

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code
