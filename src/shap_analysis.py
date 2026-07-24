import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

print("Step 1")

df = pd.read_csv("data/cleaned/telco_cleaned.csv")
print("Step 2")

X = df.drop("Churn", axis=1)
y = df["Churn"]

print("Step 3")
X = pd.get_dummies(X)

# Use only 300 samples to make SHAP faster
X_sample = X.sample(300, random_state=42)

print("Step 4")
model = RandomForestClassifier(random_state=42)
model.fit(X_sample, y.loc[X_sample.index])

print("Step 5")
explainer = shap.TreeExplainer(model)

print("Step 6")
shap_values = explainer.shap_values(X_sample)

print("Step 7")
shap.summary_plot(shap_values[1], X_sample)

print("Finished")