import pandas as pd

def load_raw_data():
    path = "data/raw/student_internal_raw.csv"
    return pd.read_csv(path)