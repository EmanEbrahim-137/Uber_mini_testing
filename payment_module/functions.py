# functions.py

def validate_card(card_number):
    card_number = card_number.replace(" ", "")
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

def process_payment(amount, card_number, ride_id, completed_rides=[]):

    if amount > 500:
        return {"status": "Failed", "message": "Amount exceeds limit"}
    if ride_id in completed_rides:
        return {"status": "Failed", "message": "Duplicate ride payment"}
    if not validate_card(card_number):
        return {"status": "Failed", "message": "Invalid card number"}
    
    completed_rides.append(ride_id)
    return {"status": "Success", "message": "Payment processed"}

def update_ride_status(ride_id, status_dict):
    status_dict[ride_id] = "Completed"
    return status_dict

def record_transaction(ride_id, amount, transaction_list):
    transaction_list.append({"ride_id": ride_id, "amount": amount})
    return transaction_list

def generate_receipt(ride_id, amount):
    return f"Receipt for ride {ride_id}: Amount ${amount} paid successfully."
