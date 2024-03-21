import os
import pandas as pd

# Define the directory containing the files
directory = "copilotFiles"

# Read the perfect file to get the base columns
perfect_df = pd.read_csv("copilotFiles/perfectFile.csv")
base_columns = perfect_df.columns.tolist()

# Define the default values for each column
default_values = {column: "default" for column in base_columns}

# Initialize a list to store DataFrames
dfs = []

# Loop over all CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # Read the file into a DataFrame
        file_df = pd.read_csv(os.path.join(directory, filename))

        # Reorder and add missing columns with default values
        file_df = file_df.reindex(columns=base_columns, fill_value="default")

        # Append the file DataFrame to the list
        dfs.append(file_df)

# Concatenate all DataFrames in the list
df = pd.concat(dfs, ignore_index=True)

# Fill missing values with default values
df = df.fillna(value=default_values)

# Write the DataFrame to an output CSV file
df.to_csv("copilotOutputs/output.csv", index=False)
print("output file generated")