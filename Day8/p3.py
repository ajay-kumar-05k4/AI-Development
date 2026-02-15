import pandas as pd

data = {
    "Name": ["Ajay", "Rahul", "Sneha", "Kiran", "Anita"],
    "Age": [21, 22, 20, None, 23],
    "Marks": [85, 90, None, 75, 88],
    "Department": ["CSE", "ECE", "CSE", "IT", "ECE"]
}

df = pd.DataFrame(data)

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df["Department"].unique())
