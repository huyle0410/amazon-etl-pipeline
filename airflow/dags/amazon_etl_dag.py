from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Ensure your repo root is on PYTHONPATH so scripts can import
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from scripts.extract import run_extract
from scripts.transform import run_transform
from scripts.load import run_load

default_args = {
    "owner": "huyle0410",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="amazon_etl_pipeline",
    default_args=default_args,
    description="ETL pipeline for Amazon reviews",
    schedule_interval="@daily",
    start_date=datetime(2025, 7, 1),
    catchup=False,
    tags=["amazon", "etl"],
) as dag:

    t1 = PythonOperator(
        task_id="extract",
        python_callable=run_extract,
    )

    t2 = PythonOperator(
        task_id="transform",
        python_callable=run_transform,
    )

    t3 = PythonOperator(
        task_id="load",
        python_callable=run_load,
    )

    t1 >> t2 >> t3

