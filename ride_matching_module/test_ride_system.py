


import pytest
from ride_system import RideSystem, Driver

@pytest.mark.matching
def test_match_driver_success():
    system = RideSystem()
    d1 = Driver("Driver1")
    system.add_driver(d1)
    ride = system.request_ride("User1")
    assert ride.driver == d1
    assert ride.eta == 10

@pytest.mark.no_driver
def test_no_driver_available():
    system = RideSystem()
    ride = system.request_ride("User1")
    assert ride.driver is None
    assert ride.eta is None

@pytest.mark.cancel
def test_cancel_ride():
    system = RideSystem()
    d1 = Driver("Driver1")
    system.add_driver(d1)
    ride = system.request_ride("User1")
    system.cancel_ride(ride)
    assert ride.driver is None
    assert ride.eta is None
    assert d1.available == True

@pytest.mark.rematch
def test_re_match_after_cancel():
    system = RideSystem()
    d1 = Driver("Driver1")
    system.add_driver(d1)
    ride1 = system.request_ride("User1")
    system.cancel_ride(ride1)
    ride2 = system.request_ride("User2")
    assert ride2.driver == d1
    assert ride2.eta == 10
