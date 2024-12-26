import pymongo
import pandas as pd
import os

ELECTRICITY_DIR = "./data/Electricity"
GAS_DIR = "./data/Gas"

# You can replace the URI with your own MongoDB URI
MONGO_URI = "mongodb+srv://cuongtran:cuongtran123@cluster0.5zjcy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# MongoDB connection
client = pymongo.MongoClient(MONGO_URI)
db = client["main"]


# Data mapping for collections
collections_mapping = {
    "electricity": {
        "2018": ["coteq_electricity_2018.csv", "stedin_electricity_2018.csv", "westland-infra_electricity_2018.csv"],
        "2019": ["coteq_electricity_2019.csv", "stedin_electricity_2019.csv", "westland-infra_electricity_2019.csv"],
        "2020": ["coteq_electricity_2020.csv", "stedin_electricity_2020.csv", "westland-infra_electricity_2020.csv"]
    },
    "gas": {
        "2018": ["coteq_gas_2018.csv", "stedin_gas_2018.csv", "westland-infra_gas_2018.csv"],
        "2019": ["coteq_gas_2019.csv", "stedin_gas_2019.csv", "westland-infra_gas_2019.csv"],
        "2020": ["coteq_gas_2020.csv", "stedin_gas_2020.csv", "westland-infra_gas_2020.csv"]
    }
}

# Check if a collection exists in MongoDB
def is_collection_exist(collection_name):
    return collection_name in db.list_collection_names()

# Load data into MongoDB
def load_data_to_mongodb(database, directory, year, file_list):
    collection_name = f"{database}_{year}"
    if is_collection_exist(collection_name):
        print(f"Collection {collection_name} already exists. Skipping data load process.")
        return
    
    collection = db[collection_name]
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        df = pd.read_csv(file_path)
        records = df.to_dict(orient="records")
        collection.insert_many(records)
        print(f"Data from {file_name} has been loaded to collection {collection_name}.")

# Main function
def main():
    for database, years in collections_mapping.items():
        for year, file_list in years.items():
            if database == "electricity":
                load_data_to_mongodb(database, ELECTRICITY_DIR, year, file_list)
            elif database == "gas":
                load_data_to_mongodb(database, GAS_DIR, year, file_list)

if __name__ == "__main__":
    main()
