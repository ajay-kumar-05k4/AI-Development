import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("iris")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())

df.hist(figsize=(10,6))
plt.suptitle("Histogram of Numerical Features")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(data=df)
plt.title("Boxplot for Outlier Detection")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='species', data=df)
plt.title("Species Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
plt.title("Sepal Length vs Petal Length")
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

sns.pairplot(df, hue="species")
plt.show()

print("EDA Completed for Iris Dataset")
