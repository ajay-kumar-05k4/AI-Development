import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split

df = sns.load_dataset("iris")

df['petal_area'] = df['petal_length'] * df['petal_width']
df['sepal_area'] = df['sepal_length'] * df['sepal_width']
df['petal_ratio'] = df['petal_length'] / df['petal_width']
df['sepal_ratio'] = df['sepal_length'] / df['sepal_width']
df['total_size'] = (
    df['sepal_length'] +
    df['sepal_width'] +
    df['petal_length'] +
    df['petal_width']
)

encoder = OneHotEncoder(sparse_output=False)
species_encoded = encoder.fit_transform(df[['species']])
species_df = pd.DataFrame(species_encoded, columns=encoder.get_feature_names_out(['species']))

df = pd.concat([df.drop(columns=['species']), species_df], axis=1)

X = df.drop(columns=['species_setosa', 'species_versicolor', 'species_virginica'])
y = df[['species_setosa', 'species_versicolor', 'species_virginica']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

standard_scaler = StandardScaler()
X_train_standard = standard_scaler.fit_transform(X_train)
X_test_standard = standard_scaler.transform(X_test)

minmax_scaler = MinMaxScaler()
X_train_minmax = minmax_scaler.fit_transform(X_train)
X_test_minmax = minmax_scaler.transform(X_test)

print("Original Shape:", df.shape)
print("Training Shape:", X_train.shape)
print("Standard Scaled Sample:\n", X_train_standard[:5])
print("MinMax Scaled Sample:\n", X_train_minmax[:5])
print("One Hot Encoded Target Sample:\n", y_train.head())
