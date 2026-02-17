import pandas as pd

data = {
    "id": [1,2,3],
    "name": ["Ajai", "Ravi", "Sita"],
    "marks": [85, 90, 78]
}

df = pd.DataFrame(data)
df.to_csv("new_students.csv", index=False)
