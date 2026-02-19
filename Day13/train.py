from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Example data
X = [[1],[2],[3],[4],[5]]
y = [2,4,6,8,10]

# Split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print(predictions)
