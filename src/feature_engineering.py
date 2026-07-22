import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Original Shape:", df.shape)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Fill missing values
df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)

# Encode Churn
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# Encode Gender
df["gender"] = df["gender"].map({"Male": 1, "Female": 0})

print("\nMissing Values:")
print(df.isnull().sum())

print("\nEncoded Columns:")
print(df[["gender", "Churn"]].head())

# Save processed dataset
df.to_csv("data/cleaned/telco_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")