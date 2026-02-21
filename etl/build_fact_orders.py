import pandas as pd

def extract():
    """
    Extract raw data and dimension tables.
    """
    orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
    payments = pd.read_csv("data/raw/olist_order_payments_dataset.csv")
    reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")

    customers = pd.read_csv("data/processed/dim_customers.csv")
    time = pd.read_csv("data/processed/dim_time.csv")

    return orders, payments, reviews, customers, time


def transform(orders, payments, reviews, customers, time):
    """
    Build fact_orders table.
    """
    # Convert timestamps to datetime
    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])

    # Aggregate payments to get total payment per order
    payments_agg = payments.groupby("order_id", as_index=False).agg(total_payment=("payment_value", "sum"))

    # Reviews (only score)
    reviews_agg = (reviews.groupby("order_id", as_index=False).agg(review_score=("review_score", "mean")))

    # Merge orders with payments
    fact = orders.merge(payments_agg, on="order_id", how="left")

    # Merge with reviews
    fact = fact.merge(reviews_agg, on="order_id", how="left")

    # Merge with customers to get customer_key
    fact = fact.merge(
        customers[["customer_key", "customer_id"]],
        on="customer_id",
        how="left"
    )

    # Create date_key from order_purchase_timestamp
    fact["date_key"] = fact["order_purchase_timestamp"].dt.strftime("%Y%m%d").astype(int)

    # Select final columns
    fact = fact[
        [
            "order_id",
            "customer_key",
            "date_key",
            "order_status",
            "total_payment",
            "review_score"
        ]
    ]

    return fact


def load(df: pd.DataFrame):
    """
    Load fact_orders to processed folder.
    """
    df.to_csv("data/processed/fact_orders.csv", index=False)
    print("fact_orders saved.")



if __name__ == "__main__":
    orders, payments, reviews, customers, time = extract()
    fact_orders = transform(orders, payments, reviews, customers, time)
    load(fact_orders)
    print(f"fact_orders shape: {fact_orders.shape}")
    # Check for duplicates in order_id
    assert fact_orders["order_id"].is_unique