import requests
import os
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.getenv("ENDPOINT")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.headers = {
            "Authorization": BEARER_TOKEN,
            "Content-Type": "application/json"
        }
        
        
        self.endpoint = "https://api.sheety.co/39420a5c7d36424afe243e6a28544e65/flightDeals/prices"
    
    def get_data(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        print(response.json())
        return response.json()['prices']
    
    def update_data(self, price_list):
        json_data = {
            "price": {
                "iataCode": None
            }
        }
        
        for row in price_list:
            json_data['price']['iataCode'] = row['iataCode']
            response = requests.put(url=self.endpoint + f"/{row['id']}", json=json_data, headers=self.headers)