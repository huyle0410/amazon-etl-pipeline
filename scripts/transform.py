import pandas as pd
import numpy as np
import os

def run_transform():
    # Ensure processed folder exists
    os.makedirs("data/processed", exist_ok=True)

    # Load the cleaned data
    df = pd.read_csv("data/processed/amazon_clean.csv")

    # --- your cleaning & feature-engineering code here ---
    # e.g. df['actual_price'] = ...
    # [...]

    # Save the feature-engineered data
    df.to_csv("data/processed/amazon_feature_engineered.csv", index=False)

