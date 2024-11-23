from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Define the default arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
with DAG(
    "git_pull_dag",
    default_args=default_args,
    description="A DAG to periodically run git pull",
    schedule_interval="0 * * * *",  # Runs every hour
    start_date=datetime(2024, 1, 1),  # Start date for the DAG
    catchup=False,  # Do not backfill missing runs
    tags=["git", "bash"],
) as dag:

    # Task: Run git pull
    git_pull_task = BashOperator(
        task_id="git_pull",
        bash_command="cd /home/ubuntu/airflow/AF_Files/dags && git pull origin main",
    )

    # Define the task order
    git_pull_task