import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import os

# Step 1: Load the dataset
# Replace with the correct file path to the dataset
file_path = "Lecture 1/Outlier Detection/Large_Dataset_With_Outliers.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Define the output directory for Isolation Forest results
output_folder = "Lecture 1/Outlier Detection/output/Isolation Forests"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Prepare data for Isolation Forest
# Select numerical columns for analysis, excluding identifiers like "TransactionID"
numerical_columns = [col for col in data.select_dtypes(include=["float64", "int64"]).columns if col != "TransactionID"]
data_for_analysis = data[numerical_columns]

# Step 4: Initialize the Isolation Forest
# Isolation Forest is a machine learning algorithm for identifying anomalies in data
isolation_forest = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)

# Step 5: Fit the Isolation Forest model and predict anomalies
# Predict whether each point is an outlier (-1) or inlier (1)
data["Isolation_Forest_Label"] = isolation_forest.fit_predict(data_for_analysis)

# Step 6: Add an outlier flag
# Mark points as "Outlier" if they are labeled as -1 by the Isolation Forest
data["Outlier_Flag"] = data["Isolation_Forest_Label"].apply(lambda x: "Outlier" if x == -1 else "Normal")

# Step 7: Save detailed outlier information
# Extract rows identified as outliers
outliers = data[data["Outlier_Flag"] == "Outlier"]
outliers_file = os.path.join(output_folder, "Isolation_Forest_Outliers.csv")
outliers.to_csv(outliers_file, index=False)

# Step 8: Save a detailed report
report_file = os.path.join(output_folder, "Isolation_Forest_Report.txt")
with open(report_file, "w") as report:
    report.write("Isolation Forest Outlier Detection Report\n")
    report.write("=" * 50 + "\n\n")
    report.write(f"Number of points analyzed: {len(data)}\n")
    report.write(f"Number of outliers detected: {len(outliers)}\n\n")
    report.write("Columns analyzed:\n")
    for col in numerical_columns:
        report.write(f"- {col}\n")
    report.write("\nOutliers saved to: Isolation_Forest_Outliers.csv\n")

# Step 9: Save the dataset with outlier flags
# Save the full dataset, including outlier labels, to an Excel file
dataset_with_outliers_file = os.path.join(output_folder, "Dataset_with_Isolation_Forest_Outliers.xlsx")
data.to_excel(dataset_with_outliers_file, index=False)

# Final Output Messages
print(f"Outliers detected using Isolation Forest saved to: {outliers_file}")
print(f"Dataset with Isolation Forest labels saved to: {dataset_with_outliers_file}")
print(f"Detailed report saved to: {report_file}")