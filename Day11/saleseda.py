import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv("Warehouse_and_Retail_Sales.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

df["YEAR"] = df["YEAR"].astype(int)
df["MONTH"] = df["MONTH"].astype(int)

df["RETAIL SALES"] = pd.to_numeric(df["RETAIL SALES"], errors="coerce")
df["RETAIL TRANSFERS"] = pd.to_numeric(df["RETAIL TRANSFERS"], errors="coerce")
df["WAREHOUSE SALES"] = pd.to_numeric(df["WAREHOUSE SALES"], errors="coerce")

df.fillna(0, inplace=True)

df["TOTAL SALES"] = df["RETAIL SALES"] + df["WAREHOUSE SALES"] + df["RETAIL TRANSFERS"]
df["SALES_PER_MONTH"] = df["TOTAL SALES"] / 12
df["YEAR_MONTH"] = df["YEAR"].astype(str) + "-" + df["MONTH"].astype(str)

plt.figure(figsize=(8,5))
sns.histplot(df["TOTAL SALES"], kde=True)
plt.title("Distribution of Total Sales")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df["TOTAL SALES"])
plt.title("Boxplot of Total Sales")
plt.show()

plt.figure(figsize=(10,6))
monthly_sales = df.groupby("MONTH")["TOTAL SALES"].sum()
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title("Monthly Total Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

plt.figure(figsize=(10,6))
yearly_sales = df.groupby("YEAR")["TOTAL SALES"].sum()
sns.barplot(x=yearly_sales.index, y=yearly_sales.values)
plt.title("Yearly Total Sales")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.show()

plt.figure(figsize=(10,6))
top_suppliers = df.groupby("SUPPLIER")["TOTAL SALES"].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_suppliers.values, y=top_suppliers.index)
plt.title("Top 10 Suppliers by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Supplier")
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df[["RETAIL SALES","RETAIL TRANSFERS","WAREHOUSE SALES","TOTAL SALES"]].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

df = pd.get_dummies(df, columns=["SUPPLIER","ITEM TYPE"], drop_first=True)

scaler_standard = StandardScaler()
scaler_minmax = MinMaxScaler()

numeric_cols = ["RETAIL SALES","RETAIL TRANSFERS","WAREHOUSE SALES","TOTAL SALES","SALES_PER_MONTH"]

df_standard_scaled = df.copy()
df_standard_scaled[numeric_cols] = scaler_standard.fit_transform(df_standard_scaled[numeric_cols])

df_minmax_scaled = df.copy()
df_minmax_scaled[numeric_cols] = scaler_minmax.fit_transform(df_minmax_scaled[numeric_cols])

print(df.head())
print(df_standard_scaled.head())
print(df_minmax_scaled.head())
