import findspark

findspark.init(r'C:\app\spark-2.3.1-bin-hadoop2.7')

from pyspark.sql import SparkSession

spark = SparkSession.builder.master(
    'local[4]').appName("Hello World").getOrCreate()


