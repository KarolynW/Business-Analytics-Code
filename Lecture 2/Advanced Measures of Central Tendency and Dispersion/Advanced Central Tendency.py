import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load the dataset
# Replace with the correct file path to the dataset
file_path = "Lecture 2/Advanced Measures of Central Tendency and Dispersion/Advanced_Descriptive_Analysis_Dataset.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Define the output directory for results
output_folder = "Lecture 2/Advanced Measures of Central Tendency and Dispersion/output"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Weighted Mean Calculation
# Weighted Mean is calculated by weighting sales with store sizes
def calculate_weighted_mean(values, weights):
    """
    Calculate the weighted mean.

    Parameters:
        values (Series): The data values.
        weights (Series): The weights for each value.

    Returns:
        float: Weighted mean.
    """
    return np.average(values, weights=weights)

weighted_mean_sales = calculate_weighted_mean(data["Sales"], data["StoreSize"])

# Step 4: Trimmed Mean Calculation
# Trimmed Mean excludes a small percentage of extreme values
def calculate_trimmed_mean(values, trim_percent):
    """
    Calculate the trimmed mean by excluding a percentage of extreme values.

    Parameters:
        values (Series): The data values.
        trim_percent (float): The percentage of values to trim from both ends.

    Returns:
        float: Trimmed mean.
    """
    trimmed_values = values.sort_values().iloc[int(len(values) * trim_percent):-int(len(values) * trim_percent)]
    return trimmed_values.mean()

trimmed_mean_sales = calculate_trimmed_mean(data["Sales"], trim_percent=0.05)

# Step 5: Coefficient of Variation (CV)
# CV is the ratio of the standard deviation to the mean
cv_sales = data["Sales"].std() / data["Sales"].mean() * 100
cv_expenses = data["Expenses"].std() / data["Expenses"].mean() * 100

# Step 6: Visualizing Distribution with Boxplots and Density Plots
# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="Region", y="Sales")
plt.title("Sales Distribution by Region (Boxplot)")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.savefig(os.path.join(output_folder, "Sales_Boxplot.png"))
plt.close()

# Density Plot
plt.figure(figsize=(10, 6))
sns.kdeplot(data["Sales"], label="Sales", fill=True, color="blue", alpha=0.6)
sns.kdeplot(data["Expenses"], label="Expenses", fill=True, color="orange", alpha=0.6)
plt.title("Density Plot for Sales and Expenses")
plt.xlabel("Values")
plt.ylabel("Density")
plt.legend()
plt.savefig(os.path.join(output_folder, "Density_Plot.png"))
plt.close()

# Step 7: Generate a Summary Report
# Create a text file summarizing the analysis
report_file = os.path.join(output_folder, "Descriptive_Analysis_Report.txt")
with open(report_file, "w") as report:
    report.write("Advanced Descriptive Analysis Report\n")
    report.write("=" * 50 + "\n\n")

    # Weighted Mean
    report.write(f"Weighted Mean:\n")
    report.write(f"- Weighted Mean Sales (weighted by StoreSize): {weighted_mean_sales:.2f}\n\n")

    # Trimmed Mean
    report.write(f"Trimmed Mean:\n")
    report.write(f"- Trimmed Mean Sales (5% trimmed): {trimmed_mean_sales:.2f}\n\n")

    # Coefficient of Variation
    report.write(f"Coefficient of Variation (CV):\n")
    report.write(f"- Sales: {cv_sales:.2f}%\n")
    report.write(f"- Expenses: {cv_expenses:.2f}%\n\n")

    # Visualizations
    report.write(f"Visualizations:\n")
    report.write(f"- Sales Boxplot by Region saved as: Sales_Boxplot.png\n")
    report.write(f"- Density Plot for Sales and Expenses saved as: Density_Plot.png\n")

# Final Output Messages
print(f"Analysis complete. Results saved in: {output_folder}")
print(f"Weighted Mean Sales: {weighted_mean_sales:.2f}")
print(f"Trimmed Mean Sales (5% trimmed): {trimmed_mean_sales:.2f}")
print(f"Coefficient of Variation - Sales: {cv_sales:.2f}%, Expenses: {cv_expenses:.2f}%")