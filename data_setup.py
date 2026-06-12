import sys
import subprocess
import os
import urllib.request
import pandas as pd

def setup_and_load():

    # these are the libraries we will need throughout the project
    required_libs = ['pandas', 'numpy', 'scikit-learn', 'openpyxl', 'matplotlib', 'seaborn']

    # here we check and install any missing libraries if they are not installed
    print("\nChecking if all required libraries are installed...\n")
    for lib in required_libs:
        try:
            __import__(lib)
        except ImportError:
            print(f"Library '{lib}' missing. Installing now...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
    print("\nAll libraries are ready.\n")


    # now we download the dataset I uploaded to dropbox for easy setup
    dataset_url = "https://www.dropbox.com/scl/fi/c46876nsy5idrhocegkui/Dry_Bean_Dataset.xlsx?rlkey=pzprk8mpt7hluaki3nscrah0r&st=or5rch11&dl=1"
    dataset_name = "Dry_Bean_Dataset.xlsx"


    if not os.path.exists(dataset_name):
        print("\nDataset not found locally, downloading from url...\n")
        urllib.request.urlretrieve(dataset_url, dataset_name)
        print("\nDownload finished.\n")
    else:
        print("\nDataset found locally. Skipping download.\n")

    # looking at the dataset and seeing how many beans belong to which class to see the distribution
    df = pd.read_excel(dataset_name)
    print("\nBean type distributions:\n")
    print(df['Class'].value_counts())

    return df

if __name__ == "__main__":
    setup_and_load()
