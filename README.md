# Algolia Data Engineer Assignment

This project implements an ETL pipeline to handle data related to
Shopify configuration using Airflow and Docker. Tests are also implemented.
The backfill logic is straightforward, each run being focused on a single day.

## Prerequisites

- docker
- docker-compose

## Setup and Running

1. Clone the repository

2. Export the AWS access and secret keys. Build and start the Docker containers:

```
export AWS_ACCESS_KEY_ID=youraccesskey
export AWS_SECRET_ACCESS_KEY=yoursecretkey
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker-compose up --build
```

If you have already built your Docker image once, you can remove
the '--build' flag.

3. Access the Airflow web interface at `http://localhost:8080`

4. The DAG 'shopify_config_etl' should be visible and ready to run.

## Using the CLI

The ETL process can be run using the algolia-etl CLI:

```
algolia-etl run-etl --start-date 2019-04-01 --end-date 2019-04-07
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
python -m unittest discover tests
```

# Notes

- The pipeline can process files between two dates.
- Ensure that your AWS credentials are properly configured for S3 access.
- Modify the PostgreSQL connection string in the DAG file if needed.

## To respect coding conventions

- Install _flake8_ and _black_
- Run :
```
black .
flake8 .
```
If there are still warnings poping up, you'll need to modify the code manually (like when lines are too long).


### Improvements for production

Lots of improvements could be brought to this project.
Here are some main ideas: 

- Use github actions to test the code before deploying it
- Build the docker image and store it in a registry (ex: ECR)
- Increase the number of celery nodes to scale up for production
- Use a secret manager to store credentials
- Use an AWS IAM Role to authenticate
- Use cloud logging, like through CloudWatch
- Instead of using a container-based database, use a cloud based one (like RDS for PostgreSQL)
- Push metrics and implement monitoring (with Prometheus/Grafana)
- Create Data Quality checks