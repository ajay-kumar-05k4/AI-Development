from datasets import load_dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds = load_dataset("phihung/titanic", split="train", streaming=True)

data_list = list(ds.take(1000))
df = pd.DataFrame(data_list)

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

if 'Cabin' in df.columns:
    df.drop(columns=['Cabin'], inplace=True)

print(df.isnull().sum())

plt.figure(figsize=(6,4))
sns.countplot(x='Survived', data=df)
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(df['Age'], kde=True)
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=df['Fare'])
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='Sex', hue='Survived', data=df)
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

print("EDA Completed")
