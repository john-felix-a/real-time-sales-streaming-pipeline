# 🚀 Real-Time Sales Streaming Pipeline

A real-time data streaming pipeline built using **Apache Kafka**, **PySpark Structured Streaming**, and **Docker**.

This project simulates live sales events, streams them through Kafka, and performs real-time window-based revenue aggregation using Spark.

---

## 📌 Project Overview

This pipeline demonstrates how real-time data flows through a distributed system:

Python Producer → Kafka Broker → PySpark Structured Streaming → Window Aggregation

The system processes streaming sales events and calculates total revenue per city in fixed time windows.

---

## 🛠 Tech Stack

- Python 3.12
- Apache Kafka
- ZooKeeper
- PySpark 4.0.1
- Docker & Docker Compose
- Structured Streaming (Event-Time Processing)

---

## 🔥 Features

- Real-time JSON event generation
- Kafka topic-based messaging
- Spark Structured Streaming integration
- Event-time windowed aggregation
- Watermark support
- Dockerized Kafka infrastructure
- Micro-batch streaming execution

---

## ▶ How To Run This Project

- pip install -r requirements.txt
- cd docker
- docker-compose up -d
- python producer/DataProducer.py
- python consumer/SparkConsumer.py