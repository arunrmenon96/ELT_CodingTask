from pymongo import MongoClient

class DataLoader:
    @staticmethod
    def load_data(data, db_name='etl_db', collection_name='members'):
        client = MongoClient('mongodb://localhost:27017/')
        db = client[db_name]
        collection = db[collection_name]
        data_dict = data.to_dict("records")
        collection.insert_many(data_dict)
