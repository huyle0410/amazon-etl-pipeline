import pandas as pd
import sqlite3
import os

def run_load():
    # Ensure database folder exists
    os.makedirs("database", exist_ok=True)

    df = pd.read_csv("data/processed/amazon_feature_engineered.csv")
    conn = sqlite3.connect("database/amazon_reviews.db")
    df.to_sql("amazon_reviews", conn, if_exists="replace", index=False)
    conn.close()

