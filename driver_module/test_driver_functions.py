# test_driver_functions.py

import pytest
from driver_functions import (
    register_driver,
    accept_ride,
    reject_ride,
    update_location,
    complete_ride
)

# ---------- Fixtures ----------

@pytest.fixture
def registered_drivers():
    return set()

@pytest.fixture
def driver_status():
    return {}

@pytest.fixture
def driver_locations():
    return {}


# ---------- Driver Registration Tests ----------

@pytest.mark.driver
def test_register_driver_success(registered_drivers):
    result = register_driver("D01", "LIC12345", registered_drivers)
    assert result["status"] == "Success"
    assert "D01" in registered_drivers


@pytest.mark.driver
def test_register_driver_missing_data(registered_drivers):
    result = register_driver("", "LIC12345", registered_drivers)
    assert result["status"] == "Failed"
    assert "Missing" in result["message"]


@pytest.mark.driver
def test_register_driver_invalid_license(registered_drivers):
    result = register_driver("D02", "123", registered_drivers)
    assert result["status"] == "Failed"
    assert "Invalid" in result["message"]


# ---------- Accept Ride Tests ----------

@pytest.mark.ride
def test_accept_ride_success(driver_status):
    result = accept_ride("D01", "R01", driver_status)
    assert result["status"] == "Success"
    assert driver_status["D01"] == "On Ride"


@pytest.mark.ride
def test_accept_ride_driver_busy(driver_status):
    driver_status["D01"] = "On Ride"
    result = accept_ride("D01", "R02", driver_status)
    assert result["status"] == "Failed"
    assert "already" in result["message"]


# ---------- Reject Ride Tests ----------

@pytest.mark.ride
def test_reject_ride():
    result = reject_ride("D01", "R03")
    assert result["status"] == "Success"
    assert "rejected" in result["message"]


# ---------- Update Location Tests ----------

@pytest.mark.location
def test_update_location_success(driver_locations):
    result = update_location("D01", (30.1, 31.2), driver_locations)
    assert result["status"] == "Success"
    assert driver_locations["D01"] == (30.1, 31.2)


@pytest.mark.location
def test_update_location_invalid(driver_locations):
    result = update_location("D01", (30.1,), driver_locations)
    assert result["status"] == "Failed"
    assert "Invalid" in result["message"]


# ---------- Complete Ride Tests ----------

@pytest.mark.ride
def test_complete_ride_success(driver_status):
    driver_status["D01"] = "On Ride"
    result = complete_ride("D01", driver_status)
    assert result["status"] == "Success"
    assert driver_status["D01"] == "Available"


@pytest.mark.ride
def test_complete_ride_not_on_ride(driver_status):
    driver_status["D01"] = "Available"
    result = complete_ride("D01", driver_status)
    assert result["status"] == "Failed"
    assert "not on a ride" in result["message"]



# run : & "C:\Program Files\Python313\python.exe" -m pytest -v