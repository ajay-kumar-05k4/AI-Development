import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

def load_iris_data():
    """
    Load the Iris dataset.
    """
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return df

def train_knn_model(df, k=3):
    """
    Train KNN model on the Iris dataset.
    """
    # Prepare features and target
    features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    X = df[features]
    y = df['target']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize and train KNN model
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    # Make predictions
    y_pred = knn.predict(X_test)

    return y_test, y_pred

def evaluate_model(y_test, y_pred):
    """
    Evaluate the model performance.
    """
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    # Load data
    data = load_iris_data()
    print("Iris dataset loaded successfully.")
    print(f"Dataset shape: {data.shape}")
    print(data.head())

    # Train model and evaluate
    y_test, y_pred = train_knn_model(data, k=3)
    print("\nEvaluating KNN model with k=3:")
    evaluate_model(y_test, y_pred)
