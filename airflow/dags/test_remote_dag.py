from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'Operativka',
    'start_date': datetime(2024, 11, 14),
    'retries': 1,
    'catchup': False,
}

dag = DAG(
    'test_dag',
    default_args=default_args,
    schedule_interval='@daily',
)

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> end