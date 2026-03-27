import streamlit as st
import requests

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

st.title("🏠 House Price Prediction")
st.write("Enter the house features below, then click **Predict**.")

# Input fields
medinc = st.number_input("Median Income (MedInc)", min_value=0.0, value=8.3252)
houseage = st.number_input("House Age", min_value=0.0, value=41.0)
averooms = st.number_input("Average Rooms", min_value=0.0, value=6.9841)
avebedrms = st.number_input("Average Bedrooms", min_value=0.0, value=1.0238)
population = st.number_input("Population", min_value=0.0, value=322.0)
aveoccup = st.number_input("Average Occupancy", min_value=0.0, value=2.5556)
latitude = st.number_input("Latitude", value=37.88, format="%.5f")
longitude = st.number_input("Longitude", value=-122.23, format="%.5f")

if st.button("Predict"):
    payload = {
        "MedInc": medinc,
        "HouseAge": houseage,
        "AveRooms": averooms,
        "AveBedrms": avebedrms,
        "Population": population,
        "AveOccup": aveoccup,
        "Latitude": latitude,
        "Longitude": longitude
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload, timeout=10)

        if response.status_code == 200:
            result = response.json()
            predicted_price = result["predicted_house_price"]
            st.success(f"Predicted House Price: {predicted_price}")
        else:
            st.error(f"API error: {response.status_code}")
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI backend. Make sure the API is running on http://127.0.0.1:8000")
    except requests.exceptions.Timeout:
        st.error("Request timed out.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")