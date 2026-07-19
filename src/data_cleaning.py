import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("========== DATA CLEANING ==========")

# Dataset shape
print("\nOriginal Shape:", df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Missing values after conversion
print("\nMissing Values After Conversion:")
print(df.isnull().sum())

# Duplicate rows
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

# Remove duplicate rows
df = df.drop_duplicates()

print("\nShape After Removing Duplicates:")
print(df.shape)