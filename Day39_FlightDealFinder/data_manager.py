import requests
from pprint import pprint

sheet_endpoint = "https://api.sheety.co/0a7ec7d2ce95ebf963bfbfaeeaff8bf8/copyOfFlightDeals/prices"
USER_ENDPOINT = "https://api.sheety.co/0a7ec7d2ce95ebf963bfbfaeeaff8bf8/copyOfFlightDeals/users"

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheet_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheet_endpoint}/{city['id']}", json=new_data)
            print(response.text)

    def get_user_data(self):
        response = requests.get(url=USER_ENDPOINT)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data
