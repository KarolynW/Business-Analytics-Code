import pandas as pd
import os

# Step 1: Load the dataset
# Replace the file path with the actual location of your dataset file.
file_path = "Lecture 1/Data Imputation/MeanMedian Example/Median_FreshFlow_Sales_Imputation_Dataset.xlsx"  # Update with the correct file path

data = pd.read_excel(file_path)

# Step 2: Check for missing values in the dataset
# Summarize missing data to confirm which columns need imputation.
print("\nMissing Data Before Imputation:")
print(data.isnull().sum())

# Step 3: Perform median imputation
# Replace missing values in the 'SalesRevenue' column with the median of the column.
median_value = data["SalesRevenue"].median()
print(f"\nMedian Value Used for Imputation: {median_value}")

data["SalesRevenue"] = data["SalesRevenue"].fillna(median_value)

# Step 4: Confirm that missing values have been filled
print("\nMissing Data After Imputation:")
print(data.isnull().sum())

# Step 5: Save the imputed dataset to the specified folder
# Ensure the output folder exists; if not, create it.
output_folder = "Lecture 1/Data Imputation/MeanMedian Example/output"
os.makedirs(output_folder, exist_ok=True)

output_file_path = os.path.join(output_folder, "Median_Imputed_Dataset.xlsx")
data.to_excel(output_file_path, index=False)

print(f"\nImputed dataset saved to: {output_file_path}")

# Notes for Students:
# 1. Median imputation is more robust for datasets with outliers as it is not affected by extreme values.
# 2. Always verify the median value before applying it to ensure it aligns with the dataset context.
# 3. After imputation, ensure no missing values remain in the column.
# 4. Save the updated dataset for further analysis or modeling steps.
