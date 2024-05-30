import unittest
import pandas as pd
from extractor import DataExtractor

class TestExtractor(unittest.TestCase):

    def test_read_data(self):
        data = DataExtractor.read_data('./member-data.csv')
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(data.shape[1], 12)  # Checking for 12 columns

if __name__ == '__main__':
    unittest.main()
