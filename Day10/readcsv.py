import pandas as pd

df = pd.read_csv("students.csv")
print(df)
print(df.head())       
print(df.info())       
print(df.describe())   
print(df.isnull().sum())
df["marks"] = df["marks"].fillna(df["marks"].mean())
df["age"] = df["age"].fillna(df["age"].median())
print(df.isnull().sum())
high_scorers = df[df["marks"] > 85]
print(high_scorers)
df["passed"] = df["marks"] > 80
print(df)
df.to_csv("cleaned_students.csv", index=False)
