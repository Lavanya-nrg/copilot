import pandas as pd
import random
import string
from random import randint
from faker import Faker
import numpy as np
fake = Faker()
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
    }

    # Create a DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Write the DataFrame to a CSV file
    df.to_csv(f"output{i}.csv", index=False)