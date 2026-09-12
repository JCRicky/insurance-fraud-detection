"""Module for SQL engine, load raw project data, and run its sql script."""

#packages
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    """Creates a SQLAlchemy engine using .env information."""
    conn_str = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    return create_engine(conn_str)

def load_raw_to_db(csv_path: str, engine, table_name: str = 'raw_claims'):
    """Reading Kaggle CSV to write into the database as raw_claims."""
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    return df

def get_raw_claims(engine, table_name:str = 'raw_claims') -> pd.DataFrame:
    """Read raw_claims from the database to a dataframe."""
    return pd.read_sql(f"SELECT * FROM {table_name}", engine)