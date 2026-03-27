from fastapi import FastAPI
import pandas as pd

from app.schema import HouseFeatures
from app.model_loader import load_model

app = FastAPI(title="House Price Prediction API")

model = load_model()

@app.get("/")
def home():
    return {"message": "House Price Prediction API is running"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    input_data = pd.DataFrame([features.dict()])
    prediction = model.predict(input_data)[0]

    return {
        "predicted_house_price": round(float(prediction), 4)
    }