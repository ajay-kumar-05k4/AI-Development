import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = np.array([[500], [800], [1000], [1200], [1500]])
y = np.array([100000, 150000, 200000, 250000, 300000])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Actual:", y_test)
print("Predicted:", prediction)
