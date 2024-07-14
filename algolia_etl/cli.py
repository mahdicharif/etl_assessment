import click
from datetime import datetime, timedelta
from .extract import extract
from .transform import transform
from .load import load


@click.group()
def cli():
    """ETL CLI"""
    pass


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)


@cli.command()
@click.option("--start-date", required=True, help="Start date in YYYY-MM-DD format")
@click.option("--end-date", required=True, help="End date in YYYY-MM-DD format")
@click.option("--table-name", default="algolia_output", help="PostgreSQL table name")
def run_etl(start_date, end_date, table_name):
    """
    This function runs the whole ETL process for a date range

    args:
        start_date (string) : the start date
        end_date (string) : the end date
        table_name (string) : the name of the postgres table

    output:
        None, loads data into a table
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    for date in date_range(start, end):
        date_str = date.strftime("%Y-%m-%d")
        click.echo(f"Processing data for {date_str}")

        # Extract
        df_extracted = extract(date)
        click.echo(f"Extracted {len(df_extracted)} rows")

        # Transform
        df_transformed = transform(df_extracted)
        click.echo(f"Transformed data: {len(df_transformed)} rows")

        # Load
        load(df_transformed, table_name)
        click.echo(f"Loaded {len(df_transformed)} rows to {table_name}")

    click.echo("ETL process completed for all dates")


if __name__ == "__main__":
    cli()
