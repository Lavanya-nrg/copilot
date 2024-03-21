import os
import pandas as pd

# Define the column_defaults dictionary
column_defaults = {
    'transaction_dt': pd.Timestamp('2022-01-01'),  # Example default date
    'unique_trx_id': 'TRX4',
    'item_code': '009',
    'item_sr_no': '2',
    'item_mfg_dt': pd.Timestamp('2022-01-01'),  # Example default date
    'sale_price': 0,  # Example default numerical value
    'disc_price': 0,  # Example default numerical value
    'store_no': '001',
    'store_name': 'estore',
    'customer_id': '1',
    'customer_name': 'shayam',
    'city': 'pune',
    'state': 'maharashtra',
    'zip': '411002'
}

# Rest of your script remains unchanged

# Path to the perfect CSV file
perfect_file_path = "/home/user1/copilot/dataFiles/salesData.csv"

# Path to the folder containing inconsistent files
inconsistent_files_folder = "/home/user1/copilot/dataFiles/inconsistentFiles"

# Output file path
output_file_path = "/home/user1/copilot/dataFiles/outputFile.csv"

# Read the perfect file to get expected columns
perfect_columns = pd.read_csv(perfect_file_path).columns

# Initialize an empty DataFrame to store concatenated data
output_data = pd.DataFrame(columns=perfect_columns)

# Iterate through inconsistent files
for file_name in os.listdir(inconsistent_files_folder):
    file_path = os.path.join(inconsistent_files_folder, file_name)
    
    # Read the inconsistent file
    df = pd.read_csv(file_path)
    
    # Check if all expected columns exist in the DataFrame
    missing_columns = [col for col in perfect_columns if col not in df.columns]
    
    # Add missing columns with default values
    for col in missing_columns:
        df[col] = column_defaults[col]
    
    # Fill missing values with default values
    df.fillna(column_defaults, inplace=True)
    
    # Filter out extra columns
    df = df[perfect_columns]
    
    # Concatenate with output data
    output_data = pd.concat([output_data, df], ignore_index=True)

# Write the output data to a CSV file
output_data.to_csv(output_file_path, index=False)

print("Output file created successfully.")
