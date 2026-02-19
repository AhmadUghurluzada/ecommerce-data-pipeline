import pandas as pd

def extract_dates():
    """
    Extracts order dates to find min and max date.
    """
    orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
    return orders


def transform_dates(orders: pd.DataFrame) -> pd.DataFrame:
    """"
    Generate dim_time table
    """
    # Convert to datetime
    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])

    # Find min and max date
    min_date = orders["order_purchase_timestamp"].min().date()
    max_date = orders["order_purchase_timestamp"].max().date()

    # Generate date range
    dates = pd.date_range(start=min_date, end=max_date)

    # Create dim_time DataFrame
    dim_time = pd.DataFrame({"full_date": dates})
    dim_time["date_key"] = dim_time["full_date"].dt.strftime("%Y%m%d").astype(int)
    dim_time["year"] = dim_time["full_date"].dt.year
    dim_time["quarter"] = dim_time["full_date"].dt.quarter
    dim_time["month"] = dim_time["full_date"].dt.month
    dim_time["month_name"] = dim_time["full_date"].dt.month_name()
    dim_time["day"] = dim_time["full_date"].dt.day 
    dim_time["weekday"] = dim_time["full_date"].dt.weekday + 1 # Monday=1, Sunday=7
    dim_time["weekday_name"] = dim_time["full_date"].dt.day_name()
    dim_time["is_weekend"] = dim_time["weekday"].isin([6, 7]).astype(int)

    # Sort by date_key
    dim_time = dim_time.sort_values("date_key").reset_index(drop=True)

    return dim_time

def load_dates(df: pd.DataFrame):
    """
    Placeholder load function.
    """
    print("Final dim_time row count:", len(df))
    print(df.head())



if __name__ == "__main__":
    orders_raw = extract_dates()
    dim_time = transform_dates(orders_raw)
    load_dates(dim_time)