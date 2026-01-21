from src.data_processing.load_data import load_raw_data
from src.data_processing.clean_data import clean_data
from src.data_processing.calculate_internal import calculate_internal

def run_pipeline():
    df = load_raw_data()
    df = clean_data(df)
    df = calculate_internal(df)

    df.to_csv(
        "data/processed/student_internal_processed.csv",
        index=False
    )

    print("✅ Pipeline executed successfully")
    print(df)


if __name__ == "__main__":
    run_pipeline()