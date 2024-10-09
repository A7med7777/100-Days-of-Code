from data_manager import DataManager
from flight_data import lowest_price
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt

ORIGIN_CITY_CODE = "CAI"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

rows = data_manager.retrieve_rows()["prices"]

for row in rows:
    iata = flight_search.city_search(row["city"])
    data_manager.edit_iata(row["id"], iata)

rows = data_manager.retrieve_rows()["prices"]

for row in rows:
    destination = row["iataCode"]
    tomorrow = dt.datetime.now() + dt.timedelta(days=1)
    six_month_from_today = dt.datetime.now() + dt.timedelta(days=(6 * 30))
    flights = flight_search.flight_offers_search(ORIGIN_CITY_CODE, destination, tomorrow, six_month_from_today)
    cheapest_flight = lowest_price(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < float(row["lowestPrice"]):
        print(f"Lower price flight found to {row['city']}!")
        notification_manager.send_message(cheapest_flight)
