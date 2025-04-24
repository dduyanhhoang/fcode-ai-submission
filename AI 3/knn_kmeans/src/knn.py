import numpy as np
from collections import Counter

class KNNClassifier:
    def __init__(self, K):
        self.K = K
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def _compute_distance(self, x1, x2):
        distance = np.sqrt(np.sum((x1 - x2) ** 2))
        return distance

    def predict(self, X):

        predictions = []
        for i, x_test in enumerate(X):
            distances = np.array([self._compute_distance(x_test, x_train) for x_train in self.X_train])
            neighbor_indices = np.argsort(distances)[:self.K]
            neighbor_labels = self.y_train[neighbor_indices]
            most_common = Counter(neighbor_labels).most_common(1)[0][0]
            predictions.append(most_common)
        return np.array(predictions)
