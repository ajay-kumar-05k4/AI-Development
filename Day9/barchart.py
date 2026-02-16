import matplotlib.pyplot as plt
fruits = ['Apple', 'Banana', 'Cherry']
quantity = [10, 15, 7]

plt.bar(fruits, quantity, color='orange')
plt.title("Fruit Quantity")
plt.xlabel("Fruit")
plt.ylabel("Quantity")
plt.show()
