import pandas as pd
import seaborn as sns

df = sns.load_dataset("iris")

df['petal_area'] = df['petal_length'] * df['petal_width']

df = pd.get_dummies(df, columns=['species'], drop_first=True)

print(df.head())
print(df.shape)
