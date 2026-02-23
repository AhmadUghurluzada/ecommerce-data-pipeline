import pandas as pd
from sqlalchemy import create_engine
import os

# Use environment variable for password
pg_password = os.getenv("PG_PASSWORD")

engine = create_engine(
    f"postgresql+psycopg2://postgres:{pg_password}@localhost:5432/ecommerce_dw"
)


def load_fact_orders_table():
    """
    Load a fact table CSV into PostgreSQL.
    - Drops rows with null dimension keys
    - Ensures integer surrogate keys
    """
    fact = pd.read_csv("data/processed/fact_orders.csv")

    # Drop rows with missing keys
    fact = fact.dropna(subset=["customer_key", "date_key"], how='any')

    # Convert keys to integers
    for col in ["customer_key", "date_key"]:
        fact[col] = fact[col].astype(int)

    # Load into Postgres
    fact.to_sql(
        name="fact_orders",
        con=engine,
        schema="dw",
        if_exists="append",  # append to existing table
        index=False
    )

    print(f"fact_orders loaded. Rows: {fact.shape[0]}")




def load_fact_order_items_table():
    """
    Load a fact table CSV into PostgreSQL.
    - Drops rows with null dimension keys
    - Ensures integer surrogate keys
    """
    fact = pd.read_csv("data/processed/fact_order_items.csv")

    # Drop rows with missing keys
    fact = fact.dropna(subset=["customer_key", "date_key", "seller_key", "date_key"], how='any')

    # Convert keys to integers
    for col in ["customer_key", "product_key", "seller_key", "date_key"]:
        fact[col] = fact[col].astype(int)

    # Load into Postgres
    fact.to_sql(
        name="fact_order_items",
        con=engine,
        schema="dw",
        if_exists="append",  # append to existing table
        index=False      # faster inserts
    )

    print(f"fact_order_items loaded. Rows: {fact.shape[0]}")



if __name__ == "__main__":
    load_fact_order_items_table()