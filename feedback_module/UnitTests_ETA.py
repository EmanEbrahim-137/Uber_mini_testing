# feedback_module.py

from typing import Dict, List

feedbacks: Dict[str, List[Dict]] = {}  
user_feedback_map: Dict[str, List[str]] = {}  


def add_feedback(ride_id: str, user_id: str, driver_id: str, rating: int, comment: str = "") -> Dict:

    if not (1 <= rating <= 5):
        return {"status": "Failed", "message": "Rating must be between 1 and 5"}

    if user_feedback_map.get(user_id) and ride_id in user_feedback_map[user_id]:
        return {"status": "Failed", "message": "Feedback already submitted for this ride"}

    feedback_entry = {"ride_id": ride_id, "user_id": user_id, "rating": rating, "comment": comment}

    if driver_id not in feedbacks:
        feedbacks[driver_id] = []

    feedbacks[driver_id].append(feedback_entry)

    if user_id not in user_feedback_map:
        user_feedback_map[user_id] = []
    user_feedback_map[user_id].append(ride_id)

    return {"status": "Success", "message": "Feedback submitted successfully"}


def get_feedback(driver_id: str) -> List[Dict]:
    return feedbacks.get(driver_id, [])


def get_average_rating(driver_id: str) -> float:
    driver_feedbacks = feedbacks.get(driver_id, [])
    if not driver_feedbacks:
        return 0.0
    total = sum(f["rating"] for f in driver_feedbacks)
    return round(total / len(driver_feedbacks), 2)


if __name__ == "__main__":
    rides = ["R001", "R002", "R003"]
    users = ["U01", "U02"]
    driver = "D01"

    print(add_feedback("R001", "U01", driver, 5, "Great ride!"))
    print(add_feedback("R002", "U02", driver, 4, "Good service"))
    print(add_feedback("R001", "U01", driver, 3, "Duplicate feedback?"))  # should fail

    print("All feedbacks:", get_feedback(driver))

    print("Average rating:", get_average_rating(driver))
