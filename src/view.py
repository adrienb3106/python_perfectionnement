from model import Weather

def parse_weather(data: dict, city_name: str) -> Weather:
    return Weather(
        temp=data["main"]["temp"] - 273.15,
        feels_like=data["main"]["feels_like"] - 273.15,
        humidity=data["main"]["humidity"],
        description=data["weather"][0]["description"],
        wind=data["wind"]["speed"],
        country=data["sys"]["country"],
        city=city_name,
    )

def feels_like_icon(temp: float) -> str:
    """
    Ajoute une icône selon la température ressentie.
    """
    if temp >= 30:
        return "🥵"
    elif temp >= 20:
        return "🙂"
    elif temp >= 10:
        return "🧥"
    else:
        return "🥶"

#usage classe pour data
def display_weather(weather: Weather) -> None:
    """
    Affiche les données météo de façon lisible.
    """
    print("\n" + "=" * 40)
    print(f"🌍 {weather.city} ({weather.country})")
    print("=" * 40)

    print(f"🌤️  Météo      : {weather.description}")
    print(f"🌡️  Température: {weather.temp:.1f} °C")
    print(f"{feels_like_icon(weather.feels_like)} Ressenti   : {weather.feels_like:.1f} °C")
    print(f"💧 Humidité    : {weather.humidity} %")
    print(f"💨 Vent       : {weather.wind:.1f} m/s")

    print("=" * 40 + "\n")