import Large_CSV_Load
import pandas as pd
import sqlite3
import os
import datetime as dt

# fetch data from file
data_file = Large_CSV_Load.large_csv_file

# fetch folder & files of db
db_folder = 'H:\Python Prac\Py_Project\database'
os.makedirs(db_folder, exist_ok=True)
db_file = os.path.join(db_folder,'sales_data.db')
print(f'Found the database file {db_file} to ingest data from {Large_CSV_Load.large_csv_file}')

conn = sqlite3.connect(db_file)

print(f'Connecting to {conn} at {dt.datetime.now()}')
print(f'Connected successfully & performing transformations')

#read csv in chunks
chunksize = 100000  # 100k rows at a time
for chunk in pd.read_csv(data_file, chunksize=chunksize):
    # Transform
    chunk['Total_Sales'] = chunk['Quantity'] * chunk['Unit Price']
    
    # Load into SQLite (append mode)
    chunk.to_sql('sales', conn, if_exists='replace', index=False)
print(f'Data was ingested to {db_file} at {dt.datetime.now()} \n Fetching required result from below query')

# Analyze after all data is loaded
query = "SELECT Product, SUM(Total_Sales) as Total_Sales FROM sales GROUP BY Product"
print(query)
result = pd.read_sql_query(query, conn)
print(f'Query Result:\n {result} \n Connection was closed at at {dt.datetime.now()}')

conn.close()

