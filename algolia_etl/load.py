from sqlalchemy import create_engine
import os


def load(df, table_name):
    """
    This function loads the transformed data

    input:
        df (dataframe): the transformed dataframe

    output:
        None, loads data into a postgres table
    """
    db_uri = os.getenv("ALGOLIA_DB_URI")
    engine = create_engine(db_uri)
    df.to_sql(table_name, engine, if_exists="append", index=False)
