import unittest
import pandas as pd
from transformer import DataTransformer

class TestTransformer(unittest.TestCase):

    def test_transform_data(self):
        data = pd.DataFrame({
            'FirstName': [' John ', ' Jane ', ' '],
            'LastName': [' Doe ', ' Doe ', 'Smith'],
            'Company': ['Example Co.', 'Example Co.', 'Example Co.'],
            'BirthDate': ['01011990', 'notadate', '29022000'],
            'Salary': [60000, 120000, 45000],
            'Address': ['123 Main St', '456 Elm St', '789 Oak St'],
            'Suburb': ['Suburbia', 'Elmville', 'Oakland'],
            'State': ['CA', 'TX', 'WA'],
            'Post': ['90001', '73301', '98101'],
            'Phone': ['123-456-7890', '234-567-8901', '345-678-9012'],
            'Mobile': ['098-765-4321', '876-543-2109', '765-432-1098'],
            'Email': ['john.doe@example.com', 'jane.doe@example.com', 'smith@example.com']
        })
        transformed_data = DataTransformer.transform_data(data)

        # Check FullName
        self.assertEqual(transformed_data['FullName'][0], 'John Doe')
        self.assertEqual(transformed_data['FullName'][1], 'Jane Doe')
        self.assertEqual(transformed_data['FullName'][2], 'Smith')

        # Check BirthDate
        self.assertEqual(transformed_data['BirthDate'][0], '01/01/1990')
        self.assertEqual(transformed_data['BirthDate'][1], None)  # Invalid date should result in None
        self.assertEqual(transformed_data['BirthDate'][2], '29/02/2000')

        # Check Salary
        self.assertEqual(transformed_data['Salary'][0], '$60,000.00')
        self.assertEqual(transformed_data['Salary'][1], '$120,000.00')
        self.assertEqual(transformed_data['Salary'][2], '$45,000.00')

        # Check Age
        self.assertEqual(transformed_data['Age'][0], 34)
        self.assertTrue(pd.isna(transformed_data['Age'][1]))
        self.assertEqual(transformed_data['Age'][2], 24)

        # Check SalaryBucket
        self.assertEqual(transformed_data['SalaryBucket'][0], 'B')
        self.assertEqual(transformed_data['SalaryBucket'][1], 'C')
        self.assertEqual(transformed_data['SalaryBucket'][2], 'A')

        # Check nested Address
        self.assertEqual(transformed_data['Address'][0]['Address'], '123 Main St')
        self.assertEqual(transformed_data['Address'][0]['Suburb'], 'Suburbia')
        self.assertEqual(transformed_data['Address'][0]['State'], 'CA')
        self.assertEqual(transformed_data['Address'][0]['Post'], '90001')

        self.assertEqual(transformed_data['Address'][1]['Address'], '456 Elm St')
        self.assertEqual(transformed_data['Address'][1]['Suburb'], 'Elmville')
        self.assertEqual(transformed_data['Address'][1]['State'], 'TX')
        self.assertEqual(transformed_data['Address'][1]['Post'], '73301')

        self.assertEqual(transformed_data['Address'][2]['Address'], '789 Oak St')
        self.assertEqual(transformed_data['Address'][2]['Suburb'], 'Oakland')
        self.assertEqual(transformed_data['Address'][2]['State'], 'WA')
        self.assertEqual(transformed_data['Address'][2]['Post'], '98101')

if __name__ == '__main__':
    unittest.main()
