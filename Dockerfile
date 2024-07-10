FROM apache/airflow:2.4.0

USER root

RUN apt-get update && apt-get install -y \
    gcc \
    && apt-get clean

USER airflow

# Install python requirements and the algolia-etl CLI
COPY requirements.txt /requirements.txt
COPY setup.py .
COPY algolia_etl /algolia_etl

RUN ls -la /opt/airflow

RUN pip install --no-cache-dir -r /requirements.txt && \
    pip install -e .

# Copy DAG
COPY dags/ ${AIRFLOW_HOME}/dags/