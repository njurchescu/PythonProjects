import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ['OWM_API_KEY']
print(api_key)
account_sid = "AC2dea3741df92ac48fcac3e52f4990fd1"
auth_token = "55279449fb9a06bdaff1eb07c83c0cfb"

parameters = {
    "lat": 45.7461591,
    "lon": 21.3245233,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_temp = weather_data['hourly']
# print(weather_data)
# print(hourly_temp)


will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to rain, bring an ☂️.",
        from_='+13613154012',
        to='+40733120289'
    )
    print(message.status)
