# test_functions.py
import pytest
from functions import validate_card, process_payment, update_ride_status, record_transaction, generate_receipt

@pytest.fixture
def completed_rides():
    return []

@pytest.fixture
def ride_status_dict():
    return {}

@pytest.fixture
def transaction_list():
    return []

@pytest.mark.validation
@pytest.mark.parametrize("card_number, expected", [
    ("4111111111111111", True),
    ("1234567890123456", False),
    ("4000000000000002", True)
])
def test_validate_card(card_number, expected):
    assert validate_card(card_number) == expected


@pytest.mark.payment
def test_process_payment_success(completed_rides):
    result = process_payment(100, "4111111111111111", "ride_1", completed_rides)
    assert result["status"] == "Success"

@pytest.mark.payment
def test_process_payment_amount_exceed(completed_rides):
    result = process_payment(600, "4111111111111111", "ride_2", completed_rides)
    assert result["status"] == "Failed"
    assert "exceeds" in result["message"]

@pytest.mark.payment
def test_process_payment_duplicate_ride(completed_rides):
    process_payment(100, "4111111111111111", "ride_3", completed_rides)
    result = process_payment(50, "4111111111111111", "ride_3", completed_rides)
    assert result["status"] == "Failed"
    assert "Duplicate" in result["message"]

@pytest.mark.payment
def test_process_payment_invalid_card(completed_rides):
    result = process_payment(100, "1234567890123456", "ride_4", completed_rides)
    assert result["status"] == "Failed"
    assert "Invalid" in result["message"]


@pytest.mark.ride
def test_update_ride_status(ride_status_dict):
    updated_status = update_ride_status("ride_5", ride_status_dict)
    assert updated_status["ride_5"] == "Completed"


@pytest.mark.transaction
def test_record_transaction(transaction_list):
    updated_list = record_transaction("ride_6", 120, transaction_list)
    assert len(updated_list) == 1
    assert updated_list[0]["ride_id"] == "ride_6"
    assert updated_list[0]["amount"] == 120


@pytest.mark.receipt
def test_generate_receipt():
    receipt = generate_receipt("ride_7", 80)
    assert "ride_7" in receipt
    assert "$80" in receipt
