import sys
import subprocess
import os
import urllib.request

# these are the libraries we will need throughout the project
required_libs = ['pandas', 'numpy', 'scikit-learn', 'openpyxl', 'matplotlib', 'seaborn']


# here we check and install any missing libraries if they are not installed
print("Checking if all libraries are installed...")
for lib in required_libs:
    try:
        __import__(lib)
    except ImportError:
        print(f"Library '{lib}' missing. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

print("\nAll libraries are installed.")


import pandas as pd

# now we download the dataset I uploaded to dropbox for easy setup
dataset_url = "https://www.dropbox.com/scl/fi/c46876nsy5idrhocegkui/Dry_Bean_Dataset.xlsx?rlkey=pzprk8mpt7hluaki3nscrah0r&st=or5rch11&dl=1"
dataset_name = "Dry_Bean_Dataset.xlsx"

def dataset_exists():
    if not os.path.exists(dataset_name):
        print("Dataset not found locally, downloading from url:")
        try:
            urllib.request.urlretrieve(dataset_url, dataset_name)
        except Exception as e:
            print(f"Error downloading dataset: {e}")
    else:
        print("Dataset found locally, loading now...")

print("Looking for dataset...")
dataset_exists()
print("\nDataset found succesfully!")

# looking at the dataset and seeing how many beans belong to which class to see the distribution
df = pd.read_excel(dataset_name)
print("\nBean type distributions:")
print(df['Class'].value_counts())
