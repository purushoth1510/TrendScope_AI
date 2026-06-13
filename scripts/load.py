import pandas as pd
import sqlite3
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

csv_path = os.path.join(
    BASE_DIR,
    "datasets",
    "processed",
    "processed_sales.csv"
)

db_path = os.path.join(
    BASE_DIR,
    "database",
    "sqlite.db"
)

df = pd.read_csv(csv_path)

conn = sqlite3.connect(db_path)

df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Data Loaded Successfully")