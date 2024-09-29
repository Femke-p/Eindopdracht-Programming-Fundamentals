from tabnanny import check

from favorite import display_favorites, choose_city_from_favorites, ask_to_save_favorite, write_favorites
from get_weather import check_city, get_weather
from math_functions import return_correct_temperature
from utils import print_stripes
from color_text import *

def get_city_from_user(favorites):
    """" Vraag de gebruiker om een stad in te voeren of gebruik de favorieten"""
    while True:
        print_stripes()
        use_favorite = input("Do you want to use saved favorites? (yes/no) ").strip().lower()
        print_stripes()
        if use_favorite == "yes" :
            if not favorites:
                print(Fore.RED + "Your favorites are empty." + Style.RESET_ALL)
                use_favorite = "no"
            else:
                display_favorites(favorites)
                while True:
                    return choose_city_from_favorites(favorites)


        elif use_favorite == "no":
            while True:
                city = input("Enter place name: ")
                print_stripes()

                if not check_city(city):
                    continue

                if ask_to_save_favorite(city):
                    write_favorites(city, favorites)

                return city
        else:
            print(Fore.RED + "Invalid input, please type 'yes' or 'no'" + Style.RESET_ALL)

def handle_weather_data(weather_data, choice_what_temperature):
    """"Zorg ervoor dat alle temperatuurgegevens juist worden omgezet."""
    weather_data['temperature'] = return_correct_temperature(weather_data['temperature'], choice_what_temperature)
    weather_data['min_temp'] = return_correct_temperature(weather_data['min_temp'], choice_what_temperature)
    weather_data['max_temp'] = return_correct_temperature(weather_data['max_temp'], choice_what_temperature)
    weather_data['feels_like'] = return_correct_temperature(weather_data['feels_like'], choice_what_temperature)



