import pandas as pd

df = pd.read_csv("netflix_titles_nov_2019.csv")

df = df.drop_duplicates()
print(df.isnull().sum())
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
df["duration"] = df["duration"].fillna("Unknown")
print(df.isnull().sum())
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["title"] = df["title"].str.strip()
df["director"] = df["director"].str.strip()
df["cast"] = df["cast"].str.strip()
df["country"] = df["country"].str.strip()
df["listed_in"] = df["listed_in"].str.strip()
df.to_csv("netflix_titles_cleaned.csv", index=False)

print(df.isnull().sum())
print(df.head())

