import requests
from datetime import datetime
"""
response = requests.get(url="http://api.open-notify.org/is-now.json")
# Raises exception depending on error code
response.raise_for_status()

data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = (longitude, latitude)
print(iss_position)

"""
MY_LAT = 45.734780
MY_LNG = 21.333570
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# print(response.status_code)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
# ['02', '51', '44+00', '00']
time_now = datetime.now()
print(time_now.hour)












