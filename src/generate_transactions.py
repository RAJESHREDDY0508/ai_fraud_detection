from kafka import KafkaProducer
import json
import time
import random
import pandas as pd

# Load training data to mimic real transaction structure
df = pd.read_csv("../data/X_train.csv")

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Transaction generator started...")

while True:

    # Pick random transaction from dataset
    txn = df.sample(1).to_dict(orient="records")[0]

    # Send transaction to Kafka topic
    producer.send("transactions", txn)

    print("Transaction sent:", txn)

    # Wait before sending next transaction
    time.sleep(1)