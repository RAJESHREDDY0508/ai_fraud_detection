from kafka import KafkaConsumer
import json

from risk_scoring import get_risk_score
from decision_engine import make_decision


# Create Kafka consumer
consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True
)

print("Fraud detection service started...")
print("Waiting for transactions...\n")


# Continuously listen for transactions
for message in consumer:

    txn = message.value

    try:
        # Get fraud risk score
        score = get_risk_score(txn)

        # Apply decision logic
        decision = make_decision(score)

        print(
            f"Amount: {txn['Amount']} | Risk Score: {score:.4f} | Decision: {decision}"
        )

    except Exception as e:

        print("Error processing transaction:", e)