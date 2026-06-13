CREATE TABLE products(
product_id INTEGER PRIMARY KEY,
product_name TEXT,
category TEXT,
price REAL
);

CREATE TABLE sales(
sale_id INTEGER PRIMARY KEY,
product_id INTEGER,
quantity INTEGER,
revenue REAL,
sale_date DATE
);

CREATE TABLE trends(
trend_id INTEGER PRIMARY KEY,
product_name TEXT,
trend_score REAL,
trend_date DATE
);