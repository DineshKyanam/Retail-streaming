# 🛒 Real-Time Retail Data Streaming Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-Streaming-black.svg)](https://kafka.apache.org/)
[![Spark](https://img.shields.io/badge/Apache%20Spark-3.x-orange.svg)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Lakehouse-00ADD8.svg)](https://delta.io/)

A production-grade, end-to-end data engineering platform that processes retail transactions in real-time. Built with modern streaming technologies to deliver sub-second analytics for business intelligence, fraud detection, and operational insights.

---

## 📊 Architecture Overview

```
┌─────────────┐      ┌─────────┐      ┌──────────┐      ┌────────────┐      ┌───────────┐
│   Retail    │─────▶│  Kafka  │─────▶│  Spark   │─────▶│ Delta Lake │─────▶│ Snowflake │
│Transactions │      │ Topics  │      │ Streaming│      │   (S3)     │      │    DWH    │
└─────────────┘      └─────────┘      └──────────┘      └────────────┘      └───────────┘
                                                                                     │
                                                                                     ▼
                                                                              ┌────────────┐
                                                                              │  Airflow   │
                                                                              │  + dbt     │
                                                                              └────────────┘
                                                                                     │
                                                                                     ▼
                                                                              ┌────────────┐
                                                                              │BI Dashboard│
                                                                              └────────────┘
```

### Key Components

- **Data Ingestion**: Mock producer simulates real-time POS and e-commerce transactions
- **Message Queue**: Apache Kafka handles high-throughput event streaming
- **Stream Processing**: Spark Structured Streaming performs real-time transformations and aggregations
- **Data Lake**: Delta Lake on S3 provides ACID transactions and time travel capabilities
- **Data Warehouse**: Snowflake stores processed data for analytics
- **Orchestration**: Apache Airflow + dbt manage ETL workflows and data transformations
- **Visualization**: Power BI/Tableau dashboards for business insights

---

## 🎯 Business Value

| Capability | Impact |
|-----------|--------|
| **Real-Time Analytics** | Sub-second latency for sales, revenue, and customer metrics |
| **Fraud Detection** | Immediate identification of suspicious transaction patterns |
| **Dynamic Pricing** | Instant pricing adjustments based on demand and inventory |
| **Inventory Optimization** | Real-time stock level monitoring and automated reordering |
| **Customer Insights** | Live segmentation and personalization opportunities |

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Languages** | Python, PySpark, SQL |
| **Streaming** | Apache Kafka, Spark Structured Streaming |
| **Storage** | Delta Lake (AWS S3), Snowflake |
| **Orchestration** | Apache Airflow, dbt |
| **Infrastructure** | Docker, AWS (MSK, EMR, S3) |
| **Visualization** | Power BI, Tableau, Streamlit |
| **Version Control** | Git, GitHub |

---

## 📁 Project Structure

```
Retail-streaming/
│
├── producer/
│   └── produce_transactions.py      # Kafka producer for mock retail data
│
├── spark_streaming/
│   └── stream_processor.py          # Spark Structured Streaming job
│
├── loaders/
│   └── snowflake_upsert.sql         # Snowflake data loading logic
│
├── airflow/
│   └── dags/
│       └── retail_streaming_dag.py  # Airflow orchestration DAG
│
├── mock/
│   ├── run_mock_stream.py           # Stream simulation scripts
│   └── run_batch_kpis.py            # Batch KPI generation
│
├── outputs/
│   └── aggregates_daily.csv         # Processed analytics results
│
├── docs/
│   └── architecture.png             # System architecture diagram
│
└── docker-compose.yml               # Local development environment
```

---

## 🚀 Quick Start

### Prerequisites

- **Docker Desktop** (version 20.10+)
- **Python** (3.8 or higher)
- **Apache Spark** (3.x)
- **AWS Account** (for S3 and optional cloud deployment)

### 1. Clone the Repository

```bash
git clone https://github.com/DineshKyanam/Retail-streaming.git
cd Retail-streaming
```

### 2. Start Local Services

Launch Kafka, Spark, and Airflow using Docker Compose:

```bash
docker compose up -d
```

Verify all services are running:
```bash
docker compose ps
```

### 3. Generate Mock Transaction Data

Start the Kafka producer to simulate retail transactions:

```bash
python producer/produce_transactions.py
```

### 4. Launch Spark Streaming Job

Process incoming data in real-time:

```bash
spark-submit spark_streaming/stream_processor.py
```

### 5. Monitor with Airflow

1. Navigate to the Airflow UI: [http://localhost:8080](http://localhost:8080)
2. Enable the `retail_streaming_dag` DAG
3. Trigger the DAG manually or wait for scheduled execution

---

## 📈 Sample Outputs

### Daily KPI Metrics

| Date | Orders | Revenue (USD) | Avg Order Value | Latency (ms) |
|------|--------|---------------|-----------------|--------------|
| 2025-10-01 | 1,023 | $34,456.78 | $33.69 | 320 |
| 2025-10-02 | 1,289 | $45,123.56 | $35.00 | 295 |
| 2025-10-03 | 1,411 | $49,320.47 | $34.95 | 270 |

📊 **[View Full Dataset →](outputs/aggregates_daily.csv)**

### Visualization Examples

**Orders Over Time**
- Real-time order volume tracking
- Hourly/daily trend analysis
- Peak period identification

**Revenue Analytics**
- Live revenue dashboards
- Product category performance
- Regional sales breakdowns

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```bash
# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
KAFKA_TOPIC=retail-transactions

# AWS Configuration
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
S3_BUCKET=your-delta-lake-bucket

# Snowflake Configuration
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_DATABASE=RETAIL_DB
SNOWFLAKE_SCHEMA=STREAMING
```

---

## 🧪 Testing

Run unit tests:

```bash
python -m pytest tests/
```

Run integration tests:

```bash
python -m pytest tests/integration/
```

---

## 📊 Monitoring & Observability

- **Kafka**: Monitor lag and throughput via Kafka Manager
- **Spark**: Track job metrics in Spark UI (http://localhost:4040)
- **Airflow**: View DAG execution status and logs in Airflow UI
- **Snowflake**: Query execution history and data quality metrics

---

## 🚀 Future Enhancements

- [ ] Integrate Kafka Connect for CDC (Change Data Capture)
- [ ] Add Schema Registry for data governance
- [ ] Implement Grafana dashboards for real-time monitoring
- [ ] Deploy to AWS (MSK + EMR + ECS) for production scalability
- [ ] Add CI/CD pipelines with GitHub Actions
- [ ] Implement comprehensive unit and integration testing
- [ ] Set up PagerDuty/Slack alerts for pipeline failures
- [ ] Add data quality checks with Great Expectations

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Dinesh Kyanam**

- GitHub: [@DineshKyanam](https://github.com/DineshKyanam)
- LinkedIn: [Connect with me](https://linkedin.com/in/dineshkyanam)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📧 Contact

For questions or feedback, please open an issue or reach out via [email](mailto:your.email@example.com).

---

**⭐ If you find this project useful, please consider giving it a star!**

