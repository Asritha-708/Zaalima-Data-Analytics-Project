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


# Exact feature order used while training the model
FEATURE_COLUMNS = [
    "gender",
    "SeniorCitizen",
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "AvgMonthlySpend",
    "IsLongTerm",

    "Partner_Yes",
    "Dependents_Yes",
    "PhoneService_Yes",

    "MultipleLines_No phone service",
    "MultipleLines_Yes",

    "InternetService_Fiber optic",
    "InternetService_No",

    "OnlineSecurity_No internet service",
    "OnlineSecurity_Yes",

    "OnlineBackup_No internet service",
    "OnlineBackup_Yes",

    "DeviceProtection_No internet service",
    "DeviceProtection_Yes",

    "TechSupport_No internet service",
    "TechSupport_Yes",

    "StreamingTV_No internet service",
    "StreamingTV_Yes",

    "StreamingMovies_No internet service",
    "StreamingMovies_Yes",

    "Contract_One year",
    "Contract_Two year",

    "PaperlessBilling_Yes",

    "PaymentMethod_Credit card (automatic)",
    "PaymentMethod_Electronic check",
    "PaymentMethod_Mailed check"
]


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


def prepare_data(customer):

    data = pd.DataFrame([customer.model_dump()])

    # Rename API field names to match training column names
    data = data.rename(columns={
        "MultipleLines_No_phone_service":
            "MultipleLines_No phone service",

        "InternetService_Fiber_optic":
            "InternetService_Fiber optic",

        "OnlineSecurity_No_internet_service":
            "OnlineSecurity_No internet service",

        "OnlineBackup_No_internet_service":
            "OnlineBackup_No internet service",

        "DeviceProtection_No_internet_service":
            "DeviceProtection_No internet service",

        "TechSupport_No_internet_service":
            "TechSupport_No internet service",

        "StreamingTV_No_internet_service":
            "StreamingTV_No internet service",

        "StreamingMovies_No_internet_service":
            "StreamingMovies_No internet service",

        "PaymentMethod_Credit_card_automatic":
            "PaymentMethod_Credit card (automatic)",

        "PaymentMethod_Mailed_check":
            "PaymentMethod_Mailed check"
    })

    # Create the same features used during model training
    data["AvgMonthlySpend"] = (
        data["TotalCharges"] /
        (data["tenure"] + 1)
    )

    data["IsLongTerm"] = (
        data["tenure"] > 24
    ).astype(int)

    # Make sure all expected columns exist
    for column in FEATURE_COLUMNS:
        if column not in data.columns:
            data[column] = False

    # Keep exactly the same feature order used during training
    data = data[FEATURE_COLUMNS]

    return data


# Single Customer Prediction
@app.post("/predict")
def predict(customer: Customer):

    data = prepare_data(customer)

    prediction = model.predict(data)

    result = "Churn" if prediction[0] == 1 else "No Churn"

    return {
        "Prediction": result
    }


# Batch Prediction
@app.post("/predict_batch")
def predict_batch(customers: List[Customer]):

    data_list = []

    for customer in customers:
        data_list.append(prepare_data(customer))

    data = pd.concat(data_list, ignore_index=True)

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
        "message":
        "Customer Churn Prediction API is Running Successfully!"
    }