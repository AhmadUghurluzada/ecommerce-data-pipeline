import pandas as pd

def extract():
    """
    Extracts all necessary raw and dimension tables.
    """
    order_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
    orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
    customers = pd.read_csv("data/processed/dim_customers.csv")
    products = pd.read_csv("data/processed/dim_products.csv")
    sellers = pd.read_csv("data/processed/dim_sellers.csv")
    time = pd.read_csv("data/processed/dim_time.csv")

    return order_items, orders, customers, products, sellers, time


def transform(order_items, orders, customers, products, sellers, time):
    """
    Build fact_order_items by merging order_items with dimensions and orders to get date_key.
    """
    # Convert timestamps to datetime
    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])

    # Merge order_items with orders
    fact = order_items.merge(
        orders[["order_id", "customer_id", "order_purchase_timestamp", "order_status"]],
        on="order_id",
        how="left"
    )

    # Merge with dim_customers to get customer_key
    fact = fact.merge(
        customers[["customer_key", "customer_id"]],
        on="customer_id",
        how="left"
    )

    # Merge with dim_products to get product_key
    fact = fact.merge(
        products[["product_key", "product_id"]],
        on="product_id",
        how="left"
    )

    # Merge with dim_sellers to get seller_key
    fact = fact.merge(
        sellers[["seller_key", "seller_id"]],
        on="seller_id",
        how="left"
    )

    # Create date_key from order_purchase_timestamp
    fact["date_key"] = fact["order_purchase_timestamp"].dt.strftime("%Y%m%d").astype(int)

    # Select final columns
    fact = fact[
        [
            "order_id",
            "order_item_id",
            "customer_key",
            "product_key",
            "seller_key",
            "date_key",
            "price",
            "freight_value"
        ]
    ]

    return fact


def load(df: pd.DataFrame):
    """
    Loads fact_order_items to processed folder.
    """
    df.to_csv("data/processed/fact_order_items.csv", index=False)
    print("fact_order_items saved.")
    print("fact_order_items shape:", df.shape)
    print(df.head())



if __name__ == "__main__":
    order_items, orders, customers, products, sellers, time = extract()
    fact_order_items = transform(order_items, orders, customers, products, sellers, time)
    load(fact_order_items)
    # Basic sanity checks
    assert fact_order_items["order_item_id"].notna().all()