import os
from datetime import timezone
import requests
from utils import print_stripes, normal_time
from color_text import *

URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """"Haalt weergegevens op voor de gevraagde stad."""
    OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

    params = {
        "q": city,
        "appid": OPEN_WEATHER_API_KEY,
    }

    response = requests.get(URL, params=params)
    if response.status_code == 200:
        data = response.json()
        timezone_offset = data["timezone"]
        weather_data = {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "sunset": normal_time(data["sys"]["sunset"], timezone_offset),
            "sunrise": normal_time(data["sys"]["sunrise"], timezone_offset),
            "feels_like": data["main"]["feels_like"],
            "min_temp": data["main"]["temp_min"],
            "max_temp": data["main"]["temp_max"],
            "pressure": data["main"]["pressure"],
            "sea_level": data.get("main", {}).get("sea_level", "N/A"),
            "grnd_level": data.get("main", {}).get("grnd_level", "N/A"),
            "wind_speed": data["wind"]["speed"],
        }
        return weather_data


def print_all_weather(weather_data, city):
    """Print alle gegevens die gevonden zijn voor het gevraagde park."""
    print_stripes()
    print(Fore.MAGENTA + f"Weather data for {city}: " + Style.RESET_ALL)
    for key, value in weather_data.items():
        if "pressure" in key or "level" in key:
            print(Fore.CYAN + f"{key}: {value} hPa" + Style.RESET_ALL)
        if "speed" in key:
            print(Fore.CYAN + f"{key}: {value} m/s" + Style.RESET_ALL)
        else:
            print(Fore.CYAN + f"{key}: {value}" + Style.RESET_ALL)

def print_specific_weather(weather_data, choice_specific_weather, city):
    """Print specifieke gegevens die gevonden zijn voor het gevraagde park"""
    if choice_specific_weather == 0:
        print(Fore.CYAN + f"Weather data for {city}: ")
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Description: {weather_data['description']}" + Style.RESET_ALL)
    elif choice_specific_weather == 1:
        print(Fore.CYAN + f"Weather data for {city}: ")
        print(f"Sunset: {weather_data['sunset']}")
        print(f"Sunrise: {weather_data['sunrise']}" + Style.RESET_ALL)
    elif choice_specific_weather == 2:
        print(Fore.CYAN + f"Weather data for {city}: ")
        print(f"Feels like: {weather_data['feels_like']}" + Style.RESET_ALL)
    elif choice_specific_weather == 3:
        print(Fore.CYAN + f"Weather data for {city}: ")
        print(f"Min temp: {weather_data['min_temp']}")
        print(f"Max temp: {weather_data['max_temp']}" + Style.RESET_ALL)
    elif choice_specific_weather == 4:
        print(Fore.CYAN + f"Weather data for {city}: ")
        print(f"Pressure: {weather_data['pressure']} hPa" + Style.RESET_ALL)
    elif choice_specific_weather == 5:
        print(Fore.CYAN + f"Weather data for {city}: ")
        print(f"Sea_level: {weather_data['sea_level']} hPa")
        print(f"Grnd_level: {weather_data['grnd_level']} hPa" + Style.RESET_ALL)
    elif choice_specific_weather == 6:
        print(Fore.CYAN + f"Weather data for {city}: ")
        print(f"Wind_speed: {weather_data['wind_speed']} m/s" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Invalid choice" + Style.RESET_ALL)



def check_city(city):
    """"Haalt weergegevens op voor de gevraagde stad."""
    OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

    params = {
        "q": city,
        "appid": OPEN_WEATHER_API_KEY,
    }

    response = requests.get(URL, params=params)
    while True:
        if response.status_code == 404:
            print(Fore.RED + "Place not found" + Style.RESET_ALL)
            return False

        elif response.status_code != 200:
            print(Fore.RED + f"Error fetching weather: {response}"+ Style.RESET_ALL)
            return None

        else:
            return True

