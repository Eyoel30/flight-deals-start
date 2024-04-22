# This class is responsible for talking to the Flight Search API.
import requests
from flight_data import FlightData
from pprint import pprint
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API = "PF23OzcF7mwa1FPii7kG_B5ruauEe_Am"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        results = results[0]["code"]
        return results

    def check_flight(self, original_city_ap, destination_city_ap, from_time, to_time):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API}
        query = {
            "fly_from": original_city_ap,
            "fly_to": destination_city_ap,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "ETB"
        }
        response = requests.get(url=search_endpoint, headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"no flight for the {destination_city_code}")
            
        pprint(data)
        print(type(data))
        flight_data = FlightData(
            price=data["price"],
            original_city=data["route"][0]["cityFrom"],
            original_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["cityCodeTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ETC {flight_data.price}")
        return flight_data


# if __name__ == '__main__':
#     from flight_search import FlightSearch
#     flight_search = FlightSearch()
#     flight_search.check_flight(original_city_ap="ETH", destination_city_ap="USA", from_time=1/11/2023, to_time=1/03/2024)



# if __name__ == '__main__':
#     from flight_search import FlightSearch
#     from data_manager import DataManager
#     data_manager = DataManager()
#     sheet_data = data_manager.price_data()
#
#     flight_search = FlightSearch()
#     for row in sheet_data:
#        data = flight_search.get_destination_code(row["city"])["locations"]
#        code = data[0]["code"]
        # if row["iataCode"] == "":
        #     row["iataCode"] = flight_search.get_destination_code(row["city"])

    # print(code)
