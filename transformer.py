import pandas as pd
from datetime import datetime

class DataTransformer:
    @staticmethod
    def transform_data(data):
        # Handle invalid dates and convert BirthDate to DD/MM/YYYY format if it's a valid date
        data['BirthDate'] = pd.to_datetime(data['BirthDate'], format='%d%m%Y', errors='coerce')
        data['BirthDate'] = data['BirthDate'].apply(lambda x: x.strftime('%d/%m/%Y') if pd.notnull(x) else None)

        # Format Salary
        data['Salary'] = data['Salary'].apply(lambda x: f"${x:,.2f}")

        # Clean names
        data['FirstName'] = data['FirstName'].str.strip()
        data['LastName'] = data['LastName'].str.strip()

        # Merge FirstName and LastName
        data['FullName'] = data['FirstName'] + ' ' + data['LastName']

        # Strip FullName
        data['FullName'] = data['FullName'].str.strip()

        # Calculate Age, only if BirthDate is valid
        reference_date = datetime(2024, 3, 1)
        data['BirthDate_dt'] = pd.to_datetime(data['BirthDate'], format='%d/%m/%Y', errors='coerce')
        data['Age'] = data['BirthDate_dt'].apply(lambda x: (reference_date - x).days // 365 if pd.notnull(x) else None)

        # Salary Bucket
        data['SalaryBucket'] = data['Salary'].replace('[\\$,]', '', regex=True).astype(float)
        data['SalaryBucket'] = pd.cut(data['SalaryBucket'], bins=[0, 50000, 100000, float('Inf')], labels=['A', 'B', 'C'])

        # Drop unnecessary columns
        data = data.drop(columns=['FirstName', 'LastName', 'BirthDate_dt'])

        # Nest Address
        data['Address'] = data.apply(lambda row: {
            "Address": row['Address'],
            "Suburb": row['Suburb'],
            "State": row['State'],
            "Post": row['Post']
        }, axis=1)
        data = data.drop(columns=['Suburb', 'State', 'Post'])

        return data
