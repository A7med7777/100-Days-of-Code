import requests
from requests.auth import HTTPBasicAuth
import os


class DataManager:
    def __init__(self):
        self.url = os.getenv("URL")
        self.username = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.basic_auth = HTTPBasicAuth(username=self.username, password=self.password)

    def add_row(self, city, iata, price):
        params = {
            "price": {
                "city": city,
                "iataCode": iata,
                "lowestPrice": price
            }
        }

        try:
            response = requests.post(self.url, auth=self.basic_auth, json=params)
            response.raise_for_status()

            return response.text
        except requests.exceptions.RequestException as re:
            return f"Failed to save data: {re}"

    def delete_row(self, object_id):
        url = f"{self.url}/{object_id}"

        try:
            response = requests.delete(url, auth=self.basic_auth)
            response.raise_for_status()

            return response.text
        except requests.exceptions.RequestException as re:
            return f"Failed to delete data: {re}"

    def edit(self, url, params):
        try:
            response = requests.put(url, auth=self.basic_auth, json=params)
            response.raise_for_status()

            return response.text
        except requests.exceptions.RequestException as re:
            return f"Failed to save data: {re}"

    def edit_iata(self, object_id, iata):
        url = f"{self.url}/{object_id}"

        params = {
            "price": {
                "iataCode": iata
            }
        }

        return self.edit(url, params)

    def edit_price(self, object_id, price):
        url = f"{self.url}/{object_id}"

        params = {
            "price": {
                "lowestPrice": price
            }
        }

        return self.edit(url, params)

    def retrieve_rows(self):
        try:
            response = requests.get(self.url, auth=self.basic_auth)
            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as re:
            return {}
