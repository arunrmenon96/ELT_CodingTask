import unittest
from extractor import DataExtractor
from transformer import DataTransformer
from loader import DataLoader
from pymongo import MongoClient

class TestIntegration(unittest.TestCase):

    def test_etl_pipeline(self):
        # Extract
        data = DataExtractor.read_data('./member-data.csv')

        # Transform
        transformed_data = DataTransformer.transform_data(data)

        # Load
        client = MongoClient('mongodb://localhost:27017/')
        db = client['etl_db_test']
        collection = db['members-integration-test']
        collection.delete_many({})  # Clear the collection before testing

        DataLoader.load_data(transformed_data, db_name='etl_db_test', collection_name='members-integration-test')
        self.assertEqual(collection.count_documents({}), len(transformed_data))

if __name__ == '__main__':
    unittest.main()
