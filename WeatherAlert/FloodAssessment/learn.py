import pickle
import numpy as np


class MachineLearning:
    def __init__(self):
        self.api_data = np.array([[28.7, 44.7, 51.6, 160, 174.7, 824.6, 743, 357.5, 197.7, 266.9, 350.8, 48.4, 3248.6]])
        self.api_data.reshape(-1, 1)
        self.filename = "finalized_model.sav"
        self.loaded_model = pickle.load(open(self.filename, 'rb'))

    def predict(self):
        
        return self.loaded_model.predict(self.api_data)
        
