#importeert de requests
import os
import requests
from utils import print_stripes
from color_text import * 


#De basis-URL voor de NPS API
URL ="https://developer.nps.gov/api/v1/"

def get_park_by_name(park_name):
    """Haalt gegevens van een nationaal park op uit de NPS API en returnt het park"""
    NPS_API_KEY = os.getenv('NPS_API_KEY')

    params = {
        "api_key": NPS_API_KEY,
        "limit": 500,
    }
    url = URL + "Parks"

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        parks = data.get('data', [])

        for park in parks:
            if park_name.lower() in park['fullName'].lower():
                return park
        print_stripes()
        print(Fore.RED + "Park not found. Please check the name and try again." + Style.RESET_ALL)
        return None
    else:
        print(f"Error fetching parks data: {response.status_code}")
        return None

def get_park_activities(park_code):
    """Haalt activiteiten op voor een park uit de NPS API"""
    NPS_API_KEY = os.getenv('NPS_API_KEY')

    params = {
        "api_key": NPS_API_KEY,
        "parkcode": park_code,
    }
    response = requests.get(f"{URL}activities/parks", params=params)

    if response.status_code == 200:
        data = response.json()
        activities = []

        for activity in data.get('data', []):
            for park in activity.get('parks', []):
                if park.get('parkCode') == park_code:
                    activities.append(activity['name'])

        if activities:
            print(Fore.CYAN + f"Activities for park code {park_code}:")
            for activity in activities:
                print(f"- {activity}")
        else:
            print(Fore.RED + f"No activities found for park {park_code}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Error fetching activities data: {response.status_code}" + Style.RESET_ALL)

def get_address(park_code):
    """Haalt adresgegevens op voor een park uit de NPS API """
    NPS_API_KEY = os.getenv('NPS_API_KEY')

    params = {
        "api_key": NPS_API_KEY,
        "parkcode": park_code,
    }
    response = requests.get(f"{URL}parks", params=params)

    if response.status_code == 200:
        data = response.json()
        parks = data.get('data', [])

        for park in parks:
            if park['parkCode'] == park_code:
                addresses = park.get('addresses', [])
                if addresses:
                    print_stripes()
                    print(Fore.GREEN + f"Park found: {park['fullName']} ({park['parkCode']})")
                    print(Fore.MAGENTA + "Address(es): ")
                    for address in addresses:
                        print(Fore.CYAN + f"Type: {address.get('type', 'N/A')}")
                        print(f"Street: {address.get('street', 'N/A')}")
                        if address.get('line2'):
                            print(f"Additional Address Info: {address.get('line2')}")
                        print(f"City: {address.get('city', 'N/A')}")
                        print(f"State: {address.get('state', 'N/A')}")
                        print(f"Postal Code: {address.get('postalCode', 'N/A')}" + Style.RESET_ALL)
                return
            else:
                print(f"No addresses found for park['fullName'].")
        else:
            print(Fore.RED + "Park not found. Please check the name and try again." + Style.RESET_ALL)
    else:
        print(f"Error fetching addresses data: {response.status_code}")



