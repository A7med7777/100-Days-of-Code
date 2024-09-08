import requests
import datetime as dt
import re


def validation(prompt, pattern):
    user_input = input(prompt)

    while not re.match(pattern, user_input):
        print(f"Invalid input. Please follow the validation rule: {pattern}")
        user_input = input(prompt)

    return user_input


TOKEN = validation("Enter your Pixela token: ", r"[ -~]{8,128}")
USERNAME = validation("Enter your Pixela username: ", r"[a-z][a-z0-9-]{1,32}")
GRAPHID = validation("Enter your graph ID: ", r"[a-z][a-z0-9-]{1,16}")

headers = {
    "X-USER-TOKEN": TOKEN
}


def create_user_account():
    url = "https://pixe.la/v1/users"

    data = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    try:
        response = requests.request("POST", url, json=data)
        print(response.json()["message"])

        return True
    except requests.exceptions.ConnectionError as ce:
        print(ce)

        return False


def create_a_graph():
    url = f"https://pixe.la/v1/users/{USERNAME}/graphs"

    data = {
        "id": GRAPHID,
        "name": input("Enter graph name: "),
        "unit": input("Enter unit of measurement (e.g., commit, kilogram, calory): "),
        "type": input("Enter type (int/float): "),
        "color": input("Enter graph color (e.g., shibafu (green), momiji (red), sora (blue), ichou (yellow), "
                       "ajisai (purple) and kuro (black)):\n")
    }

    try:
        response = requests.request("POST", url, headers=headers, json=data)
        print(response.json()["message"])

        return True
    except requests.exceptions.ConnectionError as ce:
        print(ce)

        return False


def post_value():
    url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}?date=20180915&quantity=5"

    data = {
        "date": dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d"),  # Timezone-aware datetime
        "quantity": input("Enter quantity (e.g., number of pages read): ")
    }

    response = requests.request("POST", url, headers=headers, json=data)
    print(response.json()["message"])


if __name__ == "__main__":
    if create_user_account():
        if create_a_graph():
            post_value()
