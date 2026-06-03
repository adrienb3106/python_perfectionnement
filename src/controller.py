from typing import Any
from view import display_locations


def choose_location(locations: list[dict[str, Any]]) -> dict[str, Any] | None:
    """
    Permet à l'utilisateur de choisir une localisation parmi plusieurs résultats.
    """
    display_locations(locations)

    if len(locations) == 1:
        return locations[0]

    try:
        choice = int(input("Choisissez une ville : ")) - 1
    except ValueError:
        print("Entrée invalide")
        return None

    if choice < 0 or choice >= len(locations):
        print("Choix invalide")
        return None

    return locations[choice]


def get_city_name_and_coordinates(locations: list[dict[str, Any]]) -> tuple[str, float, float] | None:
    """
    Prend une liste de localisations et retourne la sélection utilisateur.
    """
    if not locations:
        return None

    selected = choose_location(locations)

    if selected is None:
        return None

    return selected["name"], selected["lat"], selected["lon"]


def get_mode() -> str | None:
    """
    Permet à l'utilisateur de choisir entre la prévision météo ou la météo actuelle.
    """
    choice = input("Votre choix : ").strip()
    if choice not in ("1", "2"):
        print("Choix invalide")
        return None
    return choice