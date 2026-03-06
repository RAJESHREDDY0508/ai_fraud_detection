import numpy as np
import lightgbm as lgb
from feature_extraction import extract_features

import os

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "../models/fraud_model.txt")

model = lgb.Booster(model_file=MODEL_PATH)

def get_risk_score(txn: dict):

    features = extract_features(txn)

    arr = np.array([list(features.values())])

    score = model.predict(arr)[0]

    return score