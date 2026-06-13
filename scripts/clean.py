import pandas as pd
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sales_path = os.path.join(
    BASE_DIR,
    "datasets",
    "raw",
    "sales_data.csv"
)

products_path = os.path.join(
    BASE_DIR,
    "datasets",
    "raw",
    "amazon_products.csv"
)

sales = pd.read_csv(
    sales_path,
    encoding="latin1"
)

products = pd.read_csv(
    products_path,
    encoding="latin1"
)

print("Before Cleaning")
print("Sales Shape:", sales.shape)
print("Products Shape:", products.shape)

sales.drop_duplicates(inplace=True)

products.drop_duplicates(inplace=True)

sales.fillna("Unknown", inplace=True)

products.fillna("Unknown", inplace=True)

products.drop(
    columns=["Unnamed: 0"],
    errors="ignore",
    inplace=True
)

cleaned_sales = os.path.join(
    BASE_DIR,
    "datasets",
    "cleaned",
    "cleaned_sales.csv"
)

cleaned_products = os.path.join(
    BASE_DIR,
    "datasets",
    "cleaned",
    "cleaned_products.csv"
)

sales.to_csv(
    cleaned_sales,
    index=False
)

products.to_csv(
    cleaned_products,
    index=False
)

print("\nCleaning Complete")
print("Saved Successfully")