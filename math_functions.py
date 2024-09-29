
def kelvin_to_celsius(temp_kelvin):
    """ Functie voor Kelvin naar Celsius"""
    return temp_kelvin - 273.15

def kelvin_to_fahrenheit(temp_kelvin):
    """ Functie voor Kelvin naar Fahrenheit"""
    return (temp_kelvin - 273.15) * 1.8 + 32



def return_correct_temperature(temp_kelvin, temperature_choice):
    """Zet de temperatuur om op basis van de keuze van de gebruiker."""
    if temperature_choice == 0:
        return f"{round(temp_kelvin, 2)} K"
    elif temperature_choice == 1:
        temperature = kelvin_to_celsius(temp_kelvin)
        return f"{round(temperature, 2)} °C"
    elif temperature_choice == 2:
        temperature = kelvin_to_fahrenheit(temp_kelvin)
        return f"{round(temperature, 2)} °F"
