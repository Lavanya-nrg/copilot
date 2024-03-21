import os
import pandas as pd
import random
import string
from random import randint
from faker import Faker
import numpy as np

fake = Faker()

# Define the number of rows
num_rows = 20

# Define the columns for each file
columns_files = [
    ["transaction_dt", "unique_trx_id", "item_code", "sale_price", "store_no", "store_name"],
    ["transaction_dt", "unique_trx_id", "item_code", "sale_price", "store_no"],
    ["transaction_dt", "unique_trx_id", "item_code", "sale_price"],
    ["transaction_dt", "unique_trx_id", "item_code"],
    ["transaction_dt", "unique_trx_id"]
]

# Create directory if it doesn't exist
if not os.path.exists('inconsistent_files'):
    os.makedirs('inconsistent_files')

# Generate random data for each column and write to a CSV file
for i, columns in enumerate(columns_files, 1):
    data = {
        "transaction_dt": pd.date_range(start='1/1/2020', periods=num_rows),
        "unique_trx_id": ["".join(random.choices(string.ascii_uppercase + string.digits, k=10)) for _ in range(num_rows)],
        "item_code": [randint(1000, 9999) if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "item_code" in columns else None,
        "sale_price": [round(random.uniform(10.5, 99.9), 2) if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "sale_price" in columns else None,
        "store_no": [randint(1, 10) if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "store_no" in columns else None,
        "store_name": [fake.company() if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "store_name" in columns else None,
    }

    # Create a DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Write the DataFrame to a CSV file
    df.to_csv(f"copilotFiles/inconsistentFiles/file{i}.csv", index=False)