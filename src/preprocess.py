import os
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Define absolute paths based on this script's location
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "../data"))

# 1️⃣ Load the dataset
input_path = os.path.join(DATA_DIR, "creditcard_2023.csv")
df = pd.read_csv(input_path)
print(f"Dataset loaded from: {input_path}")

# 2️⃣ Split features and labels
X = df.drop("Class", axis=1)
y = df["Class"]

# 3️⃣ Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4️⃣ Scale features
scaler = StandardScaler()
feature_cols = X_train.columns.tolist()
X_train[feature_cols] = scaler.fit_transform(X_train[feature_cols])
X_test[feature_cols] = scaler.transform(X_test[feature_cols])

# 5️⃣ Save the scaler
MODEL_DIR = os.path.abspath(os.path.join(BASE_DIR, "../models"))
os.makedirs(MODEL_DIR, exist_ok=True)

scaler_path = os.path.join(MODEL_DIR, "scaler.save")
joblib.dump(scaler, scaler_path)

print(f"Scaler saved at: {scaler_path}")

# 6️⃣ Save train/test splits as CSV using absolute paths
X_train.to_csv(os.path.join(DATA_DIR, "X_train.csv"), index=False)
X_test.to_csv(os.path.join(DATA_DIR, "X_test.csv"), index=False)
y_train.to_csv(os.path.join(DATA_DIR, "y_train.csv"), index=False)
y_test.to_csv(os.path.join(DATA_DIR, "y_test.csv"), index=False)

print(f"CSV files successfully saved in: {DATA_DIR}")