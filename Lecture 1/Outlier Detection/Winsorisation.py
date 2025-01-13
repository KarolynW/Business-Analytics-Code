import pandas as pd
import numpy as np
import os

# Step 1: Load the dataset
# Replace with the correct file path to the dataset
file_path = "Lecture 1/Outlier Detection/Large_Dataset_With_Outliers.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Define the output directory for Winsorisation results
output_folder = "Lecture 1/Outlier Detection/output/Winsorisation"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Function to apply Winsorisation
def apply_winsorisation(column, lower_percentile=0.05, upper_percentile=0.95):
    """
    Apply Winsorisation to cap outliers at specified percentiles.

    Parameters:
        column (str): The column name to Winsorise.
        lower_percentile (float): Lower percentile for capping (default is 5%).
        upper_percentile (float): Upper percentile for capping (default is 95%).

    Returns:
        winsorised_column (Series): Column with Winsorised values.
    """
    lower_bound = data[column].quantile(lower_percentile)  # Calculate lower bound
    upper_bound = data[column].quantile(upper_percentile)  # Calculate upper bound

    # Apply Winsorisation by capping values
    winsorised_column = data[column].clip(lower=lower_bound, upper=upper_bound)

    return winsorised_column, lower_bound, upper_bound

# Step 4: Process numerical columns
# Select only numerical columns, excluding identifiers like "TransactionID"
numerical_columns = [col for col in data.select_dtypes(include=["float64", "int64"]).columns if col != "TransactionID"]

# Initialize a report file to store results
report_file = os.path.join(output_folder, "Winsorisation_Report.txt")
with open(report_file, "w") as report:
    report.write("Winsorisation Analysis Report\n")
    report.write("=" * 50 + "\n\n")

    # Iterate over numerical columns to apply Winsorisation
    for column in numerical_columns:
        print(f"Processing column: {column}")

        # Apply Winsorisation
        winsorised_column, lower, upper = apply_winsorisation(column)

        # Add Winsorised column to the dataset
        data[f"{column}_Winsorised"] = winsorised_column

        # Write detailed information to the report
        report.write(f"Column: {column}\n")
        report.write(f"- Lower Bound (capped at {lower * 100:.2f}%): {lower}\n")
        report.write(f"- Upper Bound (capped at {upper * 100:.2f}%): {upper}\n")
        report.write(f"- Number of values capped at lower bound: {(data[column] < lower).sum()}\n")
        report.write(f"- Number of values capped at upper bound: {(data[column] > upper).sum()}\n")
        report.write("\n")

        print(f"Winsorisation applied to {column}. Bounds: [{lower}, {upper}]")

# Step 5: Save the updated dataset with Winsorised columns
# Include the Winsorised columns in the final dataset
winsorised_file = os.path.join(output_folder, "Dataset_with_Winsorisation.xlsx")
data.to_excel(winsorised_file, index=False)

print(f"Dataset with Winsorisation saved to {winsorised_file}")
print(f"Winsorisation analysis complete. Detailed report saved to {report_file}")