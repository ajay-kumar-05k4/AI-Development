import pandas as pd

# Creating a sample DataFrame
data = {
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [50000, 60000, 55000, 65000, 70000, 75000]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Grouping by Department and calculating mean salary
grouped = df.groupby('Department')['Salary'].mean()
print("\nMean salary by Department:")
print(grouped)

# Grouping by Department and getting count of employees
count_grouped = df.groupby('Department')['Employee'].count()
print("\nNumber of employees by Department:")
print(count_grouped)

# Grouping by Department and aggregating multiple functions
agg_grouped = df.groupby('Department')['Salary'].agg(['mean', 'sum', 'count'])
print("\nAggregated salary statistics by Department:")
print(agg_grouped)
