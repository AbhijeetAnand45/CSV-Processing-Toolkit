import pandas as pd
# Load the CSV files into DataFrames
df1 = pd.read_csv('outputns.csv')
df2 = pd.read_csv('outputew.csv')

# Merge the DataFrames based on the common column
merged = pd.concat([df1, df2], axis=0, ignore_index=True)
print(merged)
# merged_df = pd.merge(df1, df2, on='common_column')

# Save the merged DataFrame to a new CSV file
merged.to_csv('merged_file.csv', index=False)