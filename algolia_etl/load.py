from sqlalchemy import create_engine

def load(df, table_name):
    db_uri = os.getenv('ALGOLIA_DB_URI')
    engine = create_engine(db_uri)
    df.to_sql(table_name, engine, if_exists='append', index=False)