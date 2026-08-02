import pandas as pd
import sqlite3

# Read CSV
df = pd.read_csv(
    r"C:\Users\buddh\Documents\Zaalima-Data-Analytics-Project\data\raw\WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# Create SQLite database
conn = sqlite3.connect(
    r"C:\Users\buddh\Documents\Zaalima-Data-Analytics-Project\data\telco.db"
)

# Save CSV as SQL table
df.to_sql("telco_churn", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully!")