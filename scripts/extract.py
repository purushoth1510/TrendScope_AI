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

print("Sales Dataset")
print(sales.head())

print("\nSales Columns")
print(sales.columns)

print("\nProducts Dataset")
print(products.head())

print("\nProducts Columns")
print(products.columns)