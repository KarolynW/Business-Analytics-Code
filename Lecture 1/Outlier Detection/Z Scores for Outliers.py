import pandas as pd
import numpy as np
import os

# Step 1: Load the dataset
# Replace with the correct file path to the dataset
file_path = "Lecture 1/Outlier Detection/Outlier_Detection_Dataset.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Define the output directory for Z-Score results
output_folder = "Lecture 1/Outlier Detection/output/Z Scores"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Function to calculate Z-Scores
def calculate_z_scores(column):
    """
    Calculate Z-Scores for a numerical column.

    Parameters:
        column (str): The column name to calculate Z-Scores for.

    Returns:
        z_scores (Series): Z-Scores for the column.
    """
    mean = data[column].mean()  # Calculate the mean
    std_dev = data[column].std()  # Calculate the standard deviation

    # Avoid division by zero if the standard deviation is zero
    if std_dev == 0:
        print(f"Standard deviation for {column} is zero. Z-Scores cannot be calculated.")
        return pd.Series([np.nan] * len(data), index=data.index)

    # Compute Z-Scores
    z_scores = (data[column] - mean) / std_dev

    return z_scores

# Step 4: Process numerical columns
# Select only numerical columns, excluding identifiers like "ID"
numerical_columns = [col for col in data.select_dtypes(include=["float64", "int64"]).columns if col != "ID"]

# Initialize a report file to store results
report_file = os.path.join(output_folder, "Z_Score_Report.txt")
with open(report_file, "w") as report:
    report.write("Z-Score Analysis Report\n")
    report.write("=" * 50 + "\n\n")

    # Iterate over numerical columns to calculate Z-Scores
    for column in numerical_columns:
        print(f"Processing column: {column}")

        # Calculate Z-Scores
        z_scores = calculate_z_scores(column)

        # Add Z-Scores to the dataset
        data[f"{column}_Z_Score"] = z_scores

        # Identify outliers based on Z-Scores
        outliers = data[np.abs(z_scores) > 3]

        # Save outliers to a CSV file
        outliers_file = os.path.join(output_folder, f"{column}_Z_Score_Outliers.csv")
        outliers.to_csv(outliers_file, index=False)

        # Write detailed information to the report
        mean = data[column].mean()
        std_dev = data[column].std()
        report.write(f"Column: {column}\n")
        report.write(f"- Mean: {mean}\n")
        report.write(f"- Standard Deviation: {std_dev}\n")
        report.write(f"- Number of Outliers (Z > |3|): {len(outliers)}\n")
        report.write(f"- Outliers saved to: {outliers_file}\n\n")

        print(f"Outliers for {column} saved to {outliers_file}")

# Step 5: Save the updated dataset with Z-Scores
# Include the Z-Score columns in the final dataset
z_scores_file = os.path.join(output_folder, "Dataset_with_Z_Scores.xlsx")
data.to_excel(z_scores_file, index=False)

print(f"Dataset with Z-Scores saved to {z_scores_file}")
print(f"Z-Score analysis complete. Detailed report saved to {report_file}")