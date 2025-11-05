from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd, os

def compact_daily(**_):
    src = "outputs/aggregates_minute.csv"
    if not os.path.exists(src):
        return
    df = pd.read_csv(src, parse_dates=["minute"])
    daily = df.groupby(df["minute"].dt.date).agg(revenue_daily=("revenue_min","sum"),
                                                 items_daily=("items_min","sum")).reset_index()
    daily.rename(columns={"minute":"date"}, inplace=True)
    daily.to_csv("outputs/aggregates_daily.csv", index=False)

with DAG("retail_streaming_compaction",
         start_date=datetime(2025,1,1),
         schedule="0 1 * * *",
         catchup=False,
         default_args={"retries": 1, "retry_delay": timedelta(minutes=5)}) as dag:
    t1 = PythonOperator(task_id="compact_daily", python_callable=compact_daily)
