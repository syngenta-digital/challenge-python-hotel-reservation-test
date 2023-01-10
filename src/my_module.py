import re
from src.entities import Hotel, Budget

def clean_data(stay_str):
    data = re.sub(r"\W+", " ", stay_str).split()
    stay_days = []

    if len(data) < 3 or (data[0] not in "Regulars" and data[0] not in "Rewards"):
        return None

    for i, day in enumerate(data):

        if i % 2 == 0:
            stay_days.append(day)

    return stay_days


def get_cheapest_hotel(data):  # DO NOT change the function's name
    """Finds the cheapest hotel given a schedule. It gives the highest rate hotel if finds equal prices"""
    client_scheduling = clean_data(data)

    if not client_scheduling:
        return "invalid input"

    lakewood = Hotel("Lakewood", 3, 110, 80, 90, 80)
    bridgewood = Hotel("Bridgewood", 4, 160, 110, 60, 50)
    ridgewood = Hotel("Ridgewood", 5, 220, 100, 150, 40)

    lakewood_price = Budget(lakewood, client_scheduling)
    bridgewood_price = Budget(bridgewood, client_scheduling)
    ridgewood_price = Budget(ridgewood, client_scheduling)

    cheapest_hotel = min(lakewood_price, bridgewood_price, ridgewood_price)

    return cheapest_hotel.hotel_name
