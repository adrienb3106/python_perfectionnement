
def choose_location(locations: list[dict[str, Any]]) -> dict[str, Any] | None:
    """
    Permet à l'utilisateur de choisir une localisation parmi plusieurs résultats.
    """
    for i, loc in enumerate(locations):
        name = loc["name"]
        country = loc["country"]
        state = loc.get("state", "")

        label = f"{name}, {state} ({country})" if state else f"{name} ({country})"
        print(f"{i + 1} - {label}")

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