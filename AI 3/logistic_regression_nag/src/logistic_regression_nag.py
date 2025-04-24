import numpy as np
import pandas as pd


class LogisticRegressionNAG:
    def __init__(self, learning_rate=0.01, momentum=0.9, n_iters=1000, class_weight=None):
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.n_iters = n_iters
        self.class_weight = class_weight  # Dictionary of class weights
        self.weights = None
        self.bias = None
        self.velocity_w = None
        self.velocity_b = None
        self.loss_history = []

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        self.velocity_w = np.zeros(n_features)
        self.velocity_b = 0

        if isinstance(y, pd.Series):
            y = y.values

        if self.class_weight is not None:
            sample_weights = np.array([self.class_weight[label] for label in y])
        else:
            sample_weights = np.ones(n_samples)

        for _ in range(self.n_iters):
            lookahead_weights = self.weights + self.momentum * self.velocity_w
            lookahead_bias = self.bias + self.momentum * self.velocity_b

            linear_model = np.dot(X, lookahead_weights) + lookahead_bias
            y_predicted = self._sigmoid(linear_model)

            error = y_predicted - y
            dw = (1 / n_samples) * np.dot(X.T, sample_weights * error)
            db = (1 / n_samples) * np.sum(sample_weights * error)

            self.velocity_w = self.momentum * self.velocity_w - self.learning_rate * dw
            self.velocity_b = self.momentum * self.velocity_b - self.learning_rate * db

            self.weights += self.velocity_w
            self.bias += self.velocity_b

            loss = (-1 / n_samples) * np.sum(
                sample_weights * (
                        y * np.log(y_predicted + 1e-15) +
                        (1 - y) * np.log(1 - y_predicted + 1e-15)
                )
            )
            self.loss_history.append(loss)

    def predict_proba(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        return self._sigmoid(linear_model)

    def predict(self, X, threshold=0.5):
        y_pred_proba = self.predict_proba(X)
        return (y_pred_proba >= threshold).astype(int)
