# 🛡️ AI Fraud Detection System

![Fraud Detection Status](https://img.shields.io/badge/Status-Production--ready-green)
![Python Version](https://img.shields.io/badge/Python-3.9+-blue)
![Kafka](https://img.shields.io/badge/Streaming-Apache%20Kafka-red)
![ML](https://img.shields.io/badge/ML-LightGBM-orange)

A **real-time AI fraud detection system** that simulates credit card transactions using **Kafka streaming** and **LightGBM** for advanced risk scoring. Transactions are processed in milliseconds and automatically classified as **ALLOW**, **ALERT**, or **BLOCK** based on machine learning predictions and custom decision rules.

---

## 🚀 Key Features

* **End-to-End Pipeline**: From raw data preprocessing to real-time stream inference.
* **High-Performance ML**: Utilizes LightGBM for fast and accurate classification of imbalanced datasets.
* **Real-Time Simulation**: Kafka producer generates synthetic transaction streams for testing.
* **Scalable Architecture**: Dockerized Kafka/Zookeeper environment for easy deployment.
* **Automated Decision Engine**: Sophisticated logic to handle model outputs and trigger security actions.

---

## 📁 Project Structure

```text
ai_fraud_detection/
├── data/                   # Raw dataset, processed CSVs, and Scaler (.pkl)
├── models/                 # Trained LightGBM model files
├── src/                    # Core Source Code
│   ├── preprocess.py       # Data cleaning and scaling
│   ├── train_model.py      # Model training and evaluation
│   ├── feature_extraction.py # Real-time feature engineering
│   ├── risk_scoring.py     # Model inference logic
│   ├── decision_engine.py  # Rule-based action logic
│   ├── generate_transactions.py # Kafka Producer (Simulator)
│   └── stream_consumer.py  # Kafka Consumer (Detection Engine)
├── docker-compose.yml      # Infrastructure (Kafka & Zookeeper)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation