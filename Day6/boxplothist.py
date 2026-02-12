import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=50, scale=10, size=200)

# Histogram
plt.figure()
plt.hist(data, bins=15)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# Boxplot
plt.figure()
plt.boxplot(data)
plt.title("Boxplot")
plt.show()
