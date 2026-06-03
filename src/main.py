from model import OpenWeatherClient
from view import display_weather, parse_weather
from controller import choose_location, get_city_name_and_coordinates
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
RESULTS_LIMIT = os.getenv("RESULTS_LIMIT")


def main():
    client = OpenWeatherClient(API_KEY, RESULTS_LIMIT)

    city = input("Veuillez saisir la ville : ")

    locations = client.fetch_locations(city)
    coords = get_city_name_and_coordinates(locations)

    if coords is None:
        return

    city_name, lat, lon = coords

    raw_weather = client.get_weather(lat, lon)
    weather = parse_weather(raw_weather, city_name)

    display_weather(weather)


if __name__ == "__main__":
    main()