import joblib
import pandas as pd

# Load the scaler created during preprocessing
scaler = joblib.load("../models/scaler.save")

# Get feature column order from training data
model_features = pd.read_csv("../data/X_train.csv", nrows=0).columns.tolist()


def extract_features(txn: dict) -> dict:
    # Convert transaction dict to DataFrame
    df = pd.DataFrame([txn])

    # Scale Amount column
    df[model_features] = scaler.transform(df[model_features])

    # Keep only columns used in model
    df = df[model_features]

    return df.to_dict(orient="records")[0]