#!/usr/bin/env python3

from scripts.extract import run_extract
from scripts.transform import run_transform
from scripts.load import run_load

if __name__ == "__main__":
    print("Starting ETL pipeline…")
    run_extract()
    print("→ Extract complete")
    run_transform()
    print("→ Transform complete")
    run_load()
    print("→ Load complete")
    print("ETL pipeline finished successfully.")

