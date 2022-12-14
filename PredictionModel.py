from joblib import load
import pandas as pd

class Model:

    def __init__(self,columns):
        self.model = load("assets/modelo.joblib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        result = pd.DataFrame(result)
        return result
