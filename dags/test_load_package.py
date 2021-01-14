from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

import hdfs

def print_hello():
    return 'Hello Wolrd'

def print_lib():
    print (hdfs)

args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2016, 10, 14, 16, 12),
    'retries': 5,
    'schedule_interval': '0 * * * *',
    'retry_delay': timedelta(minutes=1),
}

with DAG(dag_id='test_load_package', 
         default_args=args) as dag:

    start_dag = DummyOperator(task_id='START_dag')

    hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

    end_dag = DummyOperator(task_id='END_dag')

    start_dag >> hello_operator >> print_lib >> end_dag