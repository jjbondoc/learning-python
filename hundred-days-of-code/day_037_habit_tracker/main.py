from urllib import response
import requests
from datetime import datetime

USERNAME = "junel"
TOKEN = "fdJKdfws456"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token":TOKEN,
    "username":"junel",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# ------------- CREATE USER -------------
# response = requests.post(url=pixela_endpoint, json=user_params) #post request, requires json data to send over
# print(response.text)

# ------------- CREATE GRAPH DEFINITION -------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":"graph1",
    "name":"Python Graph",
    "unit": "Hrs",
    "type": "float",
    "color":"ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# ------------- POST A PIXEL -------------
today = datetime.now().strftime("%Y%m%d")
add_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
add_config = {
    "date":today,
    "quantity": input("How many hours did you spend learning Python today? ")
}

response = requests.post(url=add_endpoint, json=add_config, headers=headers)
print(response.text)

# ------------- UPDATE A PIXEL -------------
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
new_pixel_data = {
    "quantity":"3.5"
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

# ------------- DELETE A PIXEL -------------
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# response = requests.delete(url=delete_endpoint, headers=headers)