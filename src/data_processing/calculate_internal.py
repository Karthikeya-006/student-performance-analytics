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


def calculate_internal(df):
    internal_scores = []

    for _, row in df.iterrows():
        best_mid = max(row["mid1"], row["mid2"])

        assignment_score = (row["assign1"] + row["assign2"]) / 24 * 12
        quiz_score = (row["quiz1"] + row["quiz2"]) / 24 * 12
        attendance_score = attendance_marks(row["attendance"])

        total_internal = (
            best_mid + assignment_score + quiz_score + attendance_score
        )
        total_internal = (total_internal / 47) * 30
        internal_scores.append(round(total_internal, 2))

    df["internal_marks"] = internal_scores
    return df