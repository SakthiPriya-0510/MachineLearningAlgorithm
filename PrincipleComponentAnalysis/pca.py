import numpy as np
from sklearn.preprocessing import StandardScaler
X = np.array([
    [78, 80, 85, 82],
    [65, 68, 70, 72],
    [90, 88, 92, 91],
    [72, 70, 75, 74],
    [85, 84, 88, 86]
])
print("Original Dataset:\n", X)
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
print("\nStandardized Data:\n", X_std)
cov_matrix = np.cov(X_std.T)
print("\nCovariance Matrix:\n", cov_matrix)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print("\nEigenvalues:\n", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]
print("\nSorted Eigenvalues:\n", eigenvalues)
print("\nSorted Eigenvectors:\n", eigenvectors)

k = 2
principal_components = eigenvectors[:, :k]
print("\nPrincipal Component Matrix:\n", principal_components)
X_reduced = np.dot(X_std, principal_components)
print("\nReduced Dataset (After PCA):\n", X_reduced)
variance_ratio = eigenvalues / np.sum(eigenvalues)
print("\nVariance Percentage:\n", variance_ratio*100)
