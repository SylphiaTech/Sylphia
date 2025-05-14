from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyModel:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)

    def fit(self, X):
        self.model.fit(X)

    def predict(self, X):
        return self.model.predict(X)