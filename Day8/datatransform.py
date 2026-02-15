import pandas as pd

df = pd.read_csv("netflix_titles_nov_2019.csv")

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

print(df.groupby("type")["title"].count())

print(df.groupby("country")["title"].count().sort_values(ascending=False))

print(df.groupby("type").agg({
    "release_year": ["min", "max"],
    "title": "count"
}))

print(df.groupby(["type","rating"])["title"].count())

print(df.groupby("year_added")["title"].count())

print(
    df.groupby("country").agg(
        total_titles=("title","count"),
        first_year=("release_year","min"),
        last_year=("release_year","max")
    )
)
