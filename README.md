# Data Pipeline with Databricks  

A **scalable data pipeline** built using **Databricks, Apache Spark, and MongoDB** to process, transform, and analyze electricity and gas consumption data. The pipeline enables efficient data ingestion, cleaning, transformation, machine learning modeling, and visualization.

## Tech Stack  

- Python  
- Databricks  
- Apache Spark  
- MongoDB  

## Features  

### 1. Data Ingestion  
- Extracts electricity and gas consumption data from MongoDB.  
- Loads raw data into PySpark **DataFrames** for preprocessing.  

### 2. Data Cleaning and Transformation  
- Handles **missing values** by dropping irrelevant columns.  
- Removes **redundant features** with low variance or high cardinality.  
- Applies **log transformation** to mitigate skewness in numerical data.  
- Uses **one-hot encoding** for categorical variables.  
- Normalizes numerical features using **Min-Max scaling**.  

### 3. Model Training and Tracking  
- Trains **separate regression models** for **electricity and gas consumption**.  
- Implements **Random Forest** and **Decision Tree Regressors**.  
- Uses **MLflow** for **experiment tracking, model versioning, and metric logging**.  
- Selects **best-performing models** based on **MAE, R2, and RMSE** scores.  

### 4. Data Visualization  
- Creates **interactive dashboards** using MongoDB Charts.  
- Visualizes **top energy-consuming cities, distribution by connection type, and yearly trends**.  
- Provides **public MongoDB dashboard** for dynamic exploration.  
