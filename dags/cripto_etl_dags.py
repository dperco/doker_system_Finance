# crypto_etl_dag.py
# dags/crypto_etl_dag.py
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime, timedelta
# from scripts.extract import fetch_crypto_data
# from scripts.transform import transform_data
# from scripts.load import load_data

# # Configuración de la base de datos MySQL
# db_config = {
#     'host': 'host.docker.internal',  # Usar 'host.docker.internal' para acceder al host desde Docker
#     'usuario': 'root',
#     'contraseña': '',
#     'base_de_datos': 'cripto_db'
# }

# # Funciones para las tareas
# def extract():
#     return fetch_crypto_data(coin_id='bitcoin', vs_currency='usd', days='30')

# def transform(**kwargs):
#     ti = kwargs['ti']
#     df = ti.xcom_pull(task_ids='extract')
#     return transform_data(df)

# def load(**kwargs):
#     ti = kwargs['ti']
#     df_transformed = ti.xcom_pull(task_ids='transform')
#     load_data(df_transformed, table_name='crypto_prices', db_config=db_config)

# # Definir el DAG
# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': datetime(2023, 10, 1),
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# dag = DAG(
#     'crypto_etl_pipeline',
#     default_args=default_args,
#     description='Un pipeline ETL para datos de criptomonedas',
#     schedule_interval=timedelta(days=1),  # Ejecutar diariamente
# )

# # Definir las tareas
# extract_task = PythonOperator(
#     task_id='extract',
#     python_callable=extract,
#     dag=dag,
# )

# transform_task = PythonOperator(
#     task_id='transform',
#     python_callable=transform,
#     provide_context=True,
#     dag=dag,
# )

# load_task = PythonOperator(
#     task_id='load',
#     python_callable=load,
#     provide_context=True,
#     dag=dag,
# )

# # Definir el flujo de tareas
# extract_task >> transform_task >> load_task


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.extract import fetch_stock_data
from scripts.transform import transform_data
from scripts.load import load_data

# Configuración de la base de datos MySQL
db_config = {
    'host': 'mysql',  # Nombre del servicio de MySQL en docker-compose
    'usuario': 'root',
    'contraseña': 'Zaq12wsx.',
    'base_de_datos': 'cripto_db'
}

# Funciones para las tareas
def extract():
    return fetch_stock_data(symbol='IBM', api_key='')

def transform(**kwargs):
    ti = kwargs['ti']
    df = ti.xcom_pull(task_ids='extract')
    return transform_data(df)

def load(**kwargs):
    ti = kwargs['ti']
    df_transformed = ti.xcom_pull(task_ids='transform')
    load_data(df_transformed, table_name='stock_prices', db_config=db_config)

# Definir el DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'stock_etl_pipeline',
    default_args=default_args,
    description='Un pipeline ETL para datos de acciones',
    schedule_interval=timedelta(days=1),  # Ejecutar diariamente
)

# Definir las tareas
extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform,
    provide_context=True,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load,
    provide_context=True,
    dag=dag,
)

# Definir el flujo de tareas
extract_task >> transform_task >> load_task
