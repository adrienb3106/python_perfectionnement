from model import Weather, DailyForecast
from datetime import datetime, timezone

def parse_weather(data: dict, city_name: str) -> Weather:
    return Weather(
        temp=data["main"]["temp"],
        feels_like=data["main"]["feels_like"],
        humidity=data["main"]["humidity"],
        description=data["weather"][0]["description"],
        wind=data["wind"]["speed"],
        country=data["sys"]["country"],
        city=city_name,
    )

def parse_forecast(data: dict) -> list[DailyForecast]:
    days: dict[str, list] = {}

    for entry in data["list"]:
        day_key = datetime.fromtimestamp(entry["dt"], tz=timezone.utc).strftime("%Y-%m-%d")
        days.setdefault(day_key, []).append(entry)

    result = []
    for day_key, entries in sorted(days.items()):
        result.append(DailyForecast(
            date=entries[0]["dt"],
            temp_min=min(e["main"]["temp_min"] for e in entries),
            temp_max=max(e["main"]["temp_max"] for e in entries),
            humidity=round(sum(e["main"]["humidity"] for e in entries) / len(entries)),
            description=entries[len(entries) // 2]["weather"][0]["description"],
            wind=max(e["wind"]["speed"] for e in entries),
            pop=max(e.get("pop", 0.0) for e in entries),
            rain=sum(e.get("rain", {}).get("3h", 0.0) for e in entries),
        ))

    return result