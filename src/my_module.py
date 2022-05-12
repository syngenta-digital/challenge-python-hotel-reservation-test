import re


class Hotel:
    def __init__(
        self,
        name,
        rate,
        regular_weekday_price,
        reward_weekday_price,
        regular_weekend_price,
        reward_weekend_price,
    ):
        self.rate = rate
        self.name = name
        self.regular_weekday_price = regular_weekday_price
        self.reward_weekday_price = reward_weekday_price
        self.regular_weekend_price = regular_weekend_price
        self.reward_weekend_price = reward_weekend_price


class Budget:
    def __init__(self, hotel, client_scheduling):
        self.hotel_name = hotel.name
        self.hotel_rate = hotel.rate
        self.is_reward = client_scheduling[0] in "Rewards"
        self.client_schedule = client_scheduling[1:]

        def total_price(self, is_reward, hotel, client_schedule):
            price = 0

            for day in client_schedule:

                if is_reward:

                    if day in "mon tues wed thur fri":
                        price += hotel.reward_weekday_price

                    else:
                        price += hotel.reward_weekend_price

                else:
                    if day in "mon tues wed thur fri":
                        price += hotel.regular_weekday_price

                    else:
                        price += hotel.regular_weekend_price
            return price

        self.total_price = total_price(
            self, self.is_reward, hotel, self.client_schedule
        )

    def __lt__(self, other):

        if self.total_price == other.total_price:
            return self.hotel_rate > other.hotel_rate

        else:
            return self.total_price < other.total_price

    def __le__(self, other):

        if self.total_price == other.total_price:
            return self.hotel_rate >= other.hotel_rate

        else:
            return self.total_price <= other.total_price

    def __eq__(self, other):

        if self.total_price == other.total_price:
            return self.hotel_rate == other.hotel_rate

        else:
            return self.total_price == other.total_price

    def __ne__(self, other):

        if self.total_price == other.total_price:
            return self.hotel_rate != other.hotel_rate

        else:
            return self.total_price != other.total_price

    def __gt__(self, other):

        if self.total_price == other.total_price:
            return self.hotel_rate < other.hotel_rate

        else:
            return self.total_price > other.total_price

    def __ge__(self, other):

        if self.total_price == other.total_price:
            return self.hotel_rate <= other.hotel_rate

        else:
            return self.total_price >= other.total_price

    def __str__(self):
        return str(self.total_price)


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
