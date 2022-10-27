from typing import Optional
from DataModel import DataModel
from fastapi import FastAPI
import pandas as pd
from joblib import load,  dump
from sklearn.metrics import r2_score



app = FastAPI()

@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}


@app.post("/predict")
def make_predictions(dataModel: DataModel):
   df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
   df.columns = dataModel.columns()
   model = load("assets/modelo.joblib")
   result = model.predict(df)
   result_dict = pd.DataFrame(result).to_dict()
   return result_dict


@app.post("/r2")
def calculate_r2(df_in: str):
   df = pd.read_json(df_in)
   y_real = df["Admission Points"]
   model = load("assets/modelo.joblib")
   y_predict = model.predict(df)
   result_dict = {"R2 score": r2_score(y_real,y_predict) }
   return result_dict

