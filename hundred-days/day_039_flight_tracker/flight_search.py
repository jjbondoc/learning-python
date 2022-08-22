from calendar import prcal
import os
import requests
import datetime as dt
from flight_data import FlightData
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.headers = {
            "apikey": os.getenv("FS_APIKEY"),
            "Content-Type": "application/json"
        }
        
        self.endpoint = "https://tequila-api.kiwi.com"
        
    def get_iata(self, price_list: list, city: str):
        query = {
            "term": None,
            "locale": "en-US",
            "location_types": "city",
            "limit": 1,
            "active_only": True
        }
        for row in price_list:
            if row['city'] == city:
                query['term'] = city
                response = requests.get(url=self.endpoint + f"/locations/query", params=query, headers=self.headers)
                code = response.json()['locations'][0]['code']
                row['iataCode'] = code
            else:
                continue
    
    def get_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        
        response = requests.get(url=self.endpoint + f"/v2/search", params=query, headers=self.headers)
        
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_city=data['cityFrom'],
            origin_airport=data['flyFrom'],
            destination_city=data['cityTo'],
            destination_airport=data['flyTo'],
            out_date=data['route'][0]['local_departure'].split('T')[0],
            return_date=data['route'][0]['local_arrival'].split('T')[0]
        )
        
        return flight_data
        
        