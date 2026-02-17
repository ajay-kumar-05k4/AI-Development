import requests
import pandas as pd

username = "ajay-kumar-05k4"
url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)
repos = response.json()

df = pd.DataFrame(repos)

df = df[["name", "language", "stargazers_count"]]

df.to_csv("github_repos.csv", index=False)

print(df.head())
