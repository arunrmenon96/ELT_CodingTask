from extractor import DataExtractor
from transformer import DataTransformer
from loader import DataLoader

if __name__ == "__main__":
    data = DataExtractor.read_data('./member-data.csv')
    transformed_data = DataTransformer.transform_data(data)
    DataLoader.load_data(transformed_data)
