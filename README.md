# House Price Prediction API

An end-to-end machine learning application that predicts house prices using a trained Random Forest regression model.  
The project includes:

- a **FastAPI backend**
- a **Streamlit frontend**
- **Docker** support for containerized deployment

This project demonstrates how to move from a trained machine learning model to a usable application with an API and user interface.

---

## Project Overview

This application allows a user to enter housing-related features such as income, house age, rooms, population, and location, then receive a predicted house price.

The project was built to demonstrate a complete machine learning workflow:

1. Train a regression model
2. Save the trained model
3. Expose the model through a FastAPI endpoint
4. Build a frontend using Streamlit
5. Containerize the backend with Docker

---

## Tech Stack

- **Python**
- **scikit-learn**
- **pandas**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **Streamlit**
- **Requests**
- **Docker**
- **Joblib**

---

## Project Structure

```bash
housing_ml_deployment/
│
├── app/
│   ├── main.py
│   ├── model_loader.py
│   └── schema.py
│
├── frontend/
│   └── streamlit_app.py
│
├── model/
│   └── train_model.py
│
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
How It Works
Backend

The FastAPI backend loads a trained machine learning model and exposes a /predict endpoint.

Frontend

The Streamlit frontend provides a simple interface where users can enter feature values and request a prediction.

Prediction Flow
User → Streamlit Frontend → FastAPI Backend → ML Model → Prediction Response
API Endpoint
POST /predict

Accepts house feature values and returns the predicted house price.

Example input
{
  "MedInc": 8.3252,
  "HouseAge": 41.0,
  "AveRooms": 6.9841,
  "AveBedrms": 1.0238,
  "Population": 322.0,
  "AveOccup": 2.5556,
  "Latitude": 37.88,
  "Longitude": -122.23
}
Example response
{
  "predicted_house_price": 4.4441
}
Run the Project Locally
1. Clone the repository
git clone https://github.com/issa89ai/ml-house-price-deployment.git
cd ml-house-price-deployment
2. Create and activate a virtual environment
Windows
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Train the model

Since the trained model file is not included in the repository, generate it locally by running:

python model/train_model.py

This will create:

model/house_price_model.pkl
5. Run the FastAPI backend
python -m uvicorn app.main:app --reload

Backend URL:

http://127.0.0.1:8000

Swagger docs:

http://127.0.0.1:8000/docs
6. Run the Streamlit frontend

Open a new terminal, activate the virtual environment again, then run:

python -m streamlit run frontend/streamlit_app.py

Frontend URL:

http://localhost:8501
Run the Backend with Docker
1. Build the Docker image
docker build -t housing-api .
2. Run the Docker container
docker run -p 8000:8000 housing-api

Then open:

http://localhost:8000/docs
Key Features
Trained a Random Forest Regressor on housing data
Saved and loaded the model using Joblib
Built a prediction API with FastAPI
Validated request data using Pydantic
Built an interactive frontend with Streamlit
Containerized the backend using Docker
Learning Goals of This Project

This project was built to practice and demonstrate:

machine learning model serving
API development
frontend-backend integration
containerized deployment
reproducible project structure
Future Improvements

Possible next upgrades:

deploy the application to the cloud
dockerize both backend and frontend together
add Docker Compose
replace the dataset with a more business-focused use case such as insurance risk or customer churn
add model evaluation metrics to the interface
Author

Ahmad
Master’s in Computer Science
Focus: Data Science / Machine Learning / Applied AI