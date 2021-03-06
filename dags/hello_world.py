from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    print ('Diederik says Hello')
    
dag = DAG('hello', description = 'there is a first time for evrything', schedule_interval='0 12 * * *',start_date =datetime(2017,3,20), catchup=False)

dummy_operator =  DummyOperator(task_id='dummy_task', retries=3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

dummy_operator >> hello_operator


