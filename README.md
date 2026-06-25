# 🏠 House Price Prediction — ML Deployment

An end-to-end machine learning application that predicts California house prices using a trained Random Forest regression model, served via FastAPI with a Streamlit frontend.

---

## 📌 Project Overview

Users enter housing features (income, age, rooms, population, location) and receive a predicted house price. Built to demonstrate a complete ML deployment workflow:

1. Train a regression model (scikit-learn)
2. Save the model with Joblib
3. Expose it via a FastAPI REST endpoint
4. Build a Streamlit frontend
5. Containerize the backend with Docker

---

## 🛠️ Tech Stack

- **Python** — scikit-learn, pandas, Joblib
- **FastAPI** + **Uvicorn** — REST API backend
- **Pydantic** — request validation
- **Streamlit** — interactive frontend
- **Docker** — containerized backend deployment

---

## 📂 Project Structure

```
ml-house-price-deployment/
├── app/
│   ├── main.py           # FastAPI app and /predict endpoint
│   ├── model_loader.py   # Model loading logic
│   └── schema.py         # Pydantic request schema
├── frontend/
│   └── streamlit_app.py  # Streamlit UI
├── model/
│   └── train_model.py    # Model training script
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🔄 How It Works

```
User → Streamlit Frontend → FastAPI Backend → ML Model → Prediction Response
```

### API Endpoint

**POST** `/predict`

Example input:
```json
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
```

Example response:
```json
{
  "predicted_house_price": 4.4441
}
```

---

## ▶️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/issa89ai/ml-house-price-deployment.git
cd ml-house-price-deployment

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train the model
python model/train_model.py

# 5. Run the backend
python -m uvicorn app.main:app --reload
# → http://127.0.0.1:8000/docs

# 6. Run the frontend (new terminal)
python -m streamlit run frontend/streamlit_app.py
# → http://localhost:8501
```

---

## 🐳 Run with Docker

```bash
docker build -t housing-api .
docker run -p 8000:8000 housing-api
# → http://localhost:8000/docs
```

---

## 💡 Future Improvements

- Deploy to cloud (Render, Railway)
- Add Docker Compose for full stack
- Add model evaluation metrics to the UI
- Replace dataset with a business-focused use case

---

## 👤 Author

**Ahmad Issa**  
Machine Learning Engineer | AI & Data Science  
[GitHub](https://github.com/issa89ai) · [LinkedIn](https://linkedin.com/in/ahmadissa)
