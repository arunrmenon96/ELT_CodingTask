import pandas as pd

class DataExtractor:
    @staticmethod
    def read_data(file_path):
        data = pd.read_csv(file_path, delimiter='|', names=['FirstName', 'LastName', 'Company', 'BirthDate', 'Salary', 'Address', 'Suburb', 'State', 'Post', 'Phone', 'Mobile', 'Email'])
        return data
