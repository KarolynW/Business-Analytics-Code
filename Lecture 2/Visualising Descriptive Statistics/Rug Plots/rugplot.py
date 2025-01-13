import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Step 1: Load the dataset
# Replace with the correct file path to the dataset
file_path = "Lecture 2/Visualising Descriptive Statistics/Rug Plots/Rug_Plot_Demo_Dataset.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Define the output directory for results
output_folder = "Lecture 2/Visualising Descriptive Statistics/Rug Plots/output"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Function to create rug plots
# Rug plots visualize the distribution of data along a specific axis

def create_rug_plot(data, column, title, xlabel, output_path):
    """
    Creates a rug plot for a given column and saves it as an image.

    Parameters:
        data (DataFrame): The dataset.
        column (str): Column name for the rug plot.
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis.
        output_path (str): File path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data[column], fill=True, color="blue", alpha=0.6, label="Density")
    sns.rugplot(data[column], color="red", height=0.1, alpha=0.7, label="Rug Plot")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Density")
    plt.legend()
    plt.savefig(output_path)
    plt.close()

# Step 4: Create rug plots for specific columns
columns_to_visualize = ["PurchaseAmount", "Age", "SpendingScore"]

for column in columns_to_visualize:
    plot_title = f"Rug Plot and Density for {column}"
    xlabel = column
    output_path = os.path.join(output_folder, f"{column}_Rug_Plot.png")

    create_rug_plot(
        data, column, title=plot_title, xlabel=xlabel, output_path=output_path
    )

# Step 5: Generate a Report
# Summarize the rug plot visualizations in a report
report_file = os.path.join(output_folder, "Rug_Plot_Report.txt")
with open(report_file, "w") as report:
    report.write("Rug Plot Visualization Report\n")
    report.write("=" * 50 + "\n\n")
    report.write("Rug plots have been created for the following columns:\n")
    for column in columns_to_visualize:
        report.write(f"- {column}\n")
    report.write("\n")
    report.write("Each plot includes a density curve and rug plot to visualize the distribution of data.\n")
    report.write(f"Visualizations have been saved in the output folder: {output_folder}\n")

# Final Output Message
print(f"Rug plot visualizations and report saved in: {output_folder}")
