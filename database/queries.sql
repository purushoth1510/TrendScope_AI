-- Total Revenue
SELECT SUM(Sales) AS Total_Revenue
FROM sales;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM sales;

-- Revenue by Category
SELECT
Category,
ROUND(SUM(Sales),2) AS Revenue
FROM sales
GROUP BY Category
ORDER BY Revenue DESC;

-- Profit by Region
SELECT
Region,
ROUND(SUM(Profit),2) AS Profit
FROM sales
GROUP BY Region
ORDER BY Profit DESC;