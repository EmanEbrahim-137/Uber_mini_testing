# feedback_module.py

from typing import Dict, List

# ------------------------------
# Data storage (dummy, in-memory)
# ------------------------------
feedbacks: Dict[str, List[Dict]] = {}  # key = driver_id, value = list of feedbacks
user_feedback_map: Dict[str, List[str]] = {}  # key = user_id, value = list of ride_ids to prevent duplicates


# ------------------------------
# Add feedback
# ------------------------------
def add_feedback(ride_id: str, user_id: str, driver_id: str, rating: int, comment: str = "") -> Dict:
    """
    Adds a feedback for a driver.
    Rules:
    - Rating must be 1-5
    - One feedback per ride per user
    """

    # Validate rating
    if not (1 <= rating <= 5):
        return {"status": "Failed", "message": "Rating must be between 1 and 5"}

    # Prevent duplicate feedback for same ride
    if user_feedback_map.get(user_id) and ride_id in user_feedback_map[user_id]:
        return {"status": "Failed", "message": "Feedback already submitted for this ride"}

    # Add feedback
    feedback_entry = {"ride_id": ride_id, "user_id": user_id, "rating": rating, "comment": comment}

    if driver_id not in feedbacks:
        feedbacks[driver_id] = []

    feedbacks[driver_id].append(feedback_entry)

    if user_id not in user_feedback_map:
        user_feedback_map[user_id] = []
    user_feedback_map[user_id].append(ride_id)

    return {"status": "Success", "message": "Feedback submitted successfully"}


# ------------------------------
# Get all feedback for a driver
# ------------------------------
def get_feedback(driver_id: str) -> List[Dict]:
    return feedbacks.get(driver_id, [])


# ------------------------------
# Get average rating for a driver
# ------------------------------
def get_average_rating(driver_id: str) -> float:
    driver_feedbacks = feedbacks.get(driver_id, [])
    if not driver_feedbacks:
        return 0.0
    total = sum(f["rating"] for f in driver_feedbacks)
    return round(total / len(driver_feedbacks), 2)


# ------------------------------
# Example usage / testing
# ------------------------------
if __name__ == "__main__":
    # Dummy data
    rides = ["R001", "R002", "R003"]
    users = ["U01", "U02"]
    driver = "D01"

    # Add feedback
    print(add_feedback("R001", "U01", driver, 5, "Great ride!"))
    print(add_feedback("R002", "U02", driver, 4, "Good service"))
    print(add_feedback("R001", "U01", driver, 3, "Duplicate feedback?"))  # should fail

    # Display all feedbacks
    print("All feedbacks:", get_feedback(driver))

    # Average rating
    print("Average rating:", get_average_rating(driver))
