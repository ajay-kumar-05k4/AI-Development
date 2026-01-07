import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def train_models(df):
    """
    Train machine learning models on the processed Iris dataset.
    """
    # Prepare features and target
    features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    X = df[features]
    y = df['target']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize models
    models = {
        'Random Forest': RandomForestClassifier(random_state=42),
        'SVM': SVC(random_state=42),
        'Logistic Regression': LogisticRegression(random_state=42)
    }

    # Train and evaluate models
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = {
            'accuracy': accuracy,
            'report': classification_report(y_test, y_pred, output_dict=True)
        }

    return results

if __name__ == "__main__":
    from load_iris import load_iris_data
    from feature_engineering import add_feature_engineering
    from preprocessing import preprocess_data

    data = load_iris_data()
    engineered_data = add_feature_engineering(data)
    processed_data = preprocess_data(engineered_data)
    model_results = train_models(processed_data)

    for model_name, result in model_results.items():
        print(f"{model_name} Accuracy: {result['accuracy']:.4f}")
        print(f"{model_name} Classification Report:")
        print(pd.DataFrame(result['report']).transpose())
        print("\n")
