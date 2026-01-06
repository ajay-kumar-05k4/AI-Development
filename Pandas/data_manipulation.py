import pandas as pd
import numpy as np

# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, np.nan, 40],
    'City': ['New York', 'London', 'Tokyo', 'Paris'],
    'Salary': [50000, 60000, 55000, 70000]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Selecting a column
print("\nSelecting 'Name' column:")
print(df['Name'])

# Filtering rows where Age > 25
filtered_df = df[df['Age'] > 25]
print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)

# Adding a new column
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with new 'Bonus' column:")
print(df)

# Handling missing values - filling NaN with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)
print("\nDataFrame after filling missing Age values:")
print(df)
