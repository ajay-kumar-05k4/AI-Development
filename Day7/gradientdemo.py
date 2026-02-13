def function(x):
    return x**2

def gradient(x):
    return 2 * x

current_x = 10
learning_rate = 0.1
iterations = 10

for i in range(iterations):
    slope = gradient(current_x)
    current_x = current_x - (learning_rate * slope)
    print(f"x: {current_x:.4f} | Loss: {function(current_x):.4f}")