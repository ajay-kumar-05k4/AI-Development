import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X = np.array([[1, 2], [2, 3], [3, 4], [8, 9], [9, 10], [10, 11]])

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

labels = kmeans.labels_

print("Cluster Labels:", labels)

plt.scatter(X[:,0], X[:,1], c=labels)
plt.show()
