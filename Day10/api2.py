import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

data = response.json()

df = pd.DataFrame(data)

df = df[["name", "email"]]

df.to_csv("users.csv", index=False)

print("CSV file created successfully!")
print(df.head())
