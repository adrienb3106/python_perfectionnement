import requests
from dataclasses import dataclass
from typing import Any


@dataclass
class Weather:
    temp: float
    feels_like: float
    humidity: int
    description: str
    wind: float
    country: str
    city: str


@dataclass
class DailyForecast:
    date: int
    temp_min: float
    temp_max: float
    humidity: int
    description: str #description météo (soleil, huminde,etc)
    wind: float
    pop: float #risque de pluie
    rain: float #mm de pluie


class OpenWeatherClient:
    """
    Client API OpenWeatherMap.
    Encapsule les appels HTTP liés à la météo.
    """

    def __init__(self, api_key: str, results_limit: int = 5):
        self.api_key = api_key
        self.results_limit = results_limit
        self.base_url = "https://api.openweathermap.org/"

    # -------------------------
    # Abstraction HTTP
    # -------------------------
    def _get(self, endpoint: str, params: dict[str, Any]) -> dict[str, Any]:
        url = self.base_url + endpoint
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    # -------------------------
    # API methods
    # -------------------------
    def fetch_locations(self, city: str) -> list[dict[str, Any]]:
        params = {
            "q": city,
            "limit": self.results_limit,
            "appid": self.api_key,
        }
        return self._get("geo/1.0/direct", params)

    def get_weather(self, lat: float, lon: float) -> dict[str, Any]:
        params = {
            "lat": lat,
            "lon": lon,
            "units": "metric",
            "appid": self.api_key,
        }
        return self._get("data/2.5/weather", params)

    def get_forecast(self, lat: float, lon: float) -> dict[str, Any]:
        params = {
            "lat": lat,
            "lon": lon,
            "cnt": 40,  # 5 jours × 8 créneaux de 3h
            "units": "metric",
            "lang": "fr",
            "appid": self.api_key,
        }
        return self._get("data/2.5/forecast", params)