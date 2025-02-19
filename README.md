# Data Pipeline with Databricks  

This project focuses on building a data pipeline using **Databricks**, **PySpark**, and **MongoDB**, integrating **MLflow** for machine learning tracking. The pipeline handles data ingestion, transformation, model training, and visualization.

## Tech Stack  

- Python  
- Databricks  
- PySpark  
- MLflow
- MongoDB  

## Features  

### Data Preparation on MongoDB  
- Pre-loaded datasets categorized by year and type (Electricity, Gas).
- Collections structure: `electricity_2018`, `electricity_2019`, `electricity_2020`, `gas_2018`, `gas_2019`, `gas_2020`.

### Data Ingestion  
- Loading electricity and gas consumption data from MongoDB into PySpark DataFrames.
- Merging 2018 and 2019 data as the training dataset while 2020 data is used for testing.

### Data Exploration  
- Conversion of Spark DataFrames to Pandas for in-depth analysis.
- Shape, summary statistics, missing values, and outlier detection.
- Categorical and numerical features analysis.

### Data Cleaning  
- Removal of columns with excessive missing values (`%Defintieve aansl (NRM)`).
- Dropping identifier and high-cardinality categorical columns (`_id`, `street`, `zipcode_from`, `zipcode_to`).
- Eliminating constant columns (`annual_consume_lowtarif_perc` for gas).
- Handling outliers using log transformation.
- Duplicate data removal.

### Data Transformation  
- **Encoding categorical features** (One-Hot Encoding via `StringIndexer` & `OneHotEncoder`).
- **Scaling numerical features** using `MinMaxScaler`.
- **Feature engineering**: Combining transformed columns into a single feature vector.

### Model Training and Tracking  
- Implemented **Random Forest Regressor** and **Decision Tree Regressor** models.
- **MLflow** integration for parameter tracking and performance logging.
- Best models selected based on **MAE, R2, and RMSE** metrics:
  - **Electricity:** `RandomForestRegressor(numTrees=30, maxDepth=7)`
  - **Gas:** `DecisionTreeRegressor(maxDepth=7, minInstancesPerNode=2)`

### Data Visualization  
- **MongoDB Charts Dashboard**: [View Charts](https://charts.mongodb.com/charts-bigdataasm2-szigrao/public/dashboards/67724c59-0c78-4054-8e6b-1061df46332b)  
- Key visualizations:
  - **Top 10 Cities by Electricity Annual Consumption (2018)**
  - **Electricity Distribution of Connection Types (2019)**
  - **Top 10 Cities by Gas Annual Consumption (2018)**
  - **Gas Distribution of Connection Types (2019)**

## Quick Start

### Prerequisites

- Databricks Community Account: [Sign up](https://community.cloud.databricks.com)
- MongoDB Account: [Sign up](https://account.mongodb.com/account/login)

### Create a compute cluster

- On the sidebar, select **Compute**.
- Select **Create compute**.
- Enter compute name: **Big Data Assignment 2's Cluster**.
- Choose the databricks runtime version: **9.1 LTS ML (Scala 2.12, Spark 3.1.2)**.
- Select **Create compute**.

![task0-create-cluster.png](https://github.com/tom474/mongodb_and_spark/blob/main/assets/task0-create-cluster.png?raw=true)

### Install mongodb spark connector library
- On the navigation bar, select **Libraries**.
- Select **Install new**.
- For Library Source, select **Maven**.
- For Coordinates, select **Select Packages**.
- Select **Spark Packages**.
- Search and select **mongo-spark** with version **3.0.1**.
- Select **Install**.

![task0-install-library.png](https://github.com/tom474/mongodb_and_spark/blob/main/assets/task0-install-library.png?raw=true)

### Attach cluster to notebook
- Import the notebook to databricks using `.dbc` or `.ipynb` file.
- Select the notebook.
- For the Connect, select the created cluster.

![task0-attach-cluster.png](https://github.com/tom474/mongodb_and_spark/blob/main/assets/task0-attach-cluster.png?raw=true)
