import pandas as pd
import sqlite3
import os
# print("Three modules are exist")

data_folder = "H:\Python Prac\Py_Project\data"
os.makedirs(data_folder, exist_ok= True)
csv_file = os.path.join(data_folder,"sales_data.csv")
if not os.path.exists(csv_file):
    sample_data={
        "Order_ID":[1,2,3,4,5],
        "Product":["Monitor","Keyboard","Mouse","Laptop","CPU/GPU"],
        "Quantity":[2,5,3,3,1],
        "Unit Price":[2000,300,250,10000,5000]
    }
    sample_data_load=pd.DataFrame(sample_data)
    sample_data_load.to_csv(csv_file, index=False)
    print(f"Sample data load in to the {csv_file}")
else:
    print(f"{csv_file} is already present")

# Extract data
file_op = pd.read_csv(csv_file)
print(file_op)

#Transform data

file_op['Total Sales'] = file_op['Quantity'] * file_op['Unit Price']
# file_op.dropna(inplace=True)
print(f"Transform data is loaded \n {file_op}")

# Load data into sqlite database

db_folder = 'H:\Python Prac\Py_Project\database'
os.makedirs(db_folder, exist_ok=True)
db_file = os.path.join(db_folder,'sales_data.db')

conn = sqlite3.connect(db_file)
file_op.to_sql('sales', conn, if_exists='replace', index=False)
print(f'data loaded into sqlite db {db_file}\n')

# analyze data with sql 

query = 'SELECT Product, SUM("Total Sales") AS Total_Sales FROM sales GROUP BY Product'
res = pd.read_sql_query(query, conn)
print("Sql analysis result:\n",res)
