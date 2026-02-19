from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = [[2], [4], [6], [8], [10]]
y = [0, 0, 0, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Actual:", y_test)
print("Predicted:", prediction)
