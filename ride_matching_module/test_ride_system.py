import pytest
from ride_matching import (
    Driver,
    request_ride,
    search_drivers,
    match_driver,
    calculate_eta,
)


@pytest.mark.fail
def test_request_ride_fail():
    ride = request_ride("R1", None)
    assert ride is None


@pytest.mark.fail
def test_search_drivers_fail():
    drivers = [Driver(1, (0, 0), available=False)]
    result = search_drivers(drivers)
    assert result == []


@pytest.mark.pass_test
def test_match_driver_pass():
    ride = request_ride("R2", (0, 0))
    drivers = [
        Driver(1, (5, 5)),
        Driver(2, (1, 1)),
    ]
    result = match_driver(ride, drivers)
    assert result is True
    assert ride.driver.driver_id == 2


@pytest.mark.fail
def test_calculate_eta_fail():
    eta = calculate_eta((0, 0), (10, 10))
    assert eta != 5  # force failure


@pytest.mark.fail
def test_no_drivers_fail():
    ride = request_ride("R3", (1, 1))
    result = match_driver(ride, [])
    assert result is False




# pytest -v -m fail
# pytest -v -m pass_test

