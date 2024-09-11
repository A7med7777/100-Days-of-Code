import requests
from requests.auth import HTTPBasicAuth
import datetime as dt
import os

GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 180
AGE = 21


def get_exercise_stats():
    """
        Prompts the user for exercises they did and sends a request to Nutritionix API
        to get stats for those exercises.

        Returns:
            dict: JSON response from the API with exercise details or None if an error occurred.
    """

    app_id = os.getenv('X-APP-ID')
    app_key = os.getenv('X-APP-KEY')

    if not app_id or not app_key:
        raise ValueError("API credentials are missing. Please set X-APP-ID and X-APP-KEY in environment variables.")

    url = "https://trackapi.nutritionix.com/v2/natural/exercise"
    headers = {"x-app-id": app_id, "x-app-key": app_key}

    parameters = {
        "query": input("Tell me which exercises you did: "),
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }

    try:
        response = requests.request("POST", url=url, headers=headers, json=parameters)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

        return None


def saving_data(data):
    """
        Saves workout data to the external service using Sheety API.

        Args:
            data (dict): A dictionary containing workout information for a single exercise.
    """

    url = os.getenv("API_SHEETY")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    if not url or not username or not password:
        raise ValueError("Sheety API credentials or URL are missing. Please set API_SHEETY, USERNAME, and PASSWORD.")

    basic_auth = HTTPBasicAuth(username=username, password=password)

    params = {
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "exercise": data["name"].title(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"]
        }
    }

    try:
        response = requests.post(url, auth=basic_auth, json=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Data saved successfully:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Failed to save data: {e}")


if __name__ == "__main__":
    exercises = get_exercise_stats()["exercises"]

    if exercises:
        for exercise in exercises:
            saving_data(exercise)
