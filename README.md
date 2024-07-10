# Algolia Data Engineer Assignment

This project implements a daily ETL pipeline to process Shopify configuration data using Airflow and Docker.

## Prerequisites

- Docker
- Docker Compose

## Setup and Running

1. Clone the repository

2. Build and start the Docker containers:

```
docker-compose up --build
```

3. Access the Airflow web interface at `http://localhost:8080`

4. The DAG 'shopify_config_etl' should be visible and ready to run.

## Using the CLI

The ETL process can be run using the custom CLI:

```
algolia-etl run-etl --start-date 2019-04-01 --end-date 2019-04-07 --db-uri postgresql://airflow:airflow@postgres:5432/airflow
```

## Project Structure

- `algolia_etl/`: Contains the core ETL logic and CLI
- `dags/`: Contains the Airflow DAG definition
- `tests/`: Contains unit tests for the ETL scripts
- `Dockerfile`: Defines the Docker image for Airflow
- `docker-compose.yml`: Defines the services (Airflow, PostgreSQL)
- `requirements.txt`: Lists Python dependencies

## Testing

To run the unit tests:

```
docker-compose run airflow-webserver python -m unittest discover tests
```

# Notes

- The pipeline can process files between two dates.
- Ensure that your AWS credentials are properly configured for S3 access.
- Modify the PostgreSQL connection string in the DAG file if needed.
