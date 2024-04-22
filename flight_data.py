#This class is responsible for structuring the flight data.
import requests

class FlightData:
    def __init__(self, price, original_city, original_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.original_city = original_city
        self.original_airport = original_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

