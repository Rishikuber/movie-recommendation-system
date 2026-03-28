"""
retrain_and_save_model.py
--------------------------
Run this script once to retrain the Customer Churn model and save it as model.pkl.
Place this file in the root of your customer-churn-ml-project repo, then run:

    python retrain_and_save_model.py

The saved model.pkl will then work with the FastAPI app (main.py).
"""

import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# ── 1. Load Data ──────────────────────────────────────────────────────────────
# Update this path if your CSV is in a different location
DATA_PATH = "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(
        f"Dataset not found at '{DATA_PATH}'.\n"
        "Download from: https://www.kaggle.com/datasets/blastchar/telco-customer-churn\n"
        "and place it in the data/ folder."
    )

df = pd.read_csv(DATA_PATH)
print(f"[✓] Loaded dataset: {df.shape[0]} rows, {df.shape[1]} columns")

# ── 2. Preprocessing ──────────────────────────────────────────────────────────
# Drop customerID (not a feature)
df.drop(columns=["customerID"], inplace=True)

# Fix TotalCharges (has spaces instead of NaN)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)

# Encode target
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# Encode all other object columns
le = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col] = le.fit_transform(df[col])

print("[✓] Preprocessing complete")

# ── 3. Train / Test Split ─────────────────────────────────────────────────────
X = df.drop(columns=["Churn"])
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ── 4. Train Model ────────────────────────────────────────────────────────────
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)
print("[✓] Model trained")

# ── 5. Evaluate ───────────────────────────────────────────────────────────────
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n[✓] Test Accuracy: {acc:.4f} ({acc*100:.2f}%)")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["No Churn", "Churn"]))

# ── 6. Save Feature Names ─────────────────────────────────────────────────────
feature_names = list(X.columns)

# ── 7. Save Model ─────────────────────────────────────────────────────────────
os.makedirs("models", exist_ok=True)

with open("models/model.pkl", "wb") as f:
    pickle.dump({"model": model, "features": feature_names}, f)

print("\n[✓] Model saved to models/model.pkl")
print(f"[✓] Features: {feature_names}")
print("\nDone! You can now run: uvicorn main:app --reload")
