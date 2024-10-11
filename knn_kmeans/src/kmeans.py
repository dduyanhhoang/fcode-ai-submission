import numpy as np

class KMeansClustering:
    def __init__(self, K, max_iters=100, tol=1e-4):
        self.K = K
        self.max_iters = max_iters
        self.tol = tol  # Tolerance for convergence
        self.centroids = None
        self.labels = None

    def fit(self, X):
        self.centroids = self._initialize_centroids(X)

        for iteration in range(self.max_iters):
            self.labels = self._assign_clusters(X)

            centroids_old = self.centroids.copy()

            self.centroids = self._calculate_centroids(X)

            centroid_shifts = np.linalg.norm(self.centroids - centroids_old, axis=1)
            if np.max(centroid_shifts) < self.tol:
                print(f"Converged at iteration {iteration}")
                break

    def _initialize_centroids(self, X):
        centroids = []
        idx = np.random.randint(X.shape[0])
        centroids.append(X[idx])

        for _ in range(1, self.K):
            distances = np.array([min(np.linalg.norm(x - c)**2 for c in centroids) for x in X])
            probabilities = distances / distances.sum()
            cumulative_probabilities = np.cumsum(probabilities)
            r = np.random.rand()

            for idx, prob in enumerate(cumulative_probabilities):
                if r < prob:
                    centroids.append(X[idx])
                    break
        return np.array(centroids)

    def _assign_clusters(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        return labels

    def _calculate_centroids(self, X):
        centroids = np.zeros((self.K, X.shape[1]))
        for k in range(self.K):
            cluster_points = X[self.labels == k]
            if len(cluster_points) > 0:
                centroids[k] = np.mean(cluster_points, axis=0)
            else:
                centroids[k] = X[np.random.randint(0, X.shape[0])]
        return centroids

    def predict(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        return labels
