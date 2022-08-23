import requests

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "931fcbe0a5dfe687af1e19000b7f0734"
parameters = {
    "lat": 50.997410,
    "lon": -1.321790,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
data = response.json()
hourly_data = data['hourly'][:12] #12 hourly weather data
weather_ids = [hour['weather'][0]['id'] for hour in hourly_data] #list of the weather ids

for id in weather_ids:
    if int(id) < 700:
        print("Bring an umbrella today!")
        break