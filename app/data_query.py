import duckdb
import pandas as pd
from config import NIM_SQL_API_URL, NIM_API_KEY

def query_data(query: str) -> pd.DataFrame:
    # Example of querying DuckDB on a CSV file, which is in the 'data' directory
    conn = duckdb.connect(database=':memory:')
    conn.execute("CREATE TABLE nyc_taxi_data AS SELECT * FROM 'data/train.csv'")
    result = conn.execute(query).fetchdf()  # Fetch the result as a pandas DataFrame
    return result
