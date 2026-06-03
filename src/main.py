from model import OpenWeatherClient
from view import display_weather, display_forecast, display_menu
from controller import get_city_name_and_coordinates, get_mode
from dotenv import load_dotenv
from parser import parse_weather, parse_forecast
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
RESULTS_LIMIT = os.getenv("RESULTS_LIMIT")


def main():
    client = OpenWeatherClient(API_KEY, RESULTS_LIMIT)

    city = input("Veuillez saisir la ville : ")

    # Récupération du nom de la ville et des coordonnées
    locations = client.fetch_locations(city)
    coords = get_city_name_and_coordinates(locations)
    if coords is None:
        return
    city_name, lat, lon = coords

    # Choix du mode d'affichage
    display_menu()
    mode = get_mode()
    if mode is None:
        return

    # Affichage météo du jour
    if mode == "1":
        raw_weather = client.get_weather(lat, lon)
        weather = parse_weather(raw_weather, city_name)
        display_weather(weather)
    # Affichage météo prévisionnelle
    elif mode == "2":
        raw_forecast = client.get_forecast(lat, lon)
        forecasts = parse_forecast(raw_forecast)
        display_forecast(forecasts)


if __name__ == "__main__":
    main()