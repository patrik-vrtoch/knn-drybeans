import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os
import sys

# we load the dataset
dataset_name = "Dry_Bean_Dataset.xlsx"
if not os.path.exists(dataset_name):
    print(f"'{dataset_name}' not found in this folder.")
    print("Run 'data_setup.py' script first to download the data to the repository")
    sys.exit(1)

df = pd.read_excel(dataset_name)
print("Dataset loaded succesfully.")

# we separate the class column from the rest of the features
X = df.drop(columns=['Class'])
y = df['Class']

# we split the data to be 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

print(f"Total training samples: {X_train.shape[0]}")
print(f"Total testing samples: {X_test.shape[0]}")

# now we scale the data
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Scaling finished.")
print(f"Original Area training mean: {X_train['Area'].mean():.2f}")
print(f"Scaled Area training mean: {X_train_scaled[:,0].mean():.2f}")
