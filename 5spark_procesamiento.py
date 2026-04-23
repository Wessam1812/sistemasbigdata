from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SuperFreshBigData").getOrCreate()

df = spark.read.csv("1ventas.csv", header=True, inferSchema=True)

df.show()

df_group = df.groupBy("producto").sum("ventas")

df_group.show()

# Enciende Spark, lee los datos grandes y los muestra
# suma ventas por producto y lo muestra