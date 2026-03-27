import os
import joblib
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = fetch_california_housing(as_frame=True)
X = data.data
y = data.target

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Ensure model directory exists
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, "model/house_price_model.pkl")

print("Model trained and saved successfully.")