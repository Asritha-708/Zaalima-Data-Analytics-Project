# 📊 Customer Churn Prediction & Customer Lifetime Value Analytics

An end-to-end machine learning and data analytics project for predicting customer churn, estimating Customer Lifetime Value (LTV), explaining model predictions using SHAP, storing customer data in PostgreSQL, and visualizing business insights through Power BI.



## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Objectives](#-objectives)
- [Key Features](#-key-features)
- [Dataset](#-dataset)
- [Dataset Features](#-dataset-features)
- [Project Workflow](#-project-workflow)
- [Project Architecture](#-project-architecture)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Data Preprocessing](#-data-preprocessing)
- [Exploratory Data Analysis](#-exploratory-data-analysis)
- [Feature Engineering](#-feature-engineering)
- [Machine Learning Models](#-machine-learning-models)
- [Model Evaluation](#-model-evaluation)
- [Best Performing Model](#-best-performing-model)
- [SHAP Explainability](#-shap-explainability)
- [Customer Lifetime Value](#-customer-lifetime-value)
- [PostgreSQL Database](#-postgresql-database)
- [Power BI Dashboard](#-power-bi-dashboard)
- [FastAPI Application](#-fastapi-application)
- [Installation](#-installation)
- [Running the Project](#-running-the-project)
- [API Endpoints](#-api-endpoints)
- [Reports and Visualizations](#-reports-and-visualizations)
- [Business Insights](#-business-insights)
- [Business Impact](#-business-impact)
- [Future Enhancements](#-future-enhancements)
- [Limitations](#-limitations)
- [Contributors](#-contributors)
- [License](#-license)
- [Conclusion](#-conclusion)

---

# 📌 Project Overview

Customer churn is a major challenge for telecommunication companies because losing existing customers can directly affect revenue and business growth.

This project develops an end-to-end **Customer Churn Prediction and Customer Lifetime Value Analytics system** using machine learning and data analytics techniques.

The system analyzes customer information such as:

- Customer demographics
- Contract type
- Tenure
- Internet services
- Payment methods
- Monthly charges
- Total charges
- Customer service usage

Machine learning models are used to predict whether a customer is likely to churn.

The project also estimates Customer Lifetime Value (LTV), uses SHAP for model explainability, stores customer data in PostgreSQL, and provides an interactive Power BI dashboard for business analysis.

---

# 🎯 Problem Statement

Telecommunication companies collect large amounts of customer data, but identifying customers who are likely to leave can be difficult.

Traditional analysis may show what happened in the past, but machine learning can help predict potential churn based on customer characteristics.

The problem addressed by this project is:

> **How can customer data be analyzed using machine learning to predict customer churn, estimate customer value, understand the factors influencing churn, and support better customer retention decisions?**

---

# 🎯 Objectives

The main objectives of the project are:

1. Predict whether a customer is likely to churn.
2. Identify the important factors influencing customer churn.
3. Compare multiple machine learning algorithms.
4. Select the best-performing churn prediction model.
5. Explain model predictions using SHAP.
6. Estimate Customer Lifetime Value (LTV).
7. Store customer information in PostgreSQL.
8. Build an interactive Power BI dashboard.
9. Provide a FastAPI-based prediction service.
10. Support data-driven customer retention strategies.

---

# ⭐ Key Features

### 🔹 Customer Churn Prediction

Predicts whether a customer is likely to leave the telecom company.

### 🔹 Multiple Machine Learning Models

The project compares:

- Logistic Regression
- Random Forest
- XGBoost

### 🔹 Explainable AI

SHAP is used to understand which features influence churn predictions.

### 🔹 Customer Lifetime Value

Estimates the potential long-term value of customers.

### 🔹 PostgreSQL Integration

Customer data can be imported into PostgreSQL for structured storage and analysis.

### 🔹 Power BI Dashboard

Provides interactive business visualizations and KPI metrics.

### 🔹 FastAPI Prediction API

Provides REST API endpoints for customer churn prediction.

---

# 📊 Dataset

The project uses the **Telco Customer Churn Dataset**.

The dataset contains customer information collected from a telecommunications company.

The dataset contains approximately:

- **7,043 customers**
- **21 original features**

The target variable is:

```text
Churn
where :
Yes = Customer churned
No  = Customer did not churn

#project workflow
                Raw Customer Dataset
                        │
                        ▼
                Data Cleaning
                        │
                        ▼
             Exploratory Data Analysis
                        │
                        ▼
              Feature Engineering
                        │
                        ▼
              Data Preprocessing
                        │
                        ▼
                Train/Test Split
                        │
                        ▼
             Machine Learning Models
              ┌─────────┼─────────┐
              ▼         ▼         ▼
          Logistic   Random     XGBoost
         Regression  Forest
              └─────────┼─────────┘
                        ▼
                Model Evaluation
                        │
                        ▼
                 Best Model
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
       SHAP Explainability       LTV
             │                     │
             └──────────┬──────────┘
                        ▼
                 PostgreSQL
                        │
                        ▼
                  Power BI
                        │
                        ▼
                  FastAPI API

#project Architecture

Data Source
    ↓
Data Cleaning
    ↓
EDA
    ↓
Feature Engineering
    ↓
Machine Learning
    ↓
Model Evaluation
    ↓
Explainable AI
    ↓
PostgreSQL
    ↓
Power BI
    ↓
FastAPI

#Technologies used
1.Programming Language
Python
2.Data Analysis
Pandas
NumPy
3.Data Visualization
Matplotlib
Seaborn
Power BI
4.Machine Learning
Scikit-learn
XGBoost
5.Explainable AI
SHAP
6.Database
PostgreSQL
SQLAlchemy
Psycopg2
7.API
FastAPI
Uvicorn
Pydantic
8.Model Saving
Joblib
9.Development Tools
Visual Studio Code
Jupyter Notebook
Git
GitHub


#project structure
Zaalima-Data-Analytics-Project/
│
├── app.py
├── Dockerfile
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   │
│   └── cleaned/
│       ├── cleaned_telco.csv
│       └── encoded_telco.csv
│
├── docs/
│   ├── dashboard_setup.md
│   ├── project_plan.md
│   └── shap_analysis.md
│
├── models/
│   ├── README.md
│   ├── best_model.pkl
│   └── ltv_model.pkl
│
├── notebooks/
│   ├── 02_eda_visualization.ipynb
│   └── customer_churn_prediction.ipynb
│
├── reports/
│   ├── churn_distribution.png
│   ├── contract_vs_churn.png
│   ├── correlation_heatmap.png
│   ├── customer churn dashboard.pbix
│   ├── gender_vs_churn.png
│   ├── internet_vs_churn.png
│   ├── logistic_regression.png
│   ├── logistic_regression_confusion_matrix.png
│   ├── model_comparison.csv
│   ├── monthly_charges.png
│   ├── project_architecture.png
│   ├── random_forest_confusion_matrix.png
│   ├── shap_summary.png
│   └── xgboost.png
│
└── src/
    ├── data_cleaning.py
    ├── data_summary.py
    ├── eda_part1.py
    ├── eda_part2.py
    ├── feature_engineering.py
    ├── import_to_postgres.py
    ├── load_data.py
    └── shap_analysis.py


#Exploratry Data Analysis

Exploratory Data Analysis (EDA) is performed to understand customer behavior and identify patterns related to churn.

The analysis includes:

Churn distribution
Contract vs churn
Gender vs churn
Internet service vs churn
Monthly charges analysis
Correlation analysis

These visualizations help identify patterns that may contribute to customer churn.

#Feature Engineering

Feature engineering is used to create useful information from existing customer data.

Examples include:

Average Monthly Spend

Helps understand customer spending behavior.

Long-Term Customer Indicator

Identifies customers with longer relationships with the company.

Customer Lifetime Value

Combines customer financial and tenure information to estimate customer value.

Feature engineering helps convert raw customer information into meaningful features for machine learning and business analysis.

#Machinelearning Models

Three machine learning classification algorithms are used.

1. Logistic Regression

Logistic Regression is used as a baseline classification algorithm.

It predicts the probability that a customer belongs to the churn class.

Advantages:

Simple
Fast
Easy to interpret
Good baseline model
2. Random Forest

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees.

Advantages:

Handles nonlinear relationships
Works with many features
Provides feature importance
More robust than a single decision tree
3. XGBoost

XGBoost is a gradient boosting algorithm that builds trees sequentially to improve prediction performance.

Advantages:

Powerful classification algorithm
Handles complex relationships
Good performance on structured data
Supports feature importance

#Model evaluation

The models are evaluated using:

Accuracy
Precision
Recall
F1 Score

# Model Performance
Model	|Accuracy	|Precision	|Recall   |F1 Score
Logistic Regression   |	80.91%	|68.31%|	52.01%|	59.06%
Random Forest      |	79.56%	|66.04%	|46.92%	|54.86%
XGBoost	     |78.85%|	62.38%|	50.67%|	55.92%
Interpretation

Based on the current evaluation:

Logistic Regression achieved the highest accuracy.
Logistic Regression also achieved the highest F1 score.
Random Forest performed second in accuracy.
XGBoost provided competitive recall but lower overall accuracy.


#Best performing Model

The current best-performing model is:
Logistic Regression

Performance:

Metric	                  Score
Accuracy               	80.91%
Precision	            68.31%
Recall	                52.01%
F1 Score            	59.06%

Therefore, Logistic Regression is selected as the best-performing churn prediction model among the tested models.

#confusion Matrix
Confusion matrices are used to understand the classification results.

They show:

True Positives
True Negatives
False Positives
False Negatives

The project contains confusion matrix visualizations for the machine learning models.

#SHAP Analysis

SHAP is used to explain the machine learning predictions.

Instead of only predicting whether a customer will churn, SHAP helps us understand why the model made that prediction.

It helps identify the features that have the greatest influence on customer churn.

The SHAP results are available in the reports/ folder.

# Customer Lifetime Value

Customer Lifetime Value (LTV) represents the estimated value a customer can provide to the company during their relationship.

LTV analysis helps identify:

Valuable customers.
Long-term customers.
Customers who may need special retention strategies.

The LTV model is stored in the models/ folder.

##PostgreSQL Database

PostgreSQL is used to store the customer data in a structured database.

The data import script is:

src/import_to_postgres.py

The customer data is imported into the:

telco_customers

table.

To import the data:

python src/import_to_postgres.py
 ## Power BI Dashboard

An interactive Power BI dashboard was created to understand customer churn.

The dashboard includes:

Total Customers.
Churn Customers.
Active Customers.
Churn Rate.
Average Monthly Charges.
Churn by Contract.
Churn by Gender.
Churn by Internet Service.
Dashboard File
reports/customer churn dashboard.pbix

The .pbix file should be opened using Microsoft Power BI Desktop.

## Dashboard Preview

Add your final dashboard screenshot here.

Example:

![Customer Churn Dashboard](reports/dashboard_screenshot.png)
## FastAPI

FastAPI is used to provide a simple API for customer churn prediction.

The main application file is:

app.py

Run the API using:

uvicorn app:app --reload

Then open:

http://127.0.0.1:8000

Swagger API documentation:

http://127.0.0.1:8000/docs

## Main API Endpoints
Method	Endpoint	Purpose
GET	/	Check API status
POST	/predict	Predict churn for one customer
POST	/predict_batch	Predict churn for multiple customers
 ##How to Run the Project
1. Clone the Repository
git clone https://github.com/Asritha-708/Zaalima-Data-Analytics-Project.git
2. Open the Project
cd Zaalima-Data-Analytics-Project
3. Install Required Packages
pip install -r requirements.txt
4. Run the Data Processing Scripts

Example:

python src/data_cleaning.py
python src/feature_engineering.py
5. Run the FastAPI Application
uvicorn app:app --reload
#Key Business Insights

The project helps businesses understand which types of customers are more likely to churn.

The analysis can be used to:

Identify high-risk customers.
Understand customer behavior.
Improve customer retention.
Identify valuable customers.
Create targeted offers.
Reduce potential revenue loss.
## Future Enhancements

Future improvements can include:

Hyperparameter tuning.
Improving churn recall.
Real-time churn prediction.
Cloud deployment.
Automatic model retraining.
Customer segmentation.
Real-time dashboard updates.
Automated alerts for high-risk customers.

# Limitations
The model is trained using the available Telco customer dataset.
Predictions are not guaranteed to be correct for every customer.
Model performance may change with new data.
LTV is an estimated value.
Further model tuning could improve performance.

# Conclusion

This project provides an end-to-end solution for customer churn analysis.

It combines data analytics, machine learning, SHAP explainability, Customer Lifetime Value, PostgreSQL, Power BI, and FastAPI.

The system can help businesses identify customers who are likely to churn, understand the reasons behind churn, and make better customer retention decisions.

#3 Author

Asritha Buddi

B.Tech – Computer Science and Engineering

GitHub:
https://github.com/Asritha-708

LinkedIn:
https://www.linkedin.com/in/asritha-buddhi-97616b292

## Project Repository

GitHub:

https://github.com/Asritha-708/Zaalima-Data-Analytics-Project
