from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2019, 4, 1),
    "end_date": datetime(2019, 4, 8),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "shopify_config_etl",
    default_args=default_args,
    description="Shopify configuration via an ETL",
    schedule_interval="0 2 * * *",
)

etl_task = BashOperator(
    task_id="run_etl",
    bash_command="algolia-etl run-etl --start-date {{ ds }} --end-date {{ ds }}",
    dag=dag
)
