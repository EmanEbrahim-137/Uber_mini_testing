# functions.py

def validate_card(card_number):
    card_number = "".join(c for c in card_number if c.isdigit())
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

def update_ride_status(ride_id, status_dict):
    status_dict[ride_id] = "Completed"
    return status_dict

def record_transaction(ride_id, amount, transaction_list):
    transaction_list.append({"ride_id": ride_id, "amount": amount})
    return transaction_list

def generate_receipt(ride_id, amount):
    return f"Receipt for ride {ride_id}: Amount ${amount} paid successfully."

def process_payment(amount, card_number, ride_id, completed_rides=None, ride_status_dict=None, transaction_records=None):
    if completed_rides is None:
        completed_rides = []
    if ride_status_dict is None:
        ride_status_dict = {}
    if transaction_records is None:
        transaction_records = []

    if amount > 500:
        return {"status": "Failed", "message": "Amount exceeds limit"}
    if ride_id in completed_rides:
        return {"status": "Failed", "message": "Duplicate ride payment"}
    if not validate_card(card_number):
        return {"status": "Failed", "message": "Invalid card number"}
    
    completed_rides.append(ride_id)
    update_ride_status(ride_id, ride_status_dict)
    record_transaction(ride_id, amount, transaction_records)
    receipt = generate_receipt(ride_id, amount)
    return {"status": "Success", "message": "Payment processed"}
 


