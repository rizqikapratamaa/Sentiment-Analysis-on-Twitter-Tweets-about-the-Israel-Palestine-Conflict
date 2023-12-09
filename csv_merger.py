import pandas as pd

# Read the csv
df1 = pd.read_csv('gaza.csv')
df2 = pd.read_csv('hamas.csv')
df3 = pd.read_csv('israel.csv')
df4 = pd.read_csv('palestine.csv')

# Merge all of the csv
merged_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Delete duplicate element
merged_df = merged_df.drop_duplicates()

# Delete first column
merged_df = merged_df.iloc[:, 1:]

# Save the new data to new csv
merged_df.to_csv('israel_palestine_conflict.csv', index=False)