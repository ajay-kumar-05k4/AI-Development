import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Exporting DataFrame to CSV
df.to_csv('sample_data.csv', index=False)
print("\nDataFrame exported to 'sample_data.csv'")

# Importing DataFrame from CSV
imported_df = pd.read_csv('sample_data.csv')
print("\nImported DataFrame from 'sample_data.csv':")
print(imported_df)

# Note: For Excel export/import, you would use:
# df.to_excel('sample_data.xlsx', index=False)
# imported_df = pd.read_excel('sample_data.xlsx')
