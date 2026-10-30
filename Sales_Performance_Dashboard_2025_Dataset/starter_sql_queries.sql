-- Sales Performance Dashboard 2025
-- Recommended database: MySQL / SQL Server

CREATE DATABASE IF NOT EXISTS sales_dashboard_2025;
USE sales_dashboard_2025;

-- Load the CSV files into these tables:
-- dim_region
-- dim_customer
-- dim_product
-- dim_date
-- fact_sales

-- Example validation queries:

SELECT COUNT(*) AS total_orders FROM fact_sales;

SELECT
    YEAR(OrderDate) AS SalesYear,
    MONTH(OrderDate) AS SalesMonth,
    ROUND(SUM(SalesAmount), 2) AS TotalSales,
    ROUND(SUM(Profit), 2) AS TotalProfit
FROM fact_sales
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
ORDER BY SalesYear, SalesMonth;

SELECT
    r.Region,
    ROUND(SUM(f.SalesAmount), 2) AS TotalSales,
    ROUND(SUM(f.Profit), 2) AS TotalProfit
FROM fact_sales f
JOIN dim_customer c ON f.CustomerID = c.CustomerID
JOIN dim_region r ON c.RegionID = r.RegionID
GROUP BY r.Region
ORDER BY TotalSales DESC;

SELECT
    p.Category,
    ROUND(SUM(f.SalesAmount), 2) AS TotalSales,
    ROUND(SUM(f.Profit), 2) AS TotalProfit
FROM fact_sales f
JOIN dim_product p ON f.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY TotalSales DESC;
