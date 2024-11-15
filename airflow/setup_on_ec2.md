# Airflow on EC2 Instance

## EC2 Configuration

- **Instance Type**: T2.small
- **Key Pair**: Create a new key pair / Use existing one
- **Image**: Ubuntu

## Connect to EC2 Instance

After launching your EC2 instance, connect to it (in aws)

1. Commands to Run

```bash
  sudo apt update
```

2. Install Python 3 and pip:

```bash
   sudo apt install python3-pip
```

3. Install SQLite3:

```bash
   sudo apt install sqlite3
```

4. Install the Python 3.10 virtual environment package:

```bash
   sudo apt install python3.10-venv
```

5. Create a Python virtual environment:

```bash
   python3 -m venv venv
```

6. Activate the virtual environment:

```bash
   source venv/bin/activate
   ```

7. (Optional) Install PostgreSQL development libraries:
```bash
   sudo apt-get install libpq-dev
```

8. Install Apache Airflow with PostgreSQL support:
```bash
   pip install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"
```

9. Initialize the Airflow database:
```bash
   airflow db init
```

10. Install PostgreSQL and its contrib package:
```bash
    sudo apt-get install postgresql postgresql-contrib
```

11. Switch to the PostgreSQL user:
```bash
    sudo -i -u postgres
```

12. Access the PostgreSQL shell:
```bash
    psql
```

13. Create the Airflow database and user:
```sql
    CREATE DATABASE airflow;
    CREATE USER airflow WITH PASSWORD 'airflow';
    GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;
```

14. Exit the PostgreSQL shell by pressing `Ctrl + D`.

15. Navigate to the Airflow directory:
```bash
    cd airflow
```

16. Replace the connection string in the `airflow.cfg` file to use PostgreSQL instead of SQLite:
```bash
    sed -i 's#sqlite:////home/ubuntu/airflow/airflow.db#postgresql+psycopg2://airflow:airflow@localhost/airflow#g' airflow.cfg
```

17. Verify the SQL Alchemy connection string:
```bash
    grep sql_alchemy airflow.cfg
```

18. Check the executor configuration:
```bash
    grep executor airflow.cfg
```

19. Replace `SequentialExecutor` with `LocalExecutor`:
```bash
    sed -i 's#SequentialExecutor#LocalExecutor#g' airflow.cfg
```

20. Re-initialize the Airflow database:
```bash
    airflow db init
```

21. Create an Airflow user:
```bash
    airflow users create -u airflow -f airflow -l airflow -r Admin -e hr.p.hristov@gmail.com
```
    - **Enter Password**: `airflow`
    - **Repeat Password**: `airflow`

22. Update security group inbound rules in your EC2 instance:
    - **Type**: Custom TCP
    - **Port Range**: 8080
    - **Source**: Anywhere (IPV4)
    - **Save** the rules.

23. Start the Airflow webserver:
```bash
    airflow webserver &
```

24. Start the Airflow scheduler:
```bash
    airflow scheduler
```

25. Copy the public IPv4 DNS of your EC2 instance and open it in your browser with port `8080`:
```text
    http://ec2-35-159-175-125.eu-central-1.compute.amazonaws.com:8080/home
```

Use below dag code as a test. make sure to mkdir dag folder and then put this .py script in there!

```python
from airflow import dags
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'Operativka',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = dags(
    'test_dag',
    default_args=default_args,
    schedule_interval='@daily',
)

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> end
```
