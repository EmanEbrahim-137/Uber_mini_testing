
class Driver:
    def __init__(self, name, available=True):
        self.name = name
        self.available = available

class Ride:
    def __init__(self, user):
        self.user = user
        self.driver = None
        self.eta = None

class RideSystem:
    def __init__(self):
        self.drivers = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def request_ride(self, user):
        ride = Ride(user)
        ride.driver = self.match_driver()
        if ride.driver:
            ride.eta = self.calculate_eta(ride.driver)
        return ride

    def match_driver(self):
        for driver in self.drivers:
            if driver.available:
                driver.available = False  # Driver assigned
                return driver
        return None

    def calculate_eta(self, driver):
        # Simple logic for ETA calculation
        if driver:
            return 10  # ETA in minutes
        return None

    def cancel_ride(self, ride):
        if ride.driver:
            ride.driver.available = True
            ride.driver = None
            ride.eta = None
