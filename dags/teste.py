from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow import DAG
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 2, 4),
}

with DAG('spark_example', default_args=default_args, schedule_interval=None) as dag:
    
    submit_spark_job = SparkSubmitOperator(
        task_id='submit_spark_job',
        conn_id='spark_default',  # Essa conexão pode ser configurada diretamente no Airflow UI
        application='/opt/airflow/dags/your_spark_app.py',  # Caminho do seu script Spark
        conf={'spark.master': 'spark://spark-master:7077'},  # Conectar ao spark-master
        name='spark_app_job',
        verbose=True,
    )
