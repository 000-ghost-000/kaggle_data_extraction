import os
import kaggle
import pandas as pd

def download_dataset(dataset_name, download_path='data/'):
    """
    Downloads a Kaggle dataset.
    
    Parameters:
    - dataset_name: str, the Kaggle dataset in the form 'owner/dataset-name'
    - download_path: str, path where the dataset should be downloaded
    """
    # Ensure the download path exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    # Download the dataset using Kaggle API
    print(f"Downloading {dataset_name} to {download_path}...")
    kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)
    print(f"Downloaded {dataset_name} to {download_path}")

def load_data(file_path):
    """
    Loads a CSV file into a pandas DataFrame.
    
    Parameters:
    - file_path: str, path to the CSV file
    
    Returns:
    - DataFrame containing the dataset
    """
    try:
        print(f"Loading data from {file_path}...")
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

if __name__ == '__main__':
    # Example Kaggle dataset: 'zynicide/wine-reviews'
    dataset_name = 'zynicide/wine-reviews'
    download_path = 'data/'
    csv_file_name = 'winemag-data-130k-v2.csv'

    # Download dataset
    download_dataset(dataset_name, download_path)

    # Load the CSV file into a DataFrame
    file_path = os.path.join(download_path, csv_file_name)
    data = load_data(file_path)

    # Display the first few rows
    if data is not None:
        print(data.head())
