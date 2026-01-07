import pandas as pd
import numpy as np

def add_feature_engineering(df):
    """
    Add feature engineering techniques to the Iris dataset.
    """
    # Create new features
    df['sepal_area'] = df['sepal length (cm)'] * df['sepal width (cm)']
    df['petal_area'] = df['petal length (cm)'] * df['petal width (cm)']
    df['sepal_petal_ratio'] = df['sepal length (cm)'] / df['petal length (cm)']

    # Polynomial features (simple example)
    df['sepal_length_squared'] = df['sepal length (cm)'] ** 2
    df['petal_length_squared'] = df['petal length (cm)'] ** 2

    return df

if __name__ == "__main__":
    from load_iris import load_iris_data
    data = load_iris_data()
    engineered_data = add_feature_engineering(data)
    print(engineered_data.head())
    print("New features added:", [col for col in engineered_data.columns if col not in data.columns])
