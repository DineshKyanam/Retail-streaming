# Real-Time Retail Data Streaming Platform
A production-grade real-time retail data pipeline built using Apache Kafka, Spark Structured Streaming, Delta Lake, Snowflake, and Airflow.
This project simulates a retail company's end-to-end data flow — from live transaction ingestion to data warehousing and analytics — demonstrating a complete modern cloud-native data engineering pipeline.

## Architecture (Modern Data Lakehouse)
Architecture

Flow:
Mock Producer → Kafka → Spark Structured Streaming → Delta Lake (S3) → Snowflake → dbt + Airflow → BI Dashboard

## Project Overview
This project replicates a real-world retail data streaming platform where continuous point-of-sale and online transactions are processed in real time.
The goal is to deliver low-latency analytics for decision-making, fraud detection, and KPI monitoring.

## Objectives
- Real-time ingestion using Kafka
- Stream processing with Spark Structured Streaming
- Storage and versioning via Delta Lake
- Warehouse integration with Snowflake
- Workflow orchestration using Airflow
- Visualization via BI tools (Power BI / Tableau / Streamlit)

## Tech Stack
| Category | Tools / Technologies |
|----------|---------------------|
| Languages | Python, PySpark, SQL |
| Streaming | Apache Kafka, Spark Structured Streaming |
| Storage / Lakehouse | Delta Lake on AWS S3, Snowflake |
| Orchestration | Apache Airflow, dbt |
| Infrastructure | Docker, AWS |
| Visualization | Power BI / Tableau / Streamlit |
| Version Control | Git & GitHub |

## 🗂️ Project Structure
```
Retail-streaming/
│
├── producer/ → Generates mock retail transactions
│   └── produce_transactions.py
│
├── spark_streaming/ → Spark job to process data in real-time
│   └── stream_processor.py
│
├── loaders/ → SQL scripts for Snowflake upsert logic
│   └── snowflake_upsert.sql
│
├── airflow/dags/ → Airflow DAG for orchestrating the pipeline
│   └── retail_streaming_dag.py
│
├── mock/ → Scripts to simulate batch KPIs
│   ├── run_mock_stream.py
│   └── run_batch_kpis.py
│
├── outputs/ → Processed KPI and analytics results
│   └── aggregates_daily.csv
│
├── docs/ → Documentation and diagrams
│   └── architecture.png
│
└── docker-compose.yml → Local environment setup for Kafka/Spark
```

## Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/DineshKyanam/Retail-streaming.git
cd Retail-streaming
```

### 2️⃣ Start the Local Environment

Make sure you have Docker Desktop running, then start your local stack:

```bash
docker compose up -d
```

This starts Kafka, Spark, and Airflow services locally.

### 3️⃣ Generate Streaming Data

Run the mock data producer to continuously push transactions into Kafka:

```bash
python producer/produce_transactions.py
```

### 4️⃣ Process Data with Spark

Run the real-time Spark streaming job:

```bash
spark-submit spark_streaming/stream_processor.py
```

### 5️⃣ Monitor via Airflow

Access Airflow UI at http://localhost:8080

Enable and trigger the DAG `retail_streaming_dag` to orchestrate the ETL flow.

## Sample Outputs
Below is a snapshot of daily retail KPIs produced by the streaming pipeline:

| date | orders | revenue_usd | avg_order_value_usd | streaming_latency_ms |
|------|--------|-------------|---------------------|---------------------|
| 2025-10-01 | 1023 | 34456.78 | 33.69 | 320 |
| 2025-10-02 | 1289 | 45123.56 | 35.00 | 295 |
| 2025-10-03 | 1411 | 49320.47 | 34.95 | 270 |

📁 Download full output → outputs/aggregates_daily.csv

## KPI Dashboards
**Orders Over Time**
Orders Over Time

**Revenue Over Time**
Revenue Over Time

**Sample Outputs (CSV)**
📁 Download full output → outputs/aggregates_daily.csv

## Business Value
- Enables real-time sales and revenue analytics
- Delivers sub-second latency metrics for fast decision-making
- Supports fraud detection, dynamic pricing, and inventory optimization
- Combines streaming + batch processing in a unified Lakehouse architecture
- Demonstrates production-ready orchestration with Airflow and dbt

## Future Enhancements

- Integrate Kafka Connect and Schema Registry
- Add Grafana dashboards for live monitoring
- Deploy to AWS MSK + EMR + ECS for cloud scalability
- Implement CI/CD pipelines for automated deployments
- Add unit tests and alerting for production reliability

## About
Real-time retail data streaming platform using Kafka, Spark Structured Streaming, Delta Lake, and Airflow on AWS.
