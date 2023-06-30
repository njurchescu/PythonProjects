from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "LON"

flight_search = FlightSearch()
notification_manager = NotificationManager()


# sheet_user = data_manager.get_user_data()
#
# users = {
#     user["email"]: {
#         "id": user["id"],
#         "firstName": ["firstName"],
#         "lastName": ["lastName"]
#     }
#     for user in sheet_user}
# # # json_file = json.dumps(sheet_data, indent=4)
# # # with open("sheet_data.json") as infile:
# # #     data = json.load(infile)
# #
# #
if sheet_data[0]['iataCode'] == "":
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row["city"])
    print(type(sheet_data))
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination_code in destinations:
    flight = flight_search.find_flight(ORIGIN_CITY_IATA, destination_code, tomorrow, six_months_from_today)
    if flight is None:
        continue
    if flight.price < destinations[destination_code]["price"]:
        users = data_manager.get_user_data()

        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport}" \
                  f" to {flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)
        notification_manager.send_sms(message)
        notification_manager.send_emails(emails, message)
        break

