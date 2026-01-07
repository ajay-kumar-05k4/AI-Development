from sklearn.datasets import load_iris
import pandas as pd

def load_iris_data():
    """
    Load the Iris dataset from sklearn and return as a pandas DataFrame.
    """
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df['target_names'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    return df

if __name__ == "__main__":
    data = load_iris_data()
    print(data.head())
    print(data.info())
