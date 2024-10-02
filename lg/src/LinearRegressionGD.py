import numpy as np


class LinearRegressionGD:
    def __init__(self, learning_rate=0.01, momentum=0.9, n_iters=1000):
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        self.velocity_w = None
        self.velocity_b = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        self.velocity_w = np.zeros(n_features)
        self.velocity_b = 0

        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias

            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            self.velocity_w = self.momentum * self.velocity_w - self.learning_rate * dw
            self.velocity_b = self.momentum * self.velocity_b - self.learning_rate * db

            self.weights += self.velocity_w
            self.bias += self.velocity_b

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias