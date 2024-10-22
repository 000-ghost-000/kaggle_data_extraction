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

"""
import os
import kaggle
import pandas as pd

def download_dataset(dataset_name, download_path='data/'):
    """
#    Downloads a Kaggle dataset.
    
 #   Parameters:
  #  - dataset_name: str, the Kaggle dataset in the form 'owner/dataset-name'
   # - download_path: str, path where the dataset should be downloaded
"""
        # Ensure the download path exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    # Download the dataset using Kaggle API
    print(f"Downloading {dataset_name} to {download_path}...")
    kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)
    print(f"Downloaded {dataset_name} to {download_path}")

def list_files_in_directory(directory_path):
    """
#    Lists the files in the specified directory.
    
 #   Parameters:
  #  - directory_path: str, path to the directory
    
   # Returns:
   # - List of files in the directory
"""
    print(f"Listing files in directory: {directory_path}")
    try:
        files = os.listdir(directory_path)
        for file in files:
            print(file)
        return files
    except Exception as e:
        print(f"Error listing files: {e}")
        return []

def load_data(file_path):
    """
    #Loads a CSV file into a pandas DataFrame.
    
    #Parameters:
    # -file_path: str, path to the CSV file
    
    #Returns:
    #- DataFrame containing the dataset
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
    # Public dataset: Titanic - Machine Learning from Disaster
    dataset_name = 'heptapod/titanic'
    download_path = 'data/'

    # Download dataset
    download_dataset(dataset_name, download_path)

    # List files in the download directory to find the correct CSV file name
    files = list_files_in_directory(download_path)

    # Assume the CSV file we need is the first CSV file found
    csv_file_name = next((f for f in files if f.endswith('.csv')), None)

    if csv_file_name is not None:
        file_path = os.path.join(download_path, csv_file_name)
        # Load the CSV file into a DataFrame
        data = load_data(file_path)

        # Display the first few rows
        if data is not None:
            print(data.head())
    else:
        print("No CSV file found in the downloaded dataset.")

"""
