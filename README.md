# About
Practice Course on Big Data
* https://bigdatateam.org/big-data-course

# Spark Configuration

Use port_1 and port_2 provided to you during the class.

In case you would like to run Jupyter notebook interface for pyspark, at first, you need to launch Jupyter:
```bash
jupyter notebook --port=port_1
```

As soon as you launch notebook, you can start PySpark with the help of the forllowing configuration:

```python
from pyspark import SparkConf, SparkContext

spark_conf = (
    SparkConf()
    .set("spark.ui.port", port_2)
    .set("spark.driver.memory", "512m")
    .set("spark.executor.instances", "2")
    .set("spark.executor.cores", "1")
    .setAppName("your shiny name")
    .setMaster("yarn")
)
sc = SparkContext(conf=spark_conf)
```

You will be able to use the same code snippet for spark-submit.

Use the following shortuct to start interactive Jupyter Pyspark session:
```bash
PYSPARK_DRIVER_PYTHON=jupyter PYSPARK_PYTHON=python3.10 PYSPARK_DRIVER_PYTHON_OPTS='notebook --port=port_1' pyspark --conf spark.ui.port=port_2 --driver-memory 512m --master yarn --num-executors 2 --executor-cores 1
# set Python v.3.6 for Spark 2.4.7 (old version compatibility)
PYSPARK_DRIVER_PYTHON=jupyter PYSPARK_PYTHON=python3.10 PYSPARK_DRIVER_PYTHON_OPTS='notebook --port=port_1' pyspark --conf spark.ui.port=port_2 --driver-memory 512m --master yarn --num-executors 2 --executor-cores 1
```

## Spark Notes

You usually use "brain-master" for ssh forwarding. Be cautions about "localhost" in the following code snippet.
Add the following rule for ssh forwarding:
```
-L port_1:localhost:port_1 
```

Open the following URL in you favourite browser:
* http://localhost:port_1


Spark Structured Streaming and Kafka will require to add extra flags:
```bash
# Spark 3.2.4
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4
# Spark 2.4.7
--packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0
```
see more details at:
* https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html

Spark Cassandra will require two following flags:
```bash
--conf spark.cassandra.connection.host=brain-node1
# Spark 3.2.4
--packages com.datastax.spark:spark-cassandra-connector_2.12:3.2.0
# Spark 2.4.7
--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.2
```

Useful Spark documentation links:
* PySpark API: [v.3.2.4](https://spark.apache.org/docs/3.2.4/api/python/index.html), [v.2.4.7](https://spark.apache.org/docs/2.4.7/api/python/index.html)
* PySpark SQL API: [v.3.2.4](https://spark.apache.org/docs/3.2.4/api/python/reference/pyspark.sql.html), [v.2.4.7](https://spark.apache.org/docs/2.4.7/api/python/pyspark.sql.html)
* Pandas API on Spark (experimental): https://spark.apache.org/docs/3.2.4/api/python/reference/pyspark.pandas/index.html
