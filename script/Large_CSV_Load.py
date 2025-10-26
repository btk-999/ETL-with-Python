import pandas as pd
import numpy as np
import os

data_folder = 'H:\Python Prac\Py_Project\data_huge'
os.makedirs(data_folder, exist_ok=True)
large_csv_file = os.path.join(data_folder,'large_sales_data.csv')
# if not os.path.exists(large_csv_file):
#     sample_data = {

#     }
num_rows = 1000000
np.random.seed(10)
print(f'Ingesting the data into {large_csv_file}')
lg_data = pd.DataFrame({
    "OrderID": np.arange(1, num_rows + 1),
    "Product": np.random.choice(["Laptop", "Mouse", "Keyboard", "Monitor", "Speaker", "Mobiles", "Laptop Charger", "Mobile Cover", "Screen Guard"], size=num_rows),
    "Quantity": np.random.randint(1, 40, size=num_rows),
    "Unit Price": np.random.randint(1000, 30000, size=num_rows),
    "CustomerID": np.random.randint(1345, 999999, size = num_rows),
    "Product Available Count": np.random.randint(25,100, size=num_rows),
    "Total Prodcut Count": np.random.randint(150, 300, size=num_rows),
    "ProductID": np.random.randint(111,999, size=num_rows),
    "Market Label": np.random.choice(["BTK","DNK","MLK","SRV","ACT","RSK","SNT","BNG"], size=num_rows),
    "Location": np.random.choice(["NA","-","#NA"], size=num_rows),
    "Item Code": np.random.choice(["23","56","12","98","52","34","23","876","156","61","33","123","89","31","78","09","04","07","20","00"], size=num_rows),
    "Access Code": np.random.randint(333, 888, size=num_rows),
    "ItemID": np.arange(1, num_rows+1)
})
lg_data.to_csv(large_csv_file, index =False)
print(f"Huge CSV created at {large_csv_file} with {num_rows} rows")
