import os
import pandas as pd
from sqlalchemy import create_engine

# Read password from environment variable
pg_password = os.getenv("PG_PASSWORD")

# PostgreSQL connection string
engine = create_engine(
    f"postgresql+psycopg2://postgres:{pg_password}@localhost:5432/ecommerce_dw"
)


def load_dimension(csv_path, table_name):
    """
    Load a CSV into PostgreSQL dimension table.
    
    Args:
        csv_path: Path to CSV file
        table_name: Table name in schema 'dw'
    """
    df = pd.read_csv(csv_path)
    df.to_sql(
        name=table_name,
        con=engine,
        schema="dw",
        if_exists="append",
        index=False
    )

    print(f"{table_name} loaded successfully")



if __name__ == "__main__":
    load_dimension("data/processed/dim_customers.csv", "dim_customers")
    load_dimension("data/processed/dim_products.csv", "dim_products")
    load_dimension("data/processed/dim_sellers.csv", "dim_sellers")
    load_dimension("data/processed/dim_time.csv", "dim_time")
