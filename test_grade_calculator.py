"""Automated tests for grade_calculator.py (run with: pytest)."""

import pytest

from grade_calculator import (
    calculate_average,
    get_letter_grade,
    has_passed,
    student_summary,
    validate_score,
)


# ---------- validate_score ----------

def test_validate_score_accepts_valid_score():
    assert validate_score(75) is True


def test_validate_score_accepts_boundaries():
    assert validate_score(0) is True
    assert validate_score(100) is True


def test_validate_score_rejects_above_100():
    with pytest.raises(ValueError):
        validate_score(105)


def test_validate_score_rejects_negative():
    with pytest.raises(ValueError):
        validate_score(-1)


def test_validate_score_rejects_non_number():
    with pytest.raises(TypeError):
        validate_score("80")


# ---------- calculate_average ----------

def test_calculate_average_normal_list():
    assert calculate_average([80, 90, 70]) == 80


def test_calculate_average_rounds_to_two_decimals():
    assert calculate_average([70, 71, 71]) == 70.67


def test_calculate_average_single_score():
    assert calculate_average([65]) == 65


def test_calculate_average_empty_list_raises_error():
    with pytest.raises(ValueError):
        calculate_average([])


def test_calculate_average_invalid_score_raises_error():
    with pytest.raises(ValueError):
        calculate_average([80, 120])


# ---------- get_letter_grade ----------

@pytest.mark.parametrize(
    "average, expected",
    [
        (95, "A"),
        (80, "A"),    # boundary
        (79.9, "B"),  # just below boundary
        (70, "B"),
        (65, "C"),
        (50, "D"),    # boundary
        (49.9, "F"),
        (0, "F"),
    ],
)
def test_get_letter_grade(average, expected):
    assert get_letter_grade(average) == expected


# ---------- has_passed ----------

def test_has_passed_exactly_pass_mark():
    assert has_passed(50) is True


def test_has_passed_below_pass_mark():
    assert has_passed(49.99) is False


def test_has_passed_high_score():
    assert has_passed(90) is True


# ---------- student_summary ----------

def test_student_summary():
    result = student_summary("Ada", [78, 85, 62, 90])
    assert result == {
        "name": "Ada",
        "average": 78.75,
        "grade": "B",
        "passed": True,
    }
