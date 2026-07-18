import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("===================================")
print("TELCO CUSTOMER CHURN DATASET")
print("===================================")

print("\nDataset loaded successfully!")

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())