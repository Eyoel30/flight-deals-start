# This class is responsible for talking to the Google Sheet.
import requests
# from pprint import pprint

SHEETY_LOC = "https://api.sheety.co/b5b7c42dc7f69fe3a2876ba74b05e121/lowPriceFlight/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def price_data(self):
        response = requests.get(SHEETY_LOC)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
               "price": {
                   "iataCode": city["iataCode"]
               }
            }
            response = requests.put(url=f"{SHEETY_LOC}/{city['id']}", json=new_data)
            print(response.text)

# print(DataManager().price_data())
# print(DataManager().destination_data)
