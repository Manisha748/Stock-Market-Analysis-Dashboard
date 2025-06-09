from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow import DAG
from datetime import timedelta, datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'eth_price_update_daily',
    default_args=default_args,
    description='Fetch and update daily ETH price',
    schedule_interval='@daily',
    catchup=True,
    tags=['crypto'],
)

run_script = BashOperator(
    task_id='run_eth_price_update',
    bash_command='/home/robert_manisha/airflow_project/eth_tracker/wrapper.sh {{ ds }}',
    dag=dag,
)
