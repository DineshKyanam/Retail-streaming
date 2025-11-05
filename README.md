## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/DineshKyanam/Retail-streaming.git
cd Retail-streaming

2️⃣ Start the Local Environment

Make sure you have Docker Desktop running, then start your local stack:

docker compose up -d


This starts Kafka, Spark, and Airflow services locally.

3️⃣ Generate Streaming Data

Run the mock data producer to continuously push transactions into Kafka:

python producer/produce_transactions.py

4️⃣ Process Data with Spark

Run the real-time Spark streaming job:

spark-submit spark_streaming/stream_processor.py

5️⃣ Monitor via Airflow

Access Airflow UI at http://localhost:8080

Enable and trigger the DAG retail_streaming_dag to orchestrate the ETL flow.

📊 Sample Outputs

Below is a snapshot of daily retail KPIs produced by the streaming pipeline:

date	orders	revenue_usd	avg_order_value_usd	streaming_latency_ms
2025-10-01	1023	34456.78	33.69	320
2025-10-02	1289	45123.56	35.00	295
2025-10-03	1411	49320.47	34.95	270

📁 Download full output → outputs/aggregates_daily.csv

📈 Business Value

Enables real-time sales and revenue analytics

Delivers sub-second latency metrics for decision-making

Supports fraud detection, dynamic pricing, and inventory optimization

Combines streaming + batch pipelines in a unified Lakehouse architecture

🧩 Future Enhancements

Integrate Kafka Connect and Schema Registry

Add Grafana dashboards for live metrics

Deploy to AWS MSK + EMR + ECS for cloud scalability

Add CI/CD pipelines for production-grade workflows

👤 Author

Dinesh Kyanam
Data Engineer | AWS | PySpark | Snowflake | Kafka | Airflow
📧 dineshkyanam@gmail.com

🔗 LinkedIn
