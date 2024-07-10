import click
from datetime import datetime, timedelta
import pandas as pd
from .extract import extract
from .transform import transform
from .load import load

@click.group()
def cli():
    """Algolia ETL CLI"""
    pass

def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

@cli.command()
@click.option('--start-date', required=True, help='Start date in YYYY-MM-DD format')
@click.option('--end-date', required=True, help='End date in YYYY-MM-DD format')
@click.option('--table-name', default='algolia_output', help='PostgreSQL table name')
def run_etl(start_date, end_date, db_uri, table_name):
    """Run the entire ETL process for a date range"""
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    for date in date_range(start, end):
        date_str = date.strftime('%Y-%m-%d')
        click.echo(f"Processing data for {date_str}")

        # Extract
        df = extract(date)
        click.echo(f"Extracted {len(df)} rows")

        # Transform
        df_transformed = transform(df)
        click.echo(f"Transformed data: {len(df_transformed)} rows")

        # Load
        load(df_transformed, table_name)
        click.echo(f"Loaded {len(df_transformed)} rows to {table_name}")

    click.echo("ETL process completed for all dates")

if __name__ == '__main__':
    cli()