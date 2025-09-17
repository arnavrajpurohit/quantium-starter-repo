import pandas as pd
import os

# Define the file paths
file_paths = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

# Load and combine the data
all_transactions = pd.concat([pd.read_csv(file) for file in file_paths])

# Filter for 'pink morsel' in a case-insensitive manner
pink_morsel_df = all_transactions[all_transactions['product'].str.lower() == 'pink morsel'].copy()

# Clean the price column by removing '$' and converting to float
pink_morsel_df['price'] = pink_morsel_df['price'].str.replace('$', '').astype(float)

# Calculate the 'sales' column
pink_morsel_df['sales'] = pink_morsel_df['quantity'] * pink_morsel_df['price']

# Select the required columns
final_df = pink_morsel_df[['sales', 'date', 'region']]

# Export the final dataframe to a new CSV file
output_path = 'data/output.csv'
final_df.to_csv(output_path, index=False)

print(f"Data processing complete. Final data saved to {output_path}")