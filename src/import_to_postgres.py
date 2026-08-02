import pandas as pd
from sqlalchemy import create_engine

# Load the dataset
df = pd.read_csv(
    r"C:\Users\buddh\Documents\Zaalima-Data-Analytics-Project\data\raw\WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# Connect to PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://postgres:Ashritha@02@localhost:5432/telco_db"
)

# Upload data
df.to_sql(
    "telco_customers",
    engine,
    if_exists="replace",
    index=False
)

print("Data imported successfully into PostgreSQL!")