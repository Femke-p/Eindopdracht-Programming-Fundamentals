from color_text import *

from favorite import read_favorites
from functions import get_city_from_user, handle_weather_data
from get_national_park import get_park_by_name, get_park_activities, get_address
from get_weather import get_weather, print_all_weather, print_specific_weather, check_city
from selection_menus import *
from dotenv import load_dotenv

load_dotenv()



def main():
    while True:

        favorites = read_favorites()

        show_options(home_options)
        home_choice = choose_option(home_options)

        if home_choice == 0:
            show_options(specific_or_all_weather_options)
            specific_or_all_weather_choice = choose_option(specific_or_all_weather_options)
            action = followup_all_or_specific_weather(specific_or_all_weather_choice)


            city = get_city_from_user(favorites)
            check_city(city)
            weather_data = get_weather(city)
            get_weather(city)


            if action == "all_weather":
                show_options(temperature_options)
                choice_what_temperature = choose_option(temperature_options)
                weather_data = get_weather(city)
                handle_weather_data(weather_data, choice_what_temperature)
                print_all_weather(weather_data, city)

            elif action == "specific_weather":
                show_options(specific_weather_options)
                choice_specific_weather = choose_option(specific_weather_options)
                if choice_specific_weather == 0 or choice_specific_weather == 2 or choice_specific_weather == 3:
                    show_options(temperature_options)
                    choice_what_temperature = choose_option(temperature_options)
                    weather_data = get_weather(city)
                    handle_weather_data(weather_data, choice_what_temperature)
                    print_stripes()
                    print_specific_weather(weather_data, choice_specific_weather, city)
                else:
                    weather_data = get_weather(city)
                    print_stripes()
                    print_specific_weather(weather_data, choice_specific_weather, city)

        elif home_choice == 1:
            while True:
                print_stripes()
                park_name = input("Enter the name of the national park you want information about: ").strip()
                park = get_park_by_name(park_name)
                if park:
                    print(Fore.GREEN + f"Park found: {park['fullName']} ({park['parkCode']})")
                    print(Fore.MAGENTA + f"Description: {park['description']}")
                    print(f"Location: {park['states']}")
                    get_park_activities(park['parkCode'])
                    break

        elif home_choice == 2:
            while True:
                print_stripes()
                park_name = input("Enter the name of the national park you want information about: ").strip()
                park = get_park_by_name(park_name)
                if park:
                    get_address(park['parkCode'])
                    break


        elif home_choice == 3:
            print_stripes()
            print(Fore.YELLOW + "Thanks for coming to our information center. I hope we helped you and enjoy the rest of your day." + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()
