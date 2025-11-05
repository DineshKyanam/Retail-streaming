# Real-Time Retail Analytics Platform (Kafka + Spark + Snowflake + Airflow)

**Goal:** Demonstrate a streaming pipeline that ingests POS events, transforms them, and lands analytics-ready data.
This repo includes **production-like code** (Spark Structured Streaming, Airflow DAG, Snowflake loader) **and** a local
mock you can run without cloud infra to generate real outputs for screenshots.

## Architecture
- **Producer** → publishes POS events to Kafka topic `pos_transactions` (mock available).
- **Spark Structured Streaming** → consumes events, enriches with product data, aggregates KPIs (revenue, items/min).
- **Snowflake Loader** → batch upserts into a Snowflake table (local CSV sink mock included).
- **Airflow DAG** → orchestrates micro-batch compaction + quality checks.

## Quickstart (Mock, no Docker required)
```bash
python mock/run_mock_stream.py            # generates streaming-like JSONL
python mock/run_batch_kpis.py             # computes KPIs from the mock stream and writes outputs/
```

Outputs are written to `outputs/` and can be committed to Git for portfolio proof.

## Run with Docker (Kafka + Zookeeper) [Optional]
```bash
docker compose up -d
python producer/produce_transactions.py   # send events to Kafka
# submit your Spark job to consume the topic (example in spark_streaming/stream_processor.py)
```

## Airflow (Optional)
Place `airflow/dags/retail_streaming_dag.py` into your Airflow DAGs folder and update connections/variables.

## Snowflake
`loaders/snowflake_upsert.sql` contains a MERGE template. For local demo, `outputs/aggregates_daily.csv` is produced.

## Screenshots to capture
- outputs/aggregates_minute.csv (rolling KPIs)
- outputs/aggregates_daily.csv (daily KPIs)
- outputs/data_quality_summary.json (pass/fail stats)
