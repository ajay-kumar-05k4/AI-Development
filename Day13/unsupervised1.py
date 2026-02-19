from sklearn.decomposition import PCA
import numpy as np

X = np.array([[2,3],[3,4],[5,6],[7,8]])

pca = PCA(n_components=1)
X_reduced = pca.fit_transform(X)

print("Reduced Data:\n", X_reduced)
