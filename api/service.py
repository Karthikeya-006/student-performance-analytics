def attendance_marks(attendance_percent):
    if attendance_percent >= 90:
        return 5
    elif attendance_percent >= 80:
        return 4
    elif attendance_percent >= 70:
        return 3
    elif attendance_percent >= 60:
        return 2
    else:
        return 0


def calculate_internal(data):
    best_mid = max(data.mid1, data.mid2)

    assignment_score = ((data.assign1 + data.assign2) / 24) * 12
    quiz_score = ((data.quiz1 + data.quiz2) / 24) * 12
    attendance_score = attendance_marks(data.attendance)

    total_internal = (
        best_mid
        + assignment_score
        + quiz_score
        + attendance_score
    )
    total_internal=(total_internal/47)*30

    return round(total_internal, 2)