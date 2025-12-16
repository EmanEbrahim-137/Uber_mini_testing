import pytest
from feedback_module import add_feedback, get_feedback, get_average_rating
from feedback_module import feedbacks, user_feedback_map

@pytest.fixture
def clear_data():
    feedbacks.clear()
    user_feedback_map.clear()

def test_add_feedback_success(clear_data):
    result = add_feedback("R01", "U01", "D01", 5, "Excellent ride")
    assert result["status"] == "Success"

def test_add_feedback_invalid_rating(clear_data):
    result = add_feedback("R02", "U01", "D01", 7)
    assert result["status"] == "Failed"

def test_duplicate_feedback(clear_data):
    add_feedback("R03", "U01", "D01", 4)
    result = add_feedback("R03", "U01", "D01", 5)
    assert result["status"] == "Failed"

def test_get_feedback(clear_data):
    add_feedback("R04", "U02", "D02", 5)
    feedback_list = get_feedback("D02")
    assert len(feedback_list) == 1

def test_average_rating(clear_data):
    add_feedback("R05", "U01", "D03", 4)
    add_feedback("R06", "U02", "D03", 5)
    assert get_average_rating("D03") == 4.5
