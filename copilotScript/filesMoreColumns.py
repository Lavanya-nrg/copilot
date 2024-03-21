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
    ["transaction_dt", "unique_trx_id", "item_code", "item_sr_no", "sale_price", "store_no", "store_name", "customer_id", "customer_name", "city", "state", "extra1"],
    ["transaction_dt", "unique_trx_id", "item_code", "item_mfg_dt", "sale_price", "disc_price", "store_no", "store_name", "customer_id", "customer_name", "extra1", "extra2"],
    ["transaction_dt", "unique_trx_id", "item_code", "item_sr_no", "item_mfg_dt", "sale_price", "disc_price", "store_no", "store_name", "customer_id", "extra1", "extra2", "extra3"],
    ["transaction_dt", "unique_trx_id", "item_code", "item_sr_no", "item_mfg_dt", "sale_price", "disc_price", "store_no", "store_name", "customer_name", "city", "state", "zip", "extra1", "extra2"],
    ["transaction_dt", "unique_trx_id", "item_code", "item_sr_no", "item_mfg_dt", "sale_price", "disc_price", "store_no", "store_name", "customer_name", "city", "state", "zip", "extra1", "extra2", "extra3"]
]

# Create directory if it doesn't exist
if not os.path.exists('inconsistent_files'):
    os.makedirs('inconsistent_files')

# Generate random data for each column and write to a CSV file
for i, columns in enumerate(columns_files, 1):
    data = {
        "transaction_dt": pd.date_range(start='1/1/2020', periods=num_rows),
        "unique_trx_id": ["".join(random.choices(string.ascii_uppercase + string.digits, k=10)) for _ in range(num_rows)],
        "item_code": [randint(1000, 9999) if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)],
        "item_sr_no": [randint(1000, 9999) if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "item_sr_no" in columns else None,
        "item_mfg_dt": [fake.date_between(start_date='-1y', end_date='today') if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "item_mfg_dt" in columns else None,
        "sale_price": [round(random.uniform(10.5, 99.9), 2) if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)],
        "disc_price": [round(random.uniform(5.5, 49.9), 2) if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "disc_price" in columns else None,
        "store_no": [randint(1, 10) if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)],
        "store_name": [fake.company() if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)],
        "customer_id": [randint(1000, 9999) if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "customer_id" in columns else None,
        "customer_name": [fake.name() if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "customer_name" in columns else None,
        "city": [fake.city() if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "city" in columns else None,
        "state": [fake.state() if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "state" in columns else None,
        "zip": [fake.zipcode() if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "zip" in columns else None,
        "extra1": [fake.word() if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "extra1" in columns else None,
        "extra2": [fake.word() if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "extra2" in columns else None,
        "extra3": [fake.word() if np.random.rand() > 0.1 else np.nan for _ in range(num_rows)] if "extra3" in columns else None,
    }

    # Create a DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Write the DataFrame to a CSV file
    df.to_csv(f"copilotFiles/inconsistentFiles/files{i}.csv", index=False)