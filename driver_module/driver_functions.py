# driver_functions.py

def register_driver(driver_id, license_number, registered_drivers):
    if not driver_id or not license_number:
        return {"status": "Failed", "message": "Missing required data"}

    if len(license_number) < 6:
        return {"status": "Failed", "message": "Invalid license number"}

    registered_drivers.add(driver_id)
    return {"status": "Success", "message": "Driver registered successfully"}


def accept_ride(driver_id, ride_id, driver_status):
    if driver_status.get(driver_id) == "On Ride":
        return {"status": "Failed", "message": "Driver already on a ride"}

    driver_status[driver_id] = "On Ride"
    return {"status": "Success", "message": "Ride accepted"}


def reject_ride(driver_id, ride_id):
    return {
        "status": "Success",
        "message": f"Ride {ride_id} rejected by driver {driver_id}"
    }


def update_location(driver_id, location, driver_locations):
    if not location or len(location) != 2:
        return {"status": "Failed", "message": "Invalid location data"}

    driver_locations[driver_id] = location
    return {"status": "Success", "message": "Location updated"}


def complete_ride(driver_id, driver_status):
    if driver_status.get(driver_id) != "On Ride":
        return {"status": "Failed", "message": "Driver not on a ride"}

    driver_status[driver_id] = "Available"
    return {"status": "Success", "message": "Ride completed"}
