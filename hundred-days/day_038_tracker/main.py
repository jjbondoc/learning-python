import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")

GENDER = "male"
WEIGHT = 70
HEIGHT = 173
AGE = 25

DATE = dt.datetime.now().strftime('%d/%m/%Y')
TIME = dt.datetime.now().strftime('%H:%M:%S')

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query":input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=nutrition_endpoint, json=parameters, headers=headers)
result = response.json()

#-------- Sheety API -------#
sheety_endpoint = "https://api.sheety.co/39420a5c7d36424afe243e6a28544e65/workoutTracking/workouts"

sheety_headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

for exercise in result['exercises']:
    name = exercise['name'].title()
    duration = exercise['duration_min']
    calories = exercise['nf_calories']
    
    sheety_payload = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": name,
            "duration": duration,
            "calories": calories
        }
    }
    
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_payload, headers=sheety_headers)
    sheety_result = sheety_response.text
    print(sheety_result)