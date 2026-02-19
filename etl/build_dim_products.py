import pandas as pd

def extract_products():
    """
    Extracts raw products data from CSV.
    """
    products = pd.read_csv("data/raw/olist_products_dataset.csv")
    return products


def transform_products(products: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms raw products data into dim_poducts dimension table.
     - Remove rows with missing numeric measurements (weight, length, height, width).
     - Keep descriptive NULLs 
     - Generate surrogate key.
     """
    # Remove rows with missing numeric measurements
    numeric_cols = ["product_weight_g", "product_length_cm", "product_height_cm", "product_width_cm"]
    products = products.dropna(subset=numeric_cols)

    # Reset index and create surrogate key
    products = products.reset_index(drop=True)
    products["product_key"] = products.index + 1

    # Select final columns
    products = products[
        [
            "product_key", 
            "product_id", 
            "product_category_name", 
            "product_name_lenght", 
            "product_description_lenght", 
             "product_photos_qty", 
            "product_weight_g",
            "product_length_cm", 
            "product_height_cm", 
            "product_width_cm"
         ]
    ]

    return products


def load_products(df: pd.DataFrame):
    """
    wjoerturjeokwap[lwekordjfg]
    """
    print("Final dim_products row count:", len(df))
    print(df.head())



if __name__ == "__main__":
    products_raw = extract_products()
    dim_products = transform_products(products_raw)
    load_products(dim_products)