from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

cities = ["Chennai", "Bangalore", "Mumbai", "Delhi"]

while True:
    event = {
        "order_id": random.randint(1000, 9999),
        "amount": round(random.uniform(100, 1000), 2),
        "city": random.choice(cities)
    }

    producer.send("sales_topic", value=event)
    print("Sent:", event)

    time.sleep(1)