from sqlalchemy import create_engine, text
import os
from pandas.io.sql import to_sql

def load(df, table_name):
    """
    This function loads the transformed data, inserting only new rows

    input:
        df (dataframe): the transformed dataframe
        table_name (str): name of the target table

    output:
        None, loads data into a postgres table
    """
    db_uri = os.getenv("ALGOLIA_DB_URI")
    engine = create_engine(db_uri)

    records = df.to_dict('records')

    # Generate the column names
    columns = ', '.join(df.columns)

    # Generate the values
    values = ', '.join([':' + col for col in df.columns])

    # Not inserting the rows for which we already have the primary
    # key 'id'
    query = text(f"""
    INSERT INTO {table_name} ({columns})
    VALUES ({values})
    ON CONFLICT (id) DO NOTHING
    """)

    # Execute the query for each row
    with engine.begin() as conn:
        for row in records:
            conn.execute(query, row)
