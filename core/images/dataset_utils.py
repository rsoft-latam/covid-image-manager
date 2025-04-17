import os
import requests
from dotenv import load_dotenv
from zipfile import ZipFile


def download_dataset():
    """
    Downloads the COVID-19 Radiography Dataset from Kaggle using credentials
    stored in the .env file and extracts it to the data/ directory.
    If the dataset already exists, prompts the user to overwrite it.
    """
    print("Loading environment variables...")
    load_dotenv()

    username = os.getenv("KAGGLE_USERNAME")
    key = os.getenv("KAGGLE_KEY")

    if not username or not key:
        print("Kaggle credentials not found in .env")
        return

    dataset_url = "https://www.kaggle.com/api/v1/datasets/download/tawsifurrahman/covid19-radiography-database"
    output_dir = "data"
    dataset_folder = os.path.join(output_dir, "COVID-19_Radiography_Dataset")

    if os.path.exists(dataset_folder):
        print(f"Dataset already exists at: {dataset_folder}")
        choice = input("Do you want to overwrite it? (y/n): ").strip().lower()
        if choice != "y":
            print("Download cancelled.")
            return
        else:
            print("Removing existing dataset folder...")
            import shutil
            shutil.rmtree(dataset_folder)

    os.makedirs(output_dir, exist_ok=True)

    print("Connecting to Kaggle API (no kaggle.json required)...")
    response = requests.get(
        dataset_url,
        headers={"User-Agent": "Mozilla/5.0"},
        auth=(username, key),
        stream=True
    )

    if response.status_code != 200:
        print(f"Failed to download dataset: {response.status_code}")
        print(response.text)
        return

    zip_path = os.path.join(output_dir, "covid19-radiography-database.zip")
    with open(zip_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print("Extracting dataset...")
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

    os.remove(zip_path)
    print("Dataset successfully downloaded and extracted.")


def show_dataset_summary():
    """
    Displays a preview of the CSV dataset if available.
    """
    dataset_path = "data/covid_dataset.csv"
    if not os.path.exists(dataset_path):
        print("Dataset file not found. Please ensure 'data/covid_dataset.csv' exists.")
        return

    import pandas as pd
    df = pd.read_csv(dataset_path)
    print("📊 Dataset Preview:")
    print(df.head())
