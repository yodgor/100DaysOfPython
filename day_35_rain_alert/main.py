import requests
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "c502760a5c023642a36b0f0a8be8d209"

weather_params = {
    "lat": 40.75,
    "lon": -73.81,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

print(weather_data)
