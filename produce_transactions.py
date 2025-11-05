import json, time, random, uuid, datetime as dt
from kafka import KafkaProducer

PRODUCTS = [
    {"sku":"SKU-100","name":"Coffee","price":3.5},
    {"sku":"SKU-200","name":"Notebook","price":5.0},
    {"sku":"SKU-300","name":"Headphones","price":49.0},
]

def main():
    producer = KafkaProducer(bootstrap_servers="localhost:9092",
                             value_serializer=lambda v: json.dumps(v).encode("utf-8"))
    topic = "pos_transactions"
    while True:
        p = random.choice(PRODUCTS)
        event = {
            "event_id": str(uuid.uuid4()),
            "ts": dt.datetime.utcnow().isoformat(),
            "sku": p["sku"],
            "qty": random.randint(1,3),
            "unit_price": p["price"]
        }
        producer.send(topic, event)
        producer.flush()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
