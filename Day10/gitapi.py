import requests
import pandas as pd

username = "ajay-kumar-05k4"
url = f"https://api.github.com/users/{username}"

response = requests.get(url)
data = response.json()

df = pd.DataFrame([{
    "login": data["login"],
    "name": data["name"],
    "public_repos": data["public_repos"],
    "followers": data["followers"],
    "following": data["following"]
}])

#print(df)

df.to_csv("github_user.csv", index=False)

print(df)
