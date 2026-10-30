# Sales Performance Dashboard 2025 Dataset

## Files

- dim_date.csv — Date dimension for time intelligence
- dim_region.csv — Regional dimension
- dim_customer.csv — Customer and segment information
- dim_product.csv — Product, category, price and cost information
- fact_sales.csv — 10,000 sales transactions
- starter_sql_queries.sql — Initial SQL validation and analysis queries

## Relationships

dim_date[Date] 1 ---- * fact_sales[OrderDate]
dim_customer[CustomerID] 1 ---- * fact_sales[CustomerID]
dim_product[ProductID] 1 ---- * fact_sales[ProductID]
dim_region[RegionID] 1 ---- * dim_customer[RegionID]

## Intended Power BI skills

- Power Query
- Star schema
- Relationships
- DAX measures
- Time intelligence
- Slicers
- Drill-through
- KPI cards
- Interactive reporting
