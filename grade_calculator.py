"""
Student Grade Calculator
------------------------
A small module that calculates a student's average score, letter grade
and pass/fail status. Used as the sample project for our Jenkins CI pipeline.
"""

PASS_MARK = 60

GRADE_BOUNDARIES = [
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
]


def validate_score(score):
    """Check that a score is a number between 0 and 100 (inclusive)."""
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError(f"Score must be a number, got {type(score).__name__}")
    if score < 0 or score > 100:
        raise ValueError(f"Score must be between 0 and 100, got {score}")
    return True


def calculate_average(scores):
    """Return the average of a list of scores, rounded to 2 decimal places."""
    if not scores:
        raise ValueError("Cannot calculate the average of an empty list")
    for score in scores:
        validate_score(score)
    return round(sum(scores) / len(scores), 2)


def get_letter_grade(average):
    """Convert an average score into a letter grade (A, B, C, D or F)."""
    validate_score(average)
    for boundary, letter in GRADE_BOUNDARIES:
        if average >= boundary:
            return letter
    return "F"


def has_passed(average):
    """Return True if the average is at or above the pass mark."""
    validate_score(average)
    return average >= PASS_MARK


def student_summary(name, scores):
    """Return a dictionary summarising a student's results."""
    average = calculate_average(scores)
    return {
        "name": name,
        "average": average,
        "grade": get_letter_grade(average),
        "passed": has_passed(average),
    }


if __name__ == "__main__":
    result = student_summary("Example Student", [78, 85, 62, 90])
    print(result)
