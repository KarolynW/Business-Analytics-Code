import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load the dataset
# Load the dataset containing numerical and categorical data.
# Ensure the file path points to the correct location of your dataset.
file_path = "Lecture 1/Outlier Detection/Outlier_Detection_Dataset.xlsx"  # Replace with the correct path if needed
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Create a folder to save the output files, such as plots and labeled datasets.
output_folder = "Lecture 1/Outlier Detection/output/Scatterplots"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Scatterplot function to identify outliers visually
def plot_scatter_with_outliers(x_column, y_column):
    """
    Plot a scatterplot to visualize relationships between two variables
    and highlight potential outliers.

    Parameters:
        x_column (str): The name of the x-axis column.
        y_column (str): The name of the y-axis column.

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_column, y=y_column, hue="Region", style="Region", palette="muted")

    # Annotate potential outliers (extreme points visually)
    for i in range(len(data)):
        x = data[x_column].iloc[i]
        y = data[y_column].iloc[i]
        # Highlight if points are unusually high or low (simple rule)
        if y > data[y_column].quantile(0.95) or y < data[y_column].quantile(0.05):
            plt.text(x, y, f"ID {data['ID'].iloc[i]}", color="red", fontsize=9, ha="center")

    # Add titles and labels
    plt.title(f"Scatterplot of {x_column} vs {y_column} with Outliers Highlighted")
    plt.xlabel(x_column)
    plt.ylabel(y_column)

    # Save the plot
    plot_file = os.path.join(output_folder, f"{x_column}_vs_{y_column}_Scatterplot.png")
    plt.savefig(plot_file)
    plt.close()
    print(f"Scatterplot saved to {plot_file}")

# Step 4: Define pairs of columns to plot
# Select numerical columns for scatterplot analysis
numerical_columns = [col for col in data.select_dtypes(include=["float64", "int64"]).columns if col != "ID"]
column_pairs = [(numerical_columns[i], numerical_columns[j]) for i in range(len(numerical_columns)) for j in range(i + 1, len(numerical_columns))]

# Step 5: Generate scatterplots for each pair
for x_col, y_col in column_pairs:
    print(f"Creating scatterplot for {x_col} vs {y_col}")
    plot_scatter_with_outliers(x_col, y_col)

print("Scatterplot analysis complete. Results saved in the Lecture 1\Outlier Detection\output\Scatterplots.")