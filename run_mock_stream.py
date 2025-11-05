import os, json, time, uuid, random, datetime as dt
os.makedirs("mock_data", exist_ok=True)
out_path = "mock_data/stream.jsonl"

PRODUCTS = [
    {"sku":"SKU-100","price":3.5},
    {"sku":"SKU-200","price":5.0},
    {"sku":"SKU-300","price":49.0},
    {"sku":"SKU-400","price":12.0},
]

with open(out_path, "w") as f:
    for i in range(600):  # 10 minutes of 1-sec events
        p = random.choice(PRODUCTS)
        evt = {
            "event_id": str(uuid.uuid4()),
            "ts": (dt.datetime.utcnow() + dt.timedelta(seconds=i)).isoformat(),
            "sku": p["sku"],
            "qty": random.randint(1,3),
            "unit_price": p["price"]
        }
        f.write(json.dumps(evt)+"\n")

print(f"Mock stream written to {out_path}")
