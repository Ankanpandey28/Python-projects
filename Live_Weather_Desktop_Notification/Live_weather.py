# Live_weather.py
# A simple script to get current weather and show macOS notification

import requests
from pync import Notifier

# 1. Set city name
city = "Delhi"

# 2. Get coordinates from city name using Open-Meteo Geocoding API
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1}

try:
    geo_res = requests.get(geo_url, params=geo_params).json()
except Exception as e:
    print(f"Error fetching coordinates: {e}")
    exit(1)

if "results" in geo_res and len(geo_res["results"]) > 0:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # 3. Get current weather data
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    try:
        weather_res = requests.get(weather_url, params=weather_params).json()
    except Exception as e:
        print(f"Error fetching weather: {e}")
        exit(1)

    if "current_weather" in weather_res:
        temp = weather_res["current_weather"]["temperature"]
        wind = weather_res["current_weather"]["windspeed"]
        weather_info = f"{city}: {temp}°C, Wind {wind} km/h"

        # Print in terminal
        print("Weather:", weather_info)

        # Send macOS desktop notification
        Notifier.notify(weather_info, title="Weather Update")
    else:
        print("Weather data not found for the given coordinates")
else:
    print("City not found")