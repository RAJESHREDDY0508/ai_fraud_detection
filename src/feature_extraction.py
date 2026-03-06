import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
SCALER_PATH = os.path.abspath(os.path.join(BASE_DIR, "../models/scaler.save"))
DATA_PATH = os.path.abspath(os.path.join(BASE_DIR, "../data/X_train.csv"))

scaler = joblib.load(SCALER_PATH)

model_features = pd.read_csv(DATA_PATH, nrows=0).columns.tolist()

def extract_features(txn: dict) -> dict:
    df = pd.DataFrame([txn])
    df[model_features] = scaler.transform(df[model_features])
    df = df[model_features]
    return df.to_dict(orient="records")[0]