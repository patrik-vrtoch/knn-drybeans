import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# we load the data here
dataset_name = "Dry_Bean_Dataset.xlsx"
if not os.path.exists(dataset_name):
    print(f"'{dataset_name}' not found in this folder.")
    print("Run 'data_setup.py' script first to download the data to the repository")
    sys.exit(1)

df = pd.read_excel(dataset_name)
print("Dataset loaded successfully.")

print("\nGenerating plot:")

# plot
plt.figure(figsize=(12, 6))
sample_features = ['Area', 'Perimeter', 'AspectRation', 'Eccentricity', 'roundness']
sns.boxplot(data=df[sample_features])
plt.title("Scaling of Features")
plt.ylabel("Value Range")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("feature_scale_comparison.png")
plt.close()


print("\nPlot generated successfully.")