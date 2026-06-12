import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(df):

    print("\nPlotting scale distributions for features...\n")
    plt.figure(figsize=(12, 6))
    sample_features = ['Area', 'Perimeter', 'AspectRation', 'Eccentricity', 'roundness']
    sns.boxplot(data=df[sample_features])
    plt.title("Scaling of Features")
    plt.ylabel("Value Range")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("feature_scale_comparison.png")
    print("\nPlot saved as feature_scale_comparison.png\n")
    plt.close()
