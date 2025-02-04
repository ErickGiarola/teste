from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago

# Defina o nome da DAG e os parâmetros
dag = DAG(
    'spark_submit_example',  # Nome da DAG
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
    },
    description='Exemplo de DAG para executar um job Spark no Airflow',
    schedule_interval=None,  # Defina para None se não quiser agendar, ou um cronograma
    start_date=days_ago(1),  # Data de início
    catchup=False,
)

# Definindo o operador SparkSubmitOperator
spark_submit_task = SparkSubmitOperator(
    task_id='submit_spark_job',  # ID da task
    application='/opt/airflow/dags/scripts/sample_spark_job.py',  # Caminho para o script Spark
    conn_id='spark_default',  # Conexão que foi configurada no Airflow (opcional, caso tenha configurado)
    executor_memory='2g',  # Memória para o executor do Spark
    total_executor_cores=2,  # Número de núcleos do executor
    driver_memory='1g',  # Memória para o driver do Spark
    name='spark-submit-example',  # Nome do job no Spark
    conf={'spark.some.config.option': 'config-value'},  # Configurações adicionais do Spark
    dag=dag,  # Vincula a task à DAG
)

# Defina a ordem das tasks, neste caso, só temos uma task, então a execução é simples.
spark_submit_task
