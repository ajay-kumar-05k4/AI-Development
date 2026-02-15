import pandas as pd

df = pd.read_csv("ultimate_student_productivity_dataset_5000.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df["gender"].value_counts())
print(df["academic_level"].value_counts())
print(df["internet_quality"].value_counts())
