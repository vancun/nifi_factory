import findspark
from os import path

findspark.init(r'C:\app\spark-2.3.1-bin-hadoop2.7')

from pyspark.sql import SparkSession

# .config('spark.jars.packages', 'com.databricks:spark-avro_2.11:3.0.1')
spark = SparkSession.builder.master('local[4]').config('spark.jars.packages', 'com.databricks:spark-avro_2.11:3.0.1').appName("Hello World").getOrCreate()

from pyspark.sql.functions import *
from pyspark.sql.types import *

class Context:
    _vars = {}
    _data = {}

    def __init__(self, config={}, spark=None):
        self._conf = config
        self._spark = spark
        pass

    @property
    def vars(self):
        return self._vars

    @property
    def data_frames(self):
        return self._data

    @property
    def conf(self):
        return self._conf

    @property
    def spark(self):
        if not self._spark:
            # .config('spark.jars.packages', 'com.databricks:spark-avro_2.11:3.0.1')
            self._spark = SparkSession.builder.master('local[4]').appName("Hello World").getOrCreate()
        return self._spark


class Operator:
    def __init__(self, config):
        self._conf = config

    @property
    def conf(self):
        return self._conf

    def run(self, ctx):
        pass

    def prepare(self, ctx):
        pass

    def finish(self, ctx):
        pass

    def store_output(self, df, output_name, ctx):
        df_name = self.conf['output'][output_name]
        ctx.data_frames[df_name] = df

    def get_input(self, input_name, ctx):
        df_name = self.conf['input'][input_name]
        return ctx.data_frames[df_name]


class LoadData(Operator):
    def run(self, ctx):
        reader = ctx.spark.read.format(self.conf['format'])
        if ('options' in self.conf) and (self.conf['options']):
            for opt_name, opt_value in iter(self.conf['options']):
                reader = reader.option(opt_name, opt_value)
        df = reader.load(self.conf['path'])
        self.store_output(df, 'data', ctx)

class ExplodeData(Operator):
    def run(self, ctx):
        in_df = self.get_input('data', ctx)
        expr = self.conf['expression']
        out_df = in_df.select(explode(expr).alias('v')).select('v.*')
        self.store_output(out_df, 'data', ctx)

class WriteData(Operator):

    # https://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=save#pyspark.sql.DataFrame.save
    def run(self, ctx):
        in_df = self.get_input('data', ctx)
        fmt = self.conf['format']
        path = self.conf['path']
        mode = self.conf.get('mode', 'error')
        in_df.write.mode(mode).format(fmt).save(path)

ctx = Context(spark)

data_path = path.dirname(__file__) + '/../..'

loader = LoadData({'format': 'json',
        'path': data_path + '/users.json',
        'output': {
            'data': 'raw_users'
        }})
loader.run(ctx)

ExplodeData({
    'expression': 'results',
    'input': {'data': 'raw_users'},
    'output': {'data': 'users_list'}
}).run(ctx)

WriteData({
    'format': 'com.databricks.spark.avro',
    'path': data_path + '/users',
    'mode': 'overwrite',
    'input': {'data': 'users_list'}
}).run(ctx)

ctx.data_frames['users_list'].show(2)
