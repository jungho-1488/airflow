from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id = "dags_email_operator",
    schedule = "0 8 1 * *",
    start_date = pendulum.datetime(2023, 3, 1, tz = "Asia/Seoul"),
    catchup = False
) as dag:
    send_email_task = EmailOperator(
        task_id = "send_email_task",
        to = "sonic148892@gmail.com",
        subject = "Airflow Email Test",
        html_content = "<h1>This is a test email sent from Airflow</h1>",
    )