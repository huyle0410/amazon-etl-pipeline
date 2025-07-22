import pandas as pd
import os

def run_extract():
    # Ensure processed folder exists
    os.makedirs("data/processed", exist_ok=True)

    # Read raw CSV (make sure data/raw/amazon.csv exists)
    df = pd.read_csv("data/raw/amazon.csv")

    # Save cleaned CSV for next step
    df.to_csv("data/processed/amazon_clean.csv", index=False)

