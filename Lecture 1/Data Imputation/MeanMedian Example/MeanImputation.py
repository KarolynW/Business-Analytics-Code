import pandas as pd
import os

# Step 1: Load the dataset
# Replace the file path with the actual location of your dataset file.
file_path = "Median_FreshFlow_Sales_Imputation_Dataset.xlsx"  # Update with the correct file path

data = pd.read_excel(file_path)

# Step 2: Check for missing values in the dataset
# Summarize missing data to confirm which columns need imputation.
print("\nMissing Data Before Imputation:")
print(data.isnull().sum())

# Step 3: Perform mean imputation
# Replace missing values in the 'SalesRevenue' column with the mean of the column.
mean_value = data["SalesRevenue"].mean()
print(f"\nMean Value Used for Imputation: {mean_value}")

data["SalesRevenue"] = data["SalesRevenue"].fillna(mean_value)

# Step 4: Confirm that missing values have been filled
print("\nMissing Data After Imputation:")
print(data.isnull().sum())

# Step 5: Save the imputed dataset to the specified folder
# Ensure the output folder exists; if not, create it.
output_folder = "Lecture 1/Data Imputation/MeanMedian Example/output"
os.makedirs(output_folder, exist_ok=True)

output_file_path = os.path.join(output_folder, "Mean_Imputed_Dataset.xlsx")
data.to_excel(output_file_path, index=False)

print(f"\nImputed dataset saved to: {output_file_path}")

# Notes for Students:
# 1. Mean imputation is a simple method suitable for datasets without significant outliers.
# 2. Always verify the mean value before applying it to ensure it aligns with the dataset context.
# 3. After imputation, ensure no missing values remain in the column.
# 4. Save the updated dataset for further analysis or modeling steps.