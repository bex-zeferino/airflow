#### Importando bibliotecas ####
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import task
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

#### Argumentos Default ####
default_args = {
    'owner': 'Neylson - IGTI', # proprietario
    'depends_on_past': False, # Essa dag depende de algo?
    'start_date': datetime(2021, 7, 18, 19), # A execução começa às 16h do dia 18/07/2021 (GMT -3 [19 - 3])
    'email': ['julio.zeferino@bex-data.com'], # Report para o e-mail
    'email_on_failure': True, # Reporta as falhas
    'email_on_retry': False, # Reporta novas tentativas
    'retries': 1, # configura a quantidade de tentativas
    'retry_delay': timedelta(minutes=1) # tempo entre as tentativas
}

#### DAG ####
dag = DAG(
    'treino-01',
    description='Básico de Bash Operators e Python Operators',
    default_args=default_args,
    schedule_interval=timedelta(minutes=2)
)

#### TASKS ####

# Task 01
hello_bash = BashOperator(
    task_id = 'Hello_Bash', # nome da task
    bash_command='''
    echo "Hello Airflow from Bash!"
    ''', # comando Bash
    dag=dag # seleciona a dag
)

# Task 02
# Criando uma função em python
def say_hello():
    print("Hello Airflow from Python")

# Utilizando o operador
hello_python = PythonOperator(
    task_id='Hello_Python', # nome da task
    python_callable=say_hello, # seleciona a função python que o operador deve executar
    dag=dag
)

#### SCHEDULER ####
hello_bash >> hello_python


