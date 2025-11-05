# Spark Structured Streaming example (submit with spark-submit)
# Reads Kafka 'pos_transactions' topic, enriches, aggregates, and writes micro-batch parquet.
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("retail-stream").getOrCreate()

df = (spark.readStream
      .format("kafka")
      .option("kafka.bootstrap.servers","localhost:9092")
      .option("subscribe","pos_transactions")
      .load())

events = (df.selectExpr("CAST(value as STRING) as json")
            .select(F.from_json("json","event_id STRING, ts STRING, sku STRING, qty INT, unit_price DOUBLE").alias("x"))
            .select("x.*")
            .withColumn("event_ts", F.to_timestamp("ts"))
            .withWatermark("event_ts","5 minutes")
            .withColumn("revenue", F.col("qty")*F.col("unit_price")))

kpis = (events
        .groupBy(F.window("event_ts","1 minute").alias("w"))
        .agg(F.sum("revenue").alias("revenue_min"),
             F.sum("qty").alias("items_min")))

(qpis := kpis.select("w.start","w.end","revenue_min","items_min")).writeStream \    .outputMode("append").format("parquet").option("path","/tmp/retail/kpis_minute").option("checkpointLocation","/tmp/retail/_chk").start().awaitTermination()
