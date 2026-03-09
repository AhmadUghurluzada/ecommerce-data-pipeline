import pandas as pd

def extract_customers():
    """
    Extracts customers and orders data from CSV files.
    Returns:
        customers (pd.DataFrame): Raw customers dataset 
        orders (pd.DataFrame): Raw orders dataset
    """
    customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
    orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
    return customers, orders


def transform_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """
    Transform raw data into dim_customers dimension table.
    
    Logic:
    1. Merge customers with orders to get the order purchase timestamp.
    2. Sort by most recent purchase per real customer.
    3. Deduplicate based on customer_unique_id.
    4. Generate surrogate key.
    5. Select final columns.

    Returns:
        dim_customers (pd.DataFrame): Transformed customers dimension table.
    """
    # Merge to attach purchase timestamp
    df = customers.merge(
        orders[["order_id", "customer_id", "order_purchase_timestamp"]],
        on="customer_id",
        how="left"
    )

    # Convert to datetime
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

    # Sort by latest purchase per real customer
    df = df.sort_values(
        ["customer_unique_id", "order_purchase_timestamp"],
        ascending=[True, False]
    )

    # Keep most recent address per real customer
    df = df.drop_duplicates(subset="customer_unique_id", keep="first")

    # Reset index and create surrogate key
    df = df.reset_index(drop=True)
    df["customer_key"] = df.index + 1

    # Select dimension columns
    df = df[
        [
            "customer_key",
            "customer_id",
            "customer_unique_id",
            "customer_city",
            "customer_state",
            "customer_zip_code_prefix"
        ]
    ]

    return df


def load_customers(df: pd.DataFrame):
    """
    Save dim_customers to processed folder.
    """
    df.to_csv("data/processed/dim_customers.csv", index=False)
    print("dim_customers saved.")




if __name__ == "__main__":
    customers_raw, orders_row = extract_customers()
    dim_customers = transform_customers(customers_raw, orders_row)
    load_customers(dim_customers)
