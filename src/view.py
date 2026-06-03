from typing import Any
from model import Weather, DailyForecast
from datetime import datetime, timezone


def display_locations(locations: list[dict[str, Any]]) -> None:
    for i, loc in enumerate(locations):
        name = loc["name"]
        country = loc["country"]
        state = loc.get("state", "")
        label = f"{name}, {state} ({country})" if state else f"{name} ({country})"
        print(f"{i + 1} - {label}")


def display_menu() -> None:
    print("\n1 - Météo actuelle")
    print("2 - Prévisions sur 5 jours")


def display_weather(weather: Weather) -> None:
    print("\n" + "=" * 40)
    print(f"🌍 {weather.city} ({weather.country})")
    print("=" * 40)
    print(f"🌤️  Météo      : {weather.description}")
    print(f"🌡️  Température: {weather.temp:.1f} °C")
    print(f"🌡️  Ressenti   : {weather.feels_like:.1f} °C")
    print(f"💧 Humidité    : {weather.humidity} %")
    print(f"💨 Vent        : {weather.wind:.1f} m/s")
    print("=" * 40 + "\n")


def display_forecast(forecasts: list[DailyForecast]) -> None:
    print("📅 Prévisions sur 5 jours")
    print("=" * 60)
    for day in forecasts:
        label = datetime.fromtimestamp(day.date, tz=timezone.utc).strftime("%A %d %b")
        rain_str = f"  🌧️  {day.rain:.1f} mm" if day.rain > 0 else ""
        humidity_str = f"  💧{day.humidity}%"
        pop_str = f"  ☔{day.pop * 100:.0f}%"
        print(
            f"{label:<18} {day.temp_min:>3.0f}°↓ {day.temp_max:>3.0f}°↑"
            f"{humidity_str:<9}"
            f"{pop_str:<8}"
            f"  {day.description.capitalize()}"
            f"{rain_str}"
        )
    print("=" * 60 + "\n")