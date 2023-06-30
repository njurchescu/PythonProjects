import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

# USERNAME = "njuescu"
# PASSWORD = "fRoscho***"
# os.environ['USERNAME'] = "njuche***"
# os.environ['PASSWORD'] = "fmsch****"
# basic = HTTPBasicAuth(USERNAME, PASSWORD)

header = {
   "Authorization": os.environ["Authorization"]
}

# APP_ID = "0ad0188d"
# API_KEY = "faa92e6fb4ea64e330af6b89970bdc4d"
# os.environ['APP_ID'] = "0ad0188d"
# os.environ['API_KEY'] = "faa92e6fb4ea64e330af6b89970bdc4d"
parameters = {
     "query": input("Tell me which exercise you did? "),
     "gender": "male",
     "weight_kg": 68,
     "height_cm": 171,
     "age": 29
}

headers = {
    "x-app-id": os.environ['APP_ID'],
    "x-app-key": os.environ['API_KEY']
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(response.text)
print(response)

# sheety_endpoint = "https://api.sheety.co/ea09b662c24616184a5afac54a9d8e9a/workoutTracking/workouts"
# os.environ['sheety_endpoint'] = "https://api.sheety.co/ea09b662c24616184a5afac54a9d8e9a/workoutTracking/workouts"



today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# print(result["exercises"][0]["name"].title())

for exercise in result['exercises']:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# sheety_response = requests.post(url=os.environ['sheety_endpoint'], json=sheet_input, auth=(os.environ['USER'], os.environ['PASSWORD']))
sheety_response = requests.post(url=os.environ['sheety_endpoint'], json=sheet_input, headers=header)
print(sheety_response.text)