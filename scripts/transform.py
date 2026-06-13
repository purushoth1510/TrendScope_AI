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
    "cleaned",
    "cleaned_sales.csv"
)

sales = pd.read_csv(sales_path)

# Convert date
sales["Order Date"] = pd.to_datetime(
    sales["Order Date"]
)

# Month
sales["Month"] = sales["Order Date"].dt.month

# Year
sales["Year"] = sales["Order Date"].dt.year

# Profit Margin
sales["Profit_Margin"] = (
    sales["Profit"] / sales["Sales"]
) * 100

# Handle division by zero
sales["Profit_Margin"] = sales[
    "Profit_Margin"
].fillna(0)

# Revenue Category
sales["Revenue_Category"] = pd.cut(
    sales["Sales"],
    bins=[0,100,500,1000,100000],
    labels=[
        "Low Revenue",
        "Medium Revenue",
        "High Revenue",
        "Premium Revenue"
    ]
)

# Top Product Flag
top_products = sales[
    "Product Name"
].value_counts().head(10).index

sales["Top_Product_Flag"] = sales[
    "Product Name"
].isin(top_products)

output_path = os.path.join(
    BASE_DIR,
    "datasets",
    "processed",
    "processed_sales.csv"
)

sales.to_csv(
    output_path,
    index=False
)

print("Transformation Complete")
print("Saved to processed_sales.csv")