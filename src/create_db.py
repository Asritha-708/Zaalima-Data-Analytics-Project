import pandas as pd
import sqlite3
from pathlib import Path

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# CSV file path
csv_path = BASE_DIR / "data" / "raw" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

# SQLite database path
db_path = BASE_DIR / "data" / "telco.db"

# Read CSV
df = pd.read_csv(csv_path)

# Create SQLite database
conn = sqlite3.connect(db_path)

# Save CSV as SQL table
df.to_sql(
    "telco_churn",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created successfully!")