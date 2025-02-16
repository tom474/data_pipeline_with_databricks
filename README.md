# Data Pipeline with Databricks  

A **big data processing pipeline** leveraging **Databricks, Spark, and MongoDB** to perform **data ingestion, transformation, machine learning, and visualization** for electricity and gas consumption analysis.  

## Tech Stack  

- Python  
- Databricks  
- Apache Spark  
- MongoDB  

## Features  

### 1. Data Ingestion  
- Loads electricity and gas consumption data into **MongoDB**.  
- Reads and processes data in **PySpark DataFrames** for structured analysis.  

### 2. Data Cleaning and Transformation  
- Handles **missing values**, **removes redundant columns**, and **normalizes numerical data**.  
- Performs **outlier detection and transformation** using logarithmic scaling.  
- Applies **one-hot encoding** for categorical variables.  

### 3. Machine Learning Model Training  
- Builds **separate models** for **electricity** and **gas** consumption prediction.  
- Implements **Random Forest Regressor** and **Decision Tree Regressor** for analysis.  
- Tracks experiments using **MLflow**, logging **model metrics and hyperparameters**.  
- Best models selected:  
  - **Electricity**: Random Forest Regressor (`numTrees=30`, `maxDepth=7`).  
  - **Gas**: Decision Tree Regressor (`maxDepth=7`, `minInstancesPerNode=2`).  

### 4. Data Visualization  
- **MongoDB Charts Dashboard** for interactive analytics:  
  - **Top 10 Cities by Electricity & Gas Consumption**.  
  - **Electricity & Gas Consumption by Connection Type**.  
- View dashboard: [MongoDB Charts](https://charts.mongodb.com/charts-bigdataasm2-szigrao/public/dashboards/67724c59-0c78-4054-8e6b-1061df46332b).  
