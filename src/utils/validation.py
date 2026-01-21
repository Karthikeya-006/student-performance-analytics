def validate_marks(value, max_marks):
    if value < 0 or value > max_marks:
        raise ValueError(f"Marks should be between 0 and {max_marks}")
    return value


def validate_attendance(attendance):
    if attendance < 0 or attendance > 100:
        raise ValueError("Attendance must be between 0 and 100")
    return attendance# validation.py
# This file contains all validation rules for student marks

# ---------------- MID VALIDATION ----------------
# Each MID is out of 18
def validate_mid(value):
    try:
        value = float(value)
        return 0 <= value <= 18
    except:
        return False


# ---------------- ASSIGNMENT VALIDATION ----------------
# Each assignment is out of 12
def validate_assignment(value):
    try:
        value = float(value)
        return 0 <= value <= 12
    except:
        return False


# ---------------- QUIZ VALIDATION ----------------
# Each quiz is out of 12
def validate_quiz(value):
    try:
        value = float(value)
        return 0 <= value <= 12
    except:
        return False


# ---------------- ATTENDANCE VALIDATION ----------------
# Attendance is given as percentage (0–100)
def validate_attendance(value):
    try:
        value = float(value)
        return 0 <= value <= 100
    except:
        return False