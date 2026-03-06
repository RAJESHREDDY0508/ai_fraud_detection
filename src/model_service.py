import os
import joblib
import pandas as pd
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

# Import our custom database and scoring logic
# Use relative imports (the dots) so they work when run as a module
from .database import SessionLocal, TransactionRecord, init_db
from .risk_scoring import get_risk_score

# 1. Initialize Database Tables on startup
init_db()


# 2. Define the Pydantic Schema for incoming API data
# This is what validates your JSON requests
class TransactionSchema(BaseModel):
    Amount: float
    V1: float;
    V2: float;
    V3: float;
    V4: float;
    V5: float
    V6: float;
    V7: float;
    V8: float;
    V9: float;
    V10: float
    V11: float;
    V12: float;
    V13: float;
    V14: float;
    V15: float
    V16: float;
    V17: float;
    V18: float;
    V19: float;
    V20: float
    V21: float;
    V22: float;
    V23: float;
    V24: float;
    V25: float
    V26: float;
    V27: float;
    V28: float


# 3. Create the FastAPI instance (CRITICAL: This must come before @app.post)
app = FastAPI(title="Real-Time Fraud Detection System")


# 4. Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 5. API Endpoints
@app.get("/")
def home():
    return {"status": "Online", "service": "Fraud Detection API"}


@app.post("/predict")
def predict(txn: TransactionSchema, db: Session = Depends(get_db)):
    try:
        # Convert Pydantic data to a standard dictionary
        txn_dict = txn.model_dump()

        # Calculate the risk score using our ML model
        # This calls feature_extraction and the LightGBM model internally
        score = get_risk_score(txn_dict)

        # Decision logic based on our engine thresholds
        decision = "ALLOW"
        if score > 0.8:
            decision = "BLOCK"
        elif score > 0.4:
            decision = "ALERT"

        # 💾 SAVE TO POSTGRESQL
        new_record = TransactionRecord(
            amount=txn.Amount,
            risk_score=float(score),
            decision=decision
        )
        db.add(new_record)
        db.commit()

        return {
            "amount": txn.Amount,
            "risk_score": round(float(score), 4),
            "decision": decision
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))