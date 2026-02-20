import pandas as pd

def extract_sellers():
    """
    Extract raw sellers data from CSV."""
    sellers = pd.read_csv("data/raw/olist_sellers_dataset.csv")
    return sellers


def transform_sellers(sellers: pd.DataFrame) -> pd.DataFrame:
    """
    Transform raws sellers into dim_sellers dimension table.
     - Remove diplicates 
     - Generate surrogate key.
    """
    # Remove duplicates
    sellers = sellers.drop_duplicates(subset="seller_id", keep="first")

    # Reset index and create surrogate key
    sellers = sellers.reset_index(drop=True)
    sellers["seller_key"] = sellers.index + 1

    # Select final columns
    sellers = sellers[
        [
            "seller_key",
            "seller_id",
            "seller_zip_code_prefix",
            "seller_city",
            "seller_state"
        ]
    ]

    return sellers


def load_sellers(df: pd.DataFrame):
    """
    Save dim_sellers to processed folder.
    """
    df.to_csv("data/processed/dim_sellers.csv", index=False)
    print("dim_sellers saved.")




if __name__ == "__main__":
    sellers_raw = extract_sellers()
    dim_sellers = transform_sellers(sellers_raw)
    load_sellers(dim_sellers)