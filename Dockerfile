FROM apache/airflow:2.4.0

USER root

ENV DEBIAN_FRONTEND=noninteractive \
    TERM=linux \
    AIRFLOW_GPL_UNIDECODE=yes

RUN apt-get update && apt-get install -y \
    gcc \
    && apt-get clean

USER airflow

# Install python requirements and the algolia-etl CLI
COPY requirements.txt /requirements.txt
COPY setup.py .
COPY algolia_etl ./algolia_etl

RUN pip install --no-cache-dir -r /requirements.txt && \
    pip install -e .

# Copy DAG
COPY dags/ ${AIRFLOW_HOME}/dags/