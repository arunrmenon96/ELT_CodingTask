# ETL Pipeline

This project demonstrates an ETL (Extract, Transform, Load) pipeline using Python. The pipeline reads data from a CSV file, transforms it, and loads it into a MongoDB database.

## Prerequisites

- Python 3.8+
- Docker
- Docker Compose

## Setup and Running

1. **Clone the repository:**

```sh
git clone <repository_link>
cd etl_project
```

2. **Build and run the Docker containers:**

```sh
docker-compose up --build
```

3. **Running Tests:**

To run tests, use the following command:

```sh
python -m unittest discover
```

## Project Structure

- `main.py`: Contains the core ETL logic.
- `extractor.py`: Contains the data extraction logic.
- `transformer.py`: Contains the data transformation logic.
- `loader.py`: Contains the data loading logic.
- `test_extractor.py`: Contains test cases for the DataExtractor class.
- `test_transformer.py`: Contains test cases for the DataTransformer class.
- `test_loader.py`: Contains test cases for the DataLoader class.
- `test_integration.py`: Contains integration test cases for the entire ETL pipeline.
- `Dockerfile`: Dockerfile for creating a Docker image of the application.
- `docker-compose.yml`: Docker Compose file for setting up the services.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Instructions for setting up and running the ETL pipeline.

## Details

- **Reading Data:** The `DataExtractor.read_data()` function reads the data from a CSV file.
- **Transforming Data:** The `DataTransformer.transform_data()` function performs necessary transformations, including date format conversion, salary formatting, and age calculation.
- **Loading Data:** The `DataLoader.load_data()` function loads the transformed data into a MongoDB database.
