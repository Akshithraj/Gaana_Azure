# Gaana_Azure

 Project Title: Gaana End-to-End Azure Data Engineering Pipeline

* Project Summary: Architected and implemented a production-grade, end-to-end data engineering pipeline on Azure to process Gaana streaming data using the                         Medallion Architecture (Bronze, Silver, Gold)
* The project integrates advanced CI/CD workflows, metadata-driven automation, and incremental processing to handle Big Data efficiently and reliably
-------------------------------------------------------------------------------------------
** Technical Highlights:
* Dynamic Data Ingestion (Bronze): Developed real-time, parameterized pipelines in Azure Data Factory (ADF) utilizing Change Data Capture (CDC) and watermarking for incremental loading and backfilling capabilities.
* Big Data Processing (Silver): Leveraged Azure Databricks with Spark Structured Streaming and Autoloader to ingest and transform raw data into a modular, reusable Python framework.
* Metadata-Driven Automation: Integrated Jinja templating to dynamically generate SQL queries and joins, significantly reducing manual coding and improving pipeline scalability.
* Advanced Data Modeling (Gold): Built Slowly Changing Dimensions (SCD Type 2) and Star Schema models using Delta Live Tables (DLT) and Lakeflow Pipelines to maintain historical data integrity.
* Governance & Security: Implemented Unity Catalog for centralized data governance, including the configuration of meta-stores, external locations, and access connectors.
* CI/CD & DevOps: Orchestrated code deployment using GitHub branching strategies and Databricks Asset Bundles (DABs) to ensure consistent environments and automated delivery.
* Automated Monitoring: Integrated Azure Logic Apps via Web Activities to trigger real-time alerts and monitoring for pipeline failures.
---------------------------------------------------------------------------------------------
* Tech Stack:
  Cloud: Microsoft Azure
  Orchestration: Azure Data Factory (ADF)
  Processing: Azure Databricks, PySpark, Spark Structured Streaming, Autoloader
  Storage: Azure Data Lake Storage (ADLS) Gen2, Delta Lake, Azure SQL Database
  Modeling/Governance: Unity Catalog, Delta Live Tables (DLT)
  DevOps: GitHub, Databricks Asset Bundles (DABs), Jinja2
  Monitoring: Azure Logic Apps
