%load_ext autoreload
%autoreload 2
     

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

import os 
import sys

project_pth = os.path.join(os.getcwd(),'..','..')
sys.path.append(project_pth)

from utils.transformations import reusable
     
DimUser
AUTOLOADER

df_user = spark.readStream.format("cloudFiles")\
            .option("cloudFiles.format","parquet")\
            .option("cloudFiles.schemaLocation","abfss://silver@storageazureproject.dfs.core.windows.net/DimUser/chekpoint")\
            .option("schemaEvolutionMode","addNewColumns")\
            .load("abfss://bronze@storageazureproject.dfs.core.windows.net/DimUser")
     

display(df_user)
     

df_user = df_user.withColumn("user_name",upper(col("user_name")))
display(df_user)
     

df_user_obj = reusable()

df_user = df_user_obj.dropColumns(df_user,['_rescued_data'])
df_user = df_user.dropDuplicates(['user_id'])
display(df_user)
     

df_user.writeStream.format("delta")\
            .outputMode("append")\
            .option("checkpointLocation","abfss://silver@storageazureproject.dfs.core.windows.net/DimUser/chekpoint")\
            .trigger(once=True)\
            .option("path","abfss://silver@storageazureproject.dfs.core.windows.net/DimUser/data")\
            .toTable("Gaana_cata.silver.DimUser")
     
DimArtist

df_art = spark.readStream.format("cloudFiles")\
            .option("cloudFiles.format","parquet")\
            .option("cloudFiles.schemaLocation","abfss://silver@storageazureproject.dfs.core.windows.net/DimArt/chekpoint")\
            .option("schemaEvolutionMode","addNewColumns")\
            .load("abfss://bronze@storageazureproject.dfs.core.windows.net/DimArtist")
     

display(df_art)
     

df_art_obj = reusable()

df_art = df_art_obj.dropColumns(df_art,['_rescued_data'])
df_art = df_art.dropDuplicates(['artist_id'])
display(df_art)   
     

df_art.writeStream.format("delta")\
            .outputMode("append")\
            .option("checkpointLocation","abfss://silver@storageazureproject.dfs.core.windows.net/DimArt/chekpoint")\
            .trigger(once=True)\
            .option("path","abfss://silver@storageazureproject.dfs.core.windows.net/DimArt/data")\
            .toTable("Gaana_cata.silver.DimArtist")
     
DimTrack

df_track = spark.readStream.format("cloudFiles")\
            .option("cloudFiles.format","parquet")\
            .option("cloudFiles.schemaLocation","abfss://silver@storageazureproject.dfs.core.windows.net/DimTrack/chekpoint")\
            .option("schemaEvolutionMode","addNewColumns")\
            .load("abfss://bronze@storageazureproject.dfs.core.windows.net/DimTrack")
     

display(df_track)
     

df_track = df_track.withColumn("durationFlag",when(col('duration_sec')<150,"low")\
                                            .when(col('duration_sec')<300,"medium")\
                                            .otherwise("high"))

df_track = df_track.withColumn("track_name",regexp_replace(col('track_name'),'-',' '))

df_track = reusable().dropColumns(df_track,['_rescued_data'])

display(df_track)
     

df_track.writeStream.format("delta")\
            .outputMode("append")\
            .option("checkpointLocation","abfss://silver@storageazureproject.dfs.core.windows.net/DimTrack/chekpoint")\
            .trigger(once=True)\
            .option("path","abfss://silver@storageazureproject.dfs.core.windows.net/DimTrack/data")\
            .toTable("Gaana_cata.silver.DimTrack")
     
%md

DimDate

df_date = spark.readStream.format("cloudFiles")\
            .option("cloudFiles.format","parquet")\
            .option("cloudFiles.schemaLocation","abfss://silver@storageazureproject.dfs.core.windows.net/DimDate/chekpoint")\
            .option("schemaEvolutionMode","addNewColumns")\
            .load("abfss://bronze@storageazureproject.dfs.core.windows.net/DimDate")
     

df_date = reusable().dropColumns(df_date,['_rescued_data'])

df_date.writeStream.format("delta")\
            .outputMode("append")\
            .option("checkpointLocation","abfss://silver@storageazureproject.dfs.core.windows.net/DimDate/chekpoint")\
            .trigger(once=True)\
            .option("path","abfss://silver@storageazureproject.dfs.core.windows.net/DimDate/data")\
            .toTable("Gaana_cata.silver.DimDate")
     
%md

FactStream

df_fact = spark.readStream.format("cloudFiles")\
            .option("cloudFiles.format","parquet")\
            .option("cloudFiles.schemaLocation","abfss://silver@storageazureproject.dfs.core.windows.net/FactStream/chekpoint")\
            .option("schemaEvolutionMode","addNewColumns")\
            .load("abfss://bronze@storageazureproject.dfs.core.windows.net/FactStream")
     

display(df_fact)
     

df_fact = reusable().dropColumns(df_fact,['_rescued_data'])

df_fact.writeStream.format("delta")\
            .outputMode("append")\
            .option("checkpointLocation","abfss://silver@storageazureproject.dfs.core.windows.net/FactStream/chekpoint")\
            .trigger(once=True)\
            .option("path","abfss://silver@storageazureproject.dfs.core.windows.net/FactStream/data")\
            .toTable("Gaana_cata.silver.FactStream")
     


     
