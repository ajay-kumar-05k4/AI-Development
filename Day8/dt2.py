import pandas as pd

df = pd.read_csv("netflix_titles_nov_2019.csv")

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month

df["type_encoded"] = df["type"].map({"Movie": 1, "TV Show": 0})

df["country"] = df["country"].fillna("Unknown")

print(df[["type", "type_encoded", "year_added", "month_added"]].head())
