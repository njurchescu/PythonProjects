import requests
import os
from flight_data import FlightData
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ['tequila_apikey']


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": os.environ['tequila_apikey']}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def find_flight(self, origin_city_code, destination_city_code, date_from, date_to):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": os.environ['tequila_apikey']}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "max_stopovers": "0",
            "flight_type": "round",
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "curr": "GBP",
            "one_for_city": 1,
        }
        response = requests.get(url=search_endpoint, headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 2
            response = requests.get(url=search_endpoint, headers=headers, params=query)
            try:
                data = response.json()["data"][0]
            except IndexError:
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][0]["local_arrival"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][0]["local_arrival"].split("T")[0]
            )
            # print(f"{flight_data.destination_city}: {flight_data.price}")
            return flight_data
