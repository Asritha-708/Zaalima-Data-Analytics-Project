from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd
import joblib

# Create FastAPI application
app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn",
    version="1.0"
)

# Load trained model
model = joblib.load("models/best_model.pkl")


# Input Schema
class Customer(BaseModel):
    gender: int
    SeniorCitizen: int
    tenure: int
    MonthlyCharges: float
    TotalCharges: float

    Partner_Yes: bool
    Dependents_Yes: bool
    PhoneService_Yes: bool

    MultipleLines_No_phone_service: bool
    MultipleLines_Yes: bool

    InternetService_Fiber_optic: bool
    InternetService_No: bool

    OnlineSecurity_No_internet_service: bool
    OnlineSecurity_Yes: bool

    OnlineBackup_No_internet_service: bool
    OnlineBackup_Yes: bool

    DeviceProtection_No_internet_service: bool
    DeviceProtection_Yes: bool

    TechSupport_No_internet_service: bool
    TechSupport_Yes: bool

    StreamingTV_No_internet_service: bool
    StreamingTV_Yes: bool

    StreamingMovies_No_internet_service: bool
    StreamingMovies_Yes: bool

    Contract_One_year: bool
    Contract_Two_year: bool

    PaperlessBilling_Yes: bool

    PaymentMethod_Credit_card_automatic: bool
    PaymentMethod_Electronic_check: bool
    PaymentMethod_Mailed_check: bool


# Single Customer Prediction
@app.post("/predict")
def predict(customer: Customer):

    data = pd.DataFrame([customer.model_dump()])

    data.columns = model.feature_names_in_

    prediction = model.predict(data)

    result = "Churn" if prediction[0] == 1 else "No Churn"

    return {
        "Prediction": result
    }


# Batch Prediction
@app.post("/predict_batch")
def predict_batch(customers: List[Customer]):

    data = pd.DataFrame([customer.model_dump() for customer in customers])

    data.columns = model.feature_names_in_

    predictions = model.predict(data)

    results = [
        "Churn" if pred == 1 else "No Churn"
        for pred in predictions
    ]

    return {
        "Predictions": results
    }


# Home Page
@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is Running Successfully!"
    }
