from utils import print_stripes
from utils import *

home_options = ('Weather data for a place', 'Activities for a specific national park', 'Address of a specific national park', 'Close the program')
specific_or_all_weather_options = ('Do you want all the information', 'Do you want specific information')
specific_weather_options = ('Temperature and description', 'Sunset and sunrise', 'Feels like temperature', 'Min and max temperature', 'Pressure', 'Sea level and ground level', 'Wind speed')
temperature_options = ('Kelvin', 'Degrees Celsius', 'Degrees Fahrenheit')

def show_options(home_options):
    """Laat de opties zien op basis van de opties die er beschikbaar zijn."""
    print_stripes()
    print("The options are: ")
    for i, option in enumerate(home_options):
        print(f"{i + 1}. {option}")

def choose_option(home_options):
    """Vraagt de gebruiker om een optie te kiezen en returnt die keuze."""
    while True:
        try:
            choice = int(input("Please choose an option: ")) -1
            if 0 <= choice < len(home_options):
                return choice
            else: print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input, please try again." + Style.RESET_ALL)

def followup_all_or_specific_weather(specific_or_all_weather_choice):
    """Bepaalt of dat alle informatie moet worden getoond of alleen specifieke informatie."""
    if specific_or_all_weather_choice == 0:
        return 'all_weather'
    elif specific_or_all_weather_choice == 1:
        return 'specific_weather'
    else:
        return 'invalid'