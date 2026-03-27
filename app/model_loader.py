import joblib

MODEL_PATH = "model/house_price_model.pkl"

def load_model():
    model = joblib.load(MODEL_PATH)
    return model