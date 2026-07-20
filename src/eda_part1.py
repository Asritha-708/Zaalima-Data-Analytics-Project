import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("="*50)
print("EXPLORATORY DATA ANALYSIS - PART 1")
print("="*50)

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Basic statistics
print("\nNumerical Statistics:")
print(df.describe())

# Categorical statistics
print("\nCategorical Statistics:")
print(df.describe(include='object'))