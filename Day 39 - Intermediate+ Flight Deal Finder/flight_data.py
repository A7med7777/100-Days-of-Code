class FlightData:
    def __init__(self, origin, destination, departure_date, return_date, price):
        self.origin = origin
        self.destination = destination
        self.departureDate = departure_date
        self.returnDate = return_date
        self.price = price


def lowest_price(data):
    if data is None or not data['data']:
        print("No flight data")

        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data['data'][0]
    low_price = float(first_flight["price"]["total"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(
        price=low_price,
        origin=origin,
        destination=destination,
        departure_date=out_date,
        return_date=return_date
    )

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])

        if price < low_price:
            low_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

            cheapest_flight = FlightData(
                price=low_price,
                origin=origin,
                destination=destination,
                departure_date=out_date,
                return_date=return_date
            )

    print(f"Lowest price to {destination} is £{low_price}")
    return cheapest_flight
