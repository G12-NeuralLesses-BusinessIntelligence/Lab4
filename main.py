from typing import Optional
from DataModel import DataModel
from fastapi import FastAPI
import pandas as pd
import numpy as np
from joblib import load,  dump
import json

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

app = FastAPI()

@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}


@app.post("/predict")
def make_predictions(list_dataModel: list):
   dataModels = [json.loads(json.dumps(data), object_hook=lambda d: DataModel(**d)) for data in list_dataModel]
   df = pd.DataFrame(dataModels[0].dict() , columns=dataModels[0].dict().keys(), index=[0])
   for i in range(1, len(list_dataModel)):
      df = df.append(pd.DataFrame(dataModels[i].dict() , columns=dataModels[0].dict().keys(), index=[0]), ignore_index = True)
   df.columns = dataModels[0].columns()
   model = load("assets/modelo.joblib")
   result = model.predict(df)

   return {"results": pd.DataFrame(result).to_dict()}


@app.post("/retraining")
def retraining(data_in: str):

   print("\n\n\n---------------------------------------------------------------------------------------------------------\n\n\n")
   # Extraction of the data
   df = pd.read_json(data_in, )
   var_obj = df["var_obj"][0]
   df.drop("var_obj", inplace=True, axis=1)

   ## Definition of trining features
   features = list(df.columns)
   features.remove(var_obj)
   features.remove("Serial No.")

   ## Definition of the pipeline
   pipeline2export = Pipeline(
      [
         ('feature_selection', ColumnTransformer(
               [
                  ('selector', 'passthrough', features)
               ]
         )),
         ('scaler', StandardScaler()),
         ('model', LinearRegression())
      ]
   )
   # Reentrenamiento del modelo
   y_train = pd.Series(df[var_obj])
   X_train = df.drop([var_obj], axis=1)
   pipeline2export.fit(X_train, y_train)
   dump(pipeline2export, 'assets/modelo.joblib')   # Se guarda

   #Predicción para las metricas
   y_predict = pipeline2export.predict(X_train)
   result_dict = {"#Samples":len(y_train),
                  "Current var objective":var_obj,
                  "RMSE":round(mean_squared_error(y_train,y_predict),3),
                  "MAE":round(mean_absolute_error(y_train,y_predict),3),
                  "R2 score": round(r2_score(y_train,y_predict),3),
                   }
   return result_dict

