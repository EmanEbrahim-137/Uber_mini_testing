class Driver:
    def __init__(self, driver_id, location, available=True):
        self.driver_id = driver_id
        self.location = location  # (x, y)
        self.available = available


class Ride:
    def __init__(self, ride_id, pickup_location):
        self.ride_id = ride_id
        self.pickup_location = pickup_location
        self.driver = None
        self.status = "Pending"
        self.eta = None


def calculate_distance(loc1, loc2):
    return ((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2) ** 0.5


def request_ride(ride_id, pickup_location):
    if not pickup_location:
        return None
    return Ride(ride_id, pickup_location)


def search_drivers(drivers):
    return [d for d in drivers if d.available]


def match_driver(ride, drivers):
    if not drivers:
        return False

    nearest_driver = min(
        drivers,
        key=lambda d: calculate_distance(d.location, ride.pickup_location)
    )

    ride.driver = nearest_driver
    ride.status = "Matched"
    nearest_driver.available = False
    return True


def calculate_eta(driver_location, pickup_location):
    distance = calculate_distance(driver_location, pickup_location)
    return round(distance * 2)  # simple ETA logic
