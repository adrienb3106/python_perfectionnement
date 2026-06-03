import requests
from dataclasses import dataclass

@dataclass
class Weather:
    temp: float
    feels_like: float
    humidity: int
    description: str
    wind: float
    country: str
    city: str

class OpenWeatherClient:
    """
    Client API OpenWeatherMap.
    Encapsule les appels HTTP liés à la météo.
    """
    def __init__(self, api_key: str, results_limit: int = 5):
        self.api_key = api_key
        self.results_limit = results_limit
        self.base_url = "https://api.openweathermap.org/"


    def fetch_locations(self, city: str) -> list[dict[str, Any]]:
        """
        Récupère les localisations correspondant à une ville via l'API OpenWeatherMap.
        """

        params = {
            "q": city,
            "limit": self.results_limit,
            "appid": self.api_key
        }

        response = requests.get(self.base_url + "geo/1.0/direct", params=params)
        response.raise_for_status()
        return response.json()

    def get_weather(self, lat: float, lon: float) -> dict[str, Any] : 
        """
        Récupère les données météo pour des coordonnées GPS.
        """

        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key
        }

        response = requests.get(self.base_url + "data/2.5/weather", params=params)
        response.raise_for_status()
        return response.json()
