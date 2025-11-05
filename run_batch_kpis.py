import pandas as pd, json, os
from datetime import datetime

os.makedirs("outputs", exist_ok=True)
events = pd.read_json("mock_data/stream.jsonl", lines=True)
events["event_ts"] = pd.to_datetime(events["ts"])
events["revenue"] = events["qty"] * events["unit_price"]
events["minute"] = events["event_ts"].dt.floor("min")

# Minute aggregates
kpis = events.groupby("minute").agg(revenue_min=("revenue","sum"),
                                    items_min=("qty","sum")).reset_index()
kpis.to_csv("outputs/aggregates_minute.csv", index=False)

# Data quality summary
dq = {
    "rows": int(len(events)),
    "nulls_event_id": int(events["event_id"].isna().sum()),
    "min_ts": str(events["event_ts"].min()),
    "max_ts": str(events["event_ts"].max()),
    "total_revenue": float(events["revenue"].sum())
}
with open("outputs/data_quality_summary.json","w") as f:
    json.dump(dq, f, indent=2)

print("Wrote outputs/aggregates_minute.csv and outputs/data_quality_summary.json")
