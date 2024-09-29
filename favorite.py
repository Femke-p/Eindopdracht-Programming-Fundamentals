from utils import print_stripes
from color_text import *

def read_favorites(file_path = 'favorites.txt'):
    """leest alle favorieten die in het bestand favorites.txt staat"""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def write_favorites(city, favorites, file_path = 'favorites.txt'):
    """ Voegt favorieten toe aan het bestand favorites.txt als die nog niet toegevoegd waren"""
    if city not in favorites:
        with open(file_path, 'a') as file:
            file.write(f"{city} \n")
        print(f"{city} is added to your favorites.")
    else:
        print_stripes()
        print(f"{city} is already added to your favorites.")

def display_favorites(favorites):
    """ Laat een lijst met favorieten zien. Door enumerate komt er een nummer voor."""
    if favorites:
        print("Your favorites are:")
        for i, favorite in enumerate(favorites, start=1):
            print(f"{i}. {favorite}")

    else:
        print("Your favorites are empty.")
        return display_favorites == "empty"


def choose_city_from_favorites(favorites):
    """ Hierbij kan je een stad kiezen uit de favorieten lijst. Hij controleert ook de invoer"""
    while True:
        try:
            choice = int(input("Please choose a place: ")) -1
            if 0 <= choice < len(favorites):
                return favorites[choice]
            else:
                print(Fore.RED + "invalid choice, please choose a number." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "invalid input, please choose a number." + Style.RESET_ALL)

def ask_to_save_favorite(city):
    """ Vraagt of de gebruiker de stad wil toevoegen aan de favorieten."""
    while True:
        add_favorites = input(f"Do you want to add {city} to your favorites? (yes/no) ").strip().lower()
        if add_favorites == 'yes':
            return add_favorites
        if add_favorites == 'no':
            break
        else:
            print(Fore.RED + "Invalid input please choose yes or no." + Style.RESET_ALL)
            continue


