import pandas as pd
import lightgbm as lgb
from lightgbm import early_stopping
from sklearn.metrics import roc_auc_score
import os

# Paths
data_folder = os.path.join(os.path.dirname(__file__), "../data")
X_train = pd.read_csv(os.path.join(data_folder, "X_train.csv"))
X_test = pd.read_csv(os.path.join(data_folder, "X_test.csv"))
y_train = pd.read_csv(os.path.join(data_folder, "y_train.csv"))
y_test = pd.read_csv(os.path.join(data_folder, "y_test.csv"))

# LightGBM dataset
train_data = lgb.Dataset(X_train, label=y_train.values.ravel())
test_data = lgb.Dataset(X_test, label=y_test.values.ravel(), reference=train_data)

# LightGBM parameters
params = {
    'objective': 'binary',
    'metric': 'auc',
    'boosting_type': 'gbdt',
    'is_unbalance': True,
    'learning_rate': 0.05,
    'num_leaves': 31,
    'verbose': -1
}

# Train model with early stopping via callback
model = lgb.train(
    params,
    train_data,
    num_boost_round=200,
    valid_sets=[test_data],
    callbacks=[early_stopping(stopping_rounds=20)]
)

# Save model
os.makedirs(os.path.join(os.path.dirname(__file__), "../models"), exist_ok=True)
model.save_model(os.path.join(os.path.dirname(__file__), "../models/fraud_model.txt"))

# Evaluate
y_pred = model.predict(X_test)
print("Test AUC:", roc_auc_score(y_test, y_pred))