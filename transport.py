class Trip:
    def __init__(self, dist, comment="Не регламентировано"):
        self.distance = dist
        self.comment = comment


class Transport:
    def __init__(self, fuel):
        self.fuel = fuel
        self.trips = []

    def add_trip(self, trip):
        self.trips.append(trip)

    def sum_trips_distance(self):
        return sum(trip.distance for trip in self.trips)

    def calculate_reachable_distance(self):
        raise NotImplementedError


class Car (Transport):
    FUEL_CONSUMPTION_CAR = 0.12

    def calculate_reachable_distance(self):
        distance_covered = self.sum_trips_distance()
        result = (self.fuel - (distance_covered *
                               self.FUEL_CONSUMPTION_CAR)) // self.FUEL_CONSUMPTION_CAR
        return f"Топлива осталось на {result} км."


class Airplane (Transport):
    FUEL_CONSUMPTION_AIRPLANE = 200

    def calculate_reachable_distance(self):
        distance_covered = self.sum_trips_distance()
        result = (self.fuel - (distance_covered *
                               self.FUEL_CONSUMPTION_AIRPLANE)) // self.FUEL_CONSUMPTION_AIRPLANE
        return f"Топлива осталось на {result} (часы)"
