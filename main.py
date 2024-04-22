# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

ORIGINAL_CITY_IATA = "ADD"

data_manager = DataManager()
sheet_data = data_manager.price_data()
flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flight(
        ORIGINAL_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

# data_manager.destination_data = sheet_data
# data_manager.update_destination_code()

# print(search)
