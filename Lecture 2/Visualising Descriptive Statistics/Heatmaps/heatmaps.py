import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Step 1: Load the dataset
# Replace with the correct file path to the dataset
file_path = "Lecture 2/Visualising Descriptive Statistics/Heatmaps/Heatmap_Demo_Dataset.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Define the output directory for results
output_folder = "Lecture 2/Visualising Descriptive Statistics/Heatmaps/output"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Calculate Correlation Matrix
# Correlation matrix shows the relationships between numeric variables in the dataset
correlation_matrix = data.corr()

# Save the correlation matrix to a file for reference
correlation_file = os.path.join(output_folder, "Correlation_Matrix.csv")
correlation_matrix.to_csv(correlation_file)

# Step 4: Create a Heatmap
# Heatmaps visually represent the correlation matrix with color gradients to indicate strength and direction

def create_heatmap(matrix, title, output_path):
    """
    Creates a heatmap from a correlation matrix and saves it as an image.

    Parameters:
        matrix (DataFrame): Correlation matrix or data to visualize.
        title (str): Title of the heatmap.
        output_path (str): File path to save the heatmap image.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        matrix, 
        annot=True,  # Show correlation values in cells
        fmt=".2f",  # Format numbers to 2 decimal places
        cmap="coolwarm",  # Color map for heatmap
        vmin=-1, vmax=1,  # Set fixed color range
        linewidths=0.5,  # Add grid lines between cells
    )
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# Generate the heatmap for correlation matrix
heatmap_path = os.path.join(output_folder, "Correlation_Heatmap.png")
create_heatmap(correlation_matrix, "Correlation Heatmap", heatmap_path)

# Step 5: Generate a Report
# Summarize findings in the heatmap and save it as a text file
report_file = os.path.join(output_folder, "Heatmap_Report.txt")
with open(report_file, "w") as report:
    report.write("Heatmap Visualization Report\n")
    report.write("=" * 50 + "\n\n")
    report.write("Correlation Matrix:\n")
    report.write("=" * 50 + "\n")
    report.write(correlation_matrix.to_string())
    report.write("\n\n")
    report.write("Key Insights:\n")
    report.write("- Positive correlations (close to 1) indicate strong direct relationships.\n")
    report.write("- Negative correlations (close to -1) indicate strong inverse relationships.\n")
    report.write("- Values near 0 indicate weak or no linear relationship.\n\n")
    report.write(f"Heatmap image saved as: {heatmap_path}\n")

# Final Output Message
print(f"Heatmap visualizations and report saved in: {output_folder}")
print(f"Correlation matrix saved to: {correlation_file}")