from src.utils.validation import (
    validate_mid,
    validate_assignment,
    validate_quiz,
    validate_attendance
)

def clean_data(df):
    for col in ["mid1", "mid2"]:
        df = df[df[col].apply(validate_mid)]

    for col in ["assign1", "assign2"]:
        df = df[df[col].apply(validate_assignment)]

    for col in ["quiz1", "quiz2"]:
        df = df[df[col].apply(validate_quiz)]

    df = df[df["attendance"].apply(validate_attendance)]

    return df.reset_index(drop=True)