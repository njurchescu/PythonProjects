import requests
from datetime import datetime

USERNAME = "njurchescu"
TOKEN = "ssjfvlirmd8o4w09"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": GRAPH_ID,
    "name": "Coding",
    "unit": "H",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# yesterday = datetime(year=2023, month=6, day=9)
# yesterday_formatted = yesterday.strftime("%Y%m%d")
today = datetime.now()
pixel_config ={
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours have you studied today?" )
}
pixel_update_config ={
    "quantity": "1"
}
graph_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday_formatted}"
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday_formatted}"
response = requests.post(url=graph_pixel, json=pixel_config, headers=headers)
# print(response.text)

# response = requests.put(url=update_endpoint, json=pixel_update_config, headers=headers)
# response = requests.delete(url=update_endpoint,  headers=headers)
print(response.text)