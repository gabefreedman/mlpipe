from sklearn.neighbors import KNeighborsClassifier
import numpy as np

from mlpipe import Model


class KNNModel(Model):

    name = "KNNModel"

    def __init__(self):
        Model.__init__(self)
        
    def setup(self, device):
        self.knn = KNeighborsClassifier(n_neighbors=7)

    def train(self, data, labels, metadata):
        corrLive = metadata['corrLive'][:,None]
        rmsLive = metadata['rmsLive'][:,None]
        kurtLive = metadata['kurtLive'][:,None]
        skewLive = metadata['skewLive'][:,None]
        normLive = metadata['normLive'][:,None]
        features = np.hstack([corrLive, rmsLive, kurtLive, skewLive, normLive])

        self.knn.fit(features, labels)
        prediction = self.knn.predict(features)
        return prediction
    
    def test(self, data, labels, metadata):
        pass