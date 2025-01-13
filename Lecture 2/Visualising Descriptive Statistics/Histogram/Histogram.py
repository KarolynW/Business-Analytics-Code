import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load the dataset
# Replace with the correct file path to the dataset
file_path = "Lecture 2/Visualising Descriptive Statistics/Histogram/Histogram_Customization_Dataset.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Define the output directory for results
output_folder = "Lecture 2/Visualising Descriptive Statistics/Histogram/output"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Histogram Customizations
# Create histograms for each relevant column with density curves and different binning strategies

# Function to create a histogram with a density curve
def create_histogram_with_density(data, column, bins, color, title, xlabel, ylabel, output_path):
    """
    Creates a histogram with an overlaid density curve and saves it as an image.

    Parameters:
        data (DataFrame): The dataset.
        column (str): Column name for the histogram.
        bins (int): Number of bins for the histogram.
        color (str): Color of the histogram bars.
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
        output_path (str): File path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=bins, kde=True, color=color, label="Density Curve")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.savefig(output_path)
    plt.close()

# Create histograms for specific columns
columns_to_visualize = ["Age", "AnnualIncome", "SpendingScore", "PurchaseFrequency"]

# Generate visualizations for each column
for column in columns_to_visualize:
    # Default histogram with 10 bins
    create_histogram_with_density(
        data,
        column,
        bins=10,
        color="blue",
        title=f"Default Histogram for {column}",
        xlabel=column,
        ylabel="Frequency",
        output_path=os.path.join(output_folder, f"{column}_Default_Histogram.png")
    )

    # Customized histogram with 20 bins
    create_histogram_with_density(
        data,
        column,
        bins=20,
        color="green",
        title=f"Histogram for {column} with 20 Bins",
        xlabel=column,
        ylabel="Frequency",
        output_path=os.path.join(output_folder, f"{column}_20Bins_Histogram.png")
    )

    # Customized histogram with 50 bins
    create_histogram_with_density(
        data,
        column,
        bins=50,
        color="orange",
        title=f"Histogram for {column} with 50 Bins",
        xlabel=column,
        ylabel="Frequency",
        output_path=os.path.join(output_folder, f"{column}_50Bins_Histogram.png")
    )

# Step 4: Generate a Report
# Summarize the histogram customizations in a report
report_file = os.path.join(output_folder, "Histogram_Report.txt")
with open(report_file, "w") as report:
    report.write("Histogram Customization Report\n")
    report.write("=" * 50 + "\n\n")
    report.write("Visualizations have been created for the following columns:\n")
    for column in columns_to_visualize:
        report.write(f"- {column}\n")
    report.write("\n")
    report.write("For each column, the following customizations were applied:\n")
    report.write("1. Default histogram with 10 bins.\n")
    report.write("2. Histogram with 20 bins.\n")
    report.write("3. Histogram with 50 bins.\n")
    report.write("\nAll visualizations have been saved in the output folder.\n")

# Step 5: Final Output Message
print(f"Histogram visualizations and report saved in: {output_folder}")