<<<<<<< HEAD
# ETL-with-Python
Data Ingestion &amp; Transformation with python
=======
# ETL Data Engineering Project (Python + Pandas + SQLite)

## Overview
This project simulates an **ETL pipeline** using Python, Pandas, and SQLite — all running locally.  
It extracts, transforms, and loads a large CSV dataset into a database for analysis.

## Tech Stack
- Python 3
- Pandas
- SQLite
- VS Code

## Steps
1. Generate synthetic large CSV data (`generate_large_csv.py`)
2. Run ETL process (`etl_large.py`)
3. Analyze results with SQL queries

## Key Learning
- Chunk data loading for large files
- Combine Pandas with SQL
- Basic ETL workflow (Extract, Transform, Load)

## Output Example

Fetching required result from below query
SELECT Product, SUM(Total_Sales) as Total_Sales FROM sales GROUP BY Product
Query Result:
           Product  Total_Sales
0        Keyboard   3480930198
1          Laptop   3469507279
2  Laptop Charger   3423101416
3    Mobile Cover   3529717807
4         Mobiles   3386158042
5         Monitor   3432394800
6           Mouse   3406621821
7    Screen Guard   3464499877
8         Speaker   3422440191
.............
>>>>>>> aa58245 (Initial commit - Data ingestion and transformation project V1.0)
