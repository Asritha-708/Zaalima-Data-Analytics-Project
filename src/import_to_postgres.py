import pandas as pd
import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "telco_db")

encoded_password = quote_plus(DB_PASSWORD)

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Load CSV data
df = pd.read_csv(
    "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

print("CSV loaded successfully!")
print("Rows:", len(df))

# Upload data to PostgreSQL
df.to_sql(
    "telco_customers",
    engine,
    if_exists="replace",
    index=False
)

print("Data imported successfully into PostgreSQL!")