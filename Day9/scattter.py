import matplotlib.pyplot as plt
x = [5, 7, 8, 7, 2, 17, 2]
y = [99, 86, 87, 88, 100, 86, 103]

plt.scatter(x, y, color='red', marker='x')
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
