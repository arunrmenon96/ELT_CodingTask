import unittest
import pandas as pd
from pymongo import MongoClient
from loader import DataLoader

class TestLoader(unittest.TestCase):

    def test_load_data(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['etl_db_test']
        collection = db['members']
        collection.delete_many({})  # Clear the collection before testing

        data = pd.DataFrame({
            'FullName': ['John Doe'],
            'Company': ['Example Co.'],
            'BirthDate': ['01/01/1990'],
            'Salary': ['$60,000.00'],
            'Phone': ['123-456-7890'],
            'Mobile': ['098-765-4321'],
            'Email': ['john.doe@example.com'],
            'Age': [34],
            'SalaryBucket': ['B'],
            'Address': [{
                'Address': '123 Main St',
                'Suburb': 'Suburbia',
                'State': 'CA',
                'Post': '90001'
            }]
        })

        DataLoader.load_data(data, db_name='etl_db_test', collection_name='members')
        self.assertEqual(collection.count_documents({}), 1)

if __name__ == '__main__':
    unittest.main()
