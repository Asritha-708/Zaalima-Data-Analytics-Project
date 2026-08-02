import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv(
    r"C:\Users\buddh\Documents\Zaalima-Data-Analytics-Project\data\raw\WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# PostgreSQL connection

engine = create_engine(
    "postgresql+psycopg2://postgres:Ashritha%4002@localhost:5432/telco_db"
)

# Upload to PostgreSQL
df.to_sql(
    "telco_customers",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Data imported successfully into PostgreSQL!")