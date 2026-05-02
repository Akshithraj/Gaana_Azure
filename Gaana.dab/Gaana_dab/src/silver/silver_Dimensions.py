{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1759955562363,
     "inputWidgets": {},
     "nuid": "78881035-3f0e-44d1-92b0-9283b12992c7",
     "showTitle": false,
     "startTime": 1759955561906,
     "submitTime": 1759955560716,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "%load_ext autoreload\n",
    "%autoreload 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1759955562462,
     "inputWidgets": {},
     "nuid": "1c41e43e-eca4-49a9-998c-bacd18ec14ed",
     "showTitle": false,
     "startTime": 1759955562377,
     "submitTime": 1759955560719,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "from pyspark.sql.functions import *\n",
    "from pyspark.sql.types import *\n",
    "from pyspark.sql.window import Window\n",
    "\n",
    "import os \n",
    "import sys\n",
    "\n",
    "project_pth = os.path.join(os.getcwd(),'..','..')\n",
    "sys.path.append(project_pth)\n",
    "\n",
    "from utils.transformations import reusable"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "6358b020-662d-40a1-a27a-11e5beb5598e",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## **DimUser**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "95d286b6-eeae-4e67-942d-a2fa0ca858cd",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "#### **AUTOLOADER**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "finishTime": 1759955564866,
     "inputWidgets": {},
     "nuid": "c1d68c58-872e-4701-9f18-cf474f163731",
     "showTitle": false,
     "startTime": 1759955562467,
     "submitTime": 1759955560755,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_user = spark.readStream.format(\"cloudFiles\")\\\n",
    "            .option(\"cloudFiles.format\",\"parquet\")\\\n",
    "            .option(\"cloudFiles.schemaLocation\",\"abfss://silver@storageazureproject.dfs.core.windows.net/DimUser/chekpoint\")\\\n",
    "            .option(\"schemaEvolutionMode\",\"addNewColumns\")\\\n",
    "            .load(\"abfss://bronze@storageazureproject.dfs.core.windows.net/DimUser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "286a278e-9aff-4ab2-be43-3225e399e5e6",
     "showTitle": false,
     "startTime": 1759955560760,
     "streamStates": {
      "196396c8-4d25-4191-8be6-3016b9abc605": [
       {
        "exception": null,
        "isActive": true,
        "name": "196396c8-4d25-4191-8be6-3016b9abc605",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "196396c8-4d25-4191-8be6-3016b9abc605",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560760,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(df_user)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "bd3ae1fb-407e-4fe0-9a71-3469c2cd426d",
     "showTitle": false,
     "startTime": 1759955560769,
     "streamStates": {
      "da18365b-4fe2-4e10-8e7e-506d0a53d555": [
       {
        "exception": null,
        "isActive": true,
        "name": "da18365b-4fe2-4e10-8e7e-506d0a53d555",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "da18365b-4fe2-4e10-8e7e-506d0a53d555",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560769,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_user = df_user.withColumn(\"user_name\",upper(col(\"user_name\")))\n",
    "display(df_user)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "be280803-e840-49fd-a3ce-232f1e6c748c",
     "showTitle": false,
     "startTime": 1759955560774,
     "streamStates": {
      "cc432414-fe33-469a-b4f3-61242ec1e10c": [
       {
        "exception": null,
        "isActive": true,
        "name": "cc432414-fe33-469a-b4f3-61242ec1e10c",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "cc432414-fe33-469a-b4f3-61242ec1e10c",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560774,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_user_obj = reusable()\n",
    "\n",
    "df_user = df_user_obj.dropColumns(df_user,['_rescued_data'])\n",
    "df_user = df_user.dropDuplicates(['user_id'])\n",
    "display(df_user)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "551158f6-5f50-46ff-965f-dc70d13c1ac5",
     "showTitle": false,
     "startTime": 1759955560788,
     "streamStates": {
      "54a8f5f9-951d-4102-958f-e0621d474de6": [
       {
        "exception": null,
        "isActive": true,
        "name": "54a8f5f9-951d-4102-958f-e0621d474de6",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "54a8f5f9-951d-4102-958f-e0621d474de6",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560788,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_user.writeStream.format(\"delta\")\\\n",
    "            .outputMode(\"append\")\\\n",
    "            .option(\"checkpointLocation\",\"abfss://silver@storageazureproject.dfs.core.windows.net/DimUser/chekpoint\")\\\n",
    "            .trigger(once=True)\\\n",
    "            .option(\"path\",\"abfss://silver@storageazureproject.dfs.core.windows.net/DimUser/data\")\\\n",
    "            .toTable(\"spotify_cata.silver.DimUser\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "2cc25802-f129-4896-aaf4-e77679607039",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## **DimArtist**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "08ac946a-7db2-4a31-8fa4-7eb2077ff976",
     "showTitle": false,
     "startTime": 1759955560807,
     "submitTime": 1759955560807,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_art = spark.readStream.format(\"cloudFiles\")\\\n",
    "            .option(\"cloudFiles.format\",\"parquet\")\\\n",
    "            .option(\"cloudFiles.schemaLocation\",\"abfss://silver@storageazureproject.dfs.core.windows.net/DimArt/chekpoint\")\\\n",
    "            .option(\"schemaEvolutionMode\",\"addNewColumns\")\\\n",
    "            .load(\"abfss://bronze@storageazureproject.dfs.core.windows.net/DimArtist\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "4fcb9d52-152f-4cba-9c8e-4482131e6bc9",
     "showTitle": false,
     "startTime": 1759955560812,
     "streamStates": {
      "590cb500-abb2-403e-b64f-53cde00cd8d4": [
       {
        "exception": null,
        "isActive": true,
        "name": "590cb500-abb2-403e-b64f-53cde00cd8d4",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "590cb500-abb2-403e-b64f-53cde00cd8d4",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560812,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(df_art)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "96610992-3115-4aac-955b-776913ef39ad",
     "showTitle": false,
     "startTime": 1759955560816,
     "streamStates": {
      "060c3e6f-4736-4a19-87ef-3c9594928c04": [
       {
        "exception": null,
        "isActive": true,
        "name": "060c3e6f-4736-4a19-87ef-3c9594928c04",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "060c3e6f-4736-4a19-87ef-3c9594928c04",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560816,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_art_obj = reusable()\n",
    "\n",
    "df_art = df_art_obj.dropColumns(df_art,['_rescued_data'])\n",
    "df_art = df_art.dropDuplicates(['artist_id'])\n",
    "display(df_art)   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "6befa945-de19-4c1f-9f3c-43b1ea74fabc",
     "showTitle": false,
     "startTime": 1759955560821,
     "streamStates": {
      "957f2dac-4d43-443e-aa0b-7f43be05a5d8": [
       {
        "exception": null,
        "isActive": true,
        "name": "957f2dac-4d43-443e-aa0b-7f43be05a5d8",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "957f2dac-4d43-443e-aa0b-7f43be05a5d8",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560821,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_art.writeStream.format(\"delta\")\\\n",
    "            .outputMode(\"append\")\\\n",
    "            .option(\"checkpointLocation\",\"abfss://silver@storageazureproject.dfs.core.windows.net/DimArt/chekpoint\")\\\n",
    "            .trigger(once=True)\\\n",
    "            .option(\"path\",\"abfss://silver@storageazureproject.dfs.core.windows.net/DimArt/data\")\\\n",
    "            .toTable(\"spotify_cata.silver.DimArtist\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "d0f1c11a-3090-4885-9f2f-210f2f1b522c",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "## **DimTrack**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "1393a7fa-bcee-493d-8bcd-1d1b4dfbb66f",
     "showTitle": false,
     "startTime": 1759955560838,
     "submitTime": 1759955560838,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_track = spark.readStream.format(\"cloudFiles\")\\\n",
    "            .option(\"cloudFiles.format\",\"parquet\")\\\n",
    "            .option(\"cloudFiles.schemaLocation\",\"abfss://silver@storageazureproject.dfs.core.windows.net/DimTrack/chekpoint\")\\\n",
    "            .option(\"schemaEvolutionMode\",\"addNewColumns\")\\\n",
    "            .load(\"abfss://bronze@storageazureproject.dfs.core.windows.net/DimTrack\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "26442fbd-cf59-490f-81c5-c9bf47175900",
     "showTitle": false,
     "startTime": 1759955560842,
     "streamStates": {
      "82c0a007-7ece-482d-8fdb-8a8c32eb9077": [
       {
        "exception": null,
        "isActive": true,
        "name": "82c0a007-7ece-482d-8fdb-8a8c32eb9077",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "82c0a007-7ece-482d-8fdb-8a8c32eb9077",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560842,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(df_track)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "55bc4235-0ee1-4569-b588-a4ae3101292d",
     "showTitle": false,
     "startTime": 1759955560846,
     "streamStates": {
      "c6bf187e-83b1-45b4-b884-1971e392ea69": [
       {
        "exception": null,
        "isActive": true,
        "name": "c6bf187e-83b1-45b4-b884-1971e392ea69",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "c6bf187e-83b1-45b4-b884-1971e392ea69",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560846,
     "tableResultSettingsMap": {
      "0": {
       "dataGridStateBlob": "{\"version\":1,\"tableState\":{\"columnPinning\":{\"left\":[\"#row_number#\"],\"right\":[]},\"columnSizing\":{},\"columnVisibility\":{}},\"settings\":{\"columns\":{}},\"syncTimestamp\":1759948077138}",
       "filterBlob": null,
       "queryPlanFiltersBlob": null,
       "tableResultIndex": 0
      }
     },
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_track = df_track.withColumn(\"durationFlag\",when(col('duration_sec')<150,\"low\")\\\n",
    "                                            .when(col('duration_sec')<300,\"medium\")\\\n",
    "                                            .otherwise(\"high\"))\n",
    "\n",
    "df_track = df_track.withColumn(\"track_name\",regexp_replace(col('track_name'),'-',' '))\n",
    "\n",
    "df_track = reusable().dropColumns(df_track,['_rescued_data'])\n",
    "\n",
    "display(df_track)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "b0bf26af-8d68-4fa6-814e-ae10c41c205f",
     "showTitle": false,
     "startTime": 1759955560850,
     "streamStates": {
      "96882dd6-3604-4926-a191-af9be325b156": [
       {
        "exception": null,
        "isActive": true,
        "name": "96882dd6-3604-4926-a191-af9be325b156",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "96882dd6-3604-4926-a191-af9be325b156",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560850,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_track.writeStream.format(\"delta\")\\\n",
    "            .outputMode(\"append\")\\\n",
    "            .option(\"checkpointLocation\",\"abfss://silver@storageazureproject.dfs.core.windows.net/DimTrack/chekpoint\")\\\n",
    "            .trigger(once=True)\\\n",
    "            .option(\"path\",\"abfss://silver@storageazureproject.dfs.core.windows.net/DimTrack/data\")\\\n",
    "            .toTable(\"spotify_cata.silver.DimTrack\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "e1b373ff-baf7-4890-b260-a7de9f0d2efa",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "%md\n",
    "## **DimDate**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "e6995bf7-bbaa-4984-9327-d2a3a5dd52ba",
     "showTitle": false,
     "startTime": 1759955560864,
     "submitTime": 1759955560864,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_date = spark.readStream.format(\"cloudFiles\")\\\n",
    "            .option(\"cloudFiles.format\",\"parquet\")\\\n",
    "            .option(\"cloudFiles.schemaLocation\",\"abfss://silver@storageazureproject.dfs.core.windows.net/DimDate/chekpoint\")\\\n",
    "            .option(\"schemaEvolutionMode\",\"addNewColumns\")\\\n",
    "            .load(\"abfss://bronze@storageazureproject.dfs.core.windows.net/DimDate\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "203136e2-8230-41a3-90bf-154a4543e6ba",
     "showTitle": false,
     "startTime": 1759955560867,
     "streamStates": {
      "fe5e9475-c6fc-4d5b-8a12-35f389c9bd83": [
       {
        "exception": null,
        "isActive": true,
        "name": "fe5e9475-c6fc-4d5b-8a12-35f389c9bd83",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "fe5e9475-c6fc-4d5b-8a12-35f389c9bd83",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560867,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_date = reusable().dropColumns(df_date,['_rescued_data'])\n",
    "\n",
    "df_date.writeStream.format(\"delta\")\\\n",
    "            .outputMode(\"append\")\\\n",
    "            .option(\"checkpointLocation\",\"abfss://silver@storageazureproject.dfs.core.windows.net/DimDate/chekpoint\")\\\n",
    "            .trigger(once=True)\\\n",
    "            .option(\"path\",\"abfss://silver@storageazureproject.dfs.core.windows.net/DimDate/data\")\\\n",
    "            .toTable(\"spotify_cata.silver.DimDate\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "c46f8dd4-f045-4e7e-aae4-da7dcf0e2ef3",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "source": [
    "%md\n",
    "## **FactStream**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "35d0dbd0-eec8-425a-b701-a549441edc7b",
     "showTitle": false,
     "startTime": 1759955560882,
     "submitTime": 1759955560882,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_fact = spark.readStream.format(\"cloudFiles\")\\\n",
    "            .option(\"cloudFiles.format\",\"parquet\")\\\n",
    "            .option(\"cloudFiles.schemaLocation\",\"abfss://silver@storageazureproject.dfs.core.windows.net/FactStream/chekpoint\")\\\n",
    "            .option(\"schemaEvolutionMode\",\"addNewColumns\")\\\n",
    "            .load(\"abfss://bronze@storageazureproject.dfs.core.windows.net/FactStream\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "ba03dac2-0ad0-4e7c-94f7-89eead34554a",
     "showTitle": false,
     "startTime": 1759955560886,
     "streamStates": {
      "dd199849-e357-4bd9-adc1-9fc2ba5dfcbd": [
       {
        "exception": null,
        "isActive": true,
        "name": "dd199849-e357-4bd9-adc1-9fc2ba5dfcbd",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "dd199849-e357-4bd9-adc1-9fc2ba5dfcbd",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560886,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "display(df_fact)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "80071904-e8c4-41a5-9495-7709ac608496",
     "showTitle": false,
     "startTime": 1759955560890,
     "streamStates": {
      "aa93bd4f-a983-4472-83a7-7f6cbe0e7e65": [
       {
        "exception": null,
        "isActive": true,
        "name": "aa93bd4f-a983-4472-83a7-7f6cbe0e7e65",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       },
       {
        "exception": null,
        "isActive": false,
        "name": "aa93bd4f-a983-4472-83a7-7f6cbe0e7e65",
        "progressJson": null,
        "sink": null,
        "sources": [],
        "version": 2
       }
      ]
     },
     "submitTime": 1759955560890,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "df_fact = reusable().dropColumns(df_fact,['_rescued_data'])\n",
    "\n",
    "df_fact.writeStream.format(\"delta\")\\\n",
    "            .outputMode(\"append\")\\\n",
    "            .option(\"checkpointLocation\",\"abfss://silver@storageazureproject.dfs.core.windows.net/FactStream/chekpoint\")\\\n",
    "            .trigger(once=True)\\\n",
    "            .option(\"path\",\"abfss://silver@storageazureproject.dfs.core.windows.net/FactStream/data\")\\\n",
    "            .toTable(\"spotify_cata.silver.FactStream\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "38f4ba78-1dfc-4dd3-a9e6-a77367ab574e",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": {
    "hardware": {
     "accelerator": null,
     "gpuPoolId": null,
     "memory": null
    },
    "software": null
   },
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "3"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "mostRecentlyExecutedCommandWithImplicitDF": {
     "commandId": 6731249260900475,
     "dataframes": [
      "_sqldf"
     ]
    },
    "pythonIndentUnit": 4
   },
   "notebookName": "silver_Dimensions",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
