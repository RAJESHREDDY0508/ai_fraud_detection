import json
from kafka import KafkaConsumer
from .risk_scoring import get_risk_score
from .decision_engine import make_decision


def start_processing():
    consumer = KafkaConsumer(
        "transactions",
        bootstrap_servers="localhost:9092",
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        auto_offset_reset="latest"
    )

    print("🚀 Real-time Processing Engine Active...")

    for message in consumer:
        txn = message.value
        try:
            score = get_risk_score(txn)
            decision = make_decision(score)

            # Log results
            result = {
                "amount": txn['Amount'],
                "score": round(float(score), 4),
                "decision": decision
            }
            print(f"Processed: {result}")

            # TODO: In a full stack app, you would send 'result'
            # to a database or a WebSocket here.

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    start_processing()