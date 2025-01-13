import os
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

# Step 1: Load the dataset
# Replace the file path with the actual location of your dataset file.
file_path = "Lecture 1/Data Imputation/KNN Example/KNN_Imputation_Dataset.xlsx"  # Update with the correct file path

data = pd.read_excel(file_path)

# Step 2: Display the first few rows of the dataset
# This provides an overview of the data structure, including missing values.
print("\nOriginal Dataset:")
print(data.head())

# Step 3: Encode categorical variables
# KNNImputer works with numerical data, so categorical variables must be encoded.
encoded_data = data.copy()

# Encoding 'Region', 'IncomeLevel', and 'ProductCategory' using label encoding
# This transforms categorical data into numeric representations.
categorical_columns = ["Region", "IncomeLevel", "ProductCategory"]
for column in categorical_columns:
    encoded_data[column] = encoded_data[column].astype("category").cat.codes

print("\nEncoded Dataset:")
print(encoded_data.head())

# Step 4: Initialize the KNN Imputer
# n_neighbors determines how many nearby data points are used to estimate missing values.
knn_imputer = KNNImputer(n_neighbors=5)

# Step 5: Apply KNN Imputation
# Impute missing values in the dataset.
imputed_data_array = knn_imputer.fit_transform(encoded_data)

# Convert the imputed data back to a DataFrame
imputed_data = pd.DataFrame(imputed_data_array, columns=encoded_data.columns)

# Decode the categorical columns back to their original categories
for column in categorical_columns:
    imputed_data[column] = imputed_data[column].round().astype("int").map(
        dict(enumerate(data[column].astype("category").cat.categories))
    )

# Step 6: Highlight the changes (showing imputed values)
# Identify where missing values were imputed
imputed_values = encoded_data["PurchaseAmount"].isnull()
print("\nImputed Values:")
for idx in encoded_data[imputed_values].index:
    original_row = encoded_data.loc[idx]
    imputed_row = imputed_data.loc[idx]
    print(f"Row {idx + 1}: Original: {original_row['PurchaseAmount']} -> Imputed: {imputed_row['PurchaseAmount']}")

# Step 7: Display the imputed dataset
print("\nImputed Dataset:")
print(imputed_data.head())

# Step 8: Save the imputed dataset to a file
output_folder = "Lecture 1/Data Imputation/KNN Example/output"
os.makedirs(output_folder, exist_ok=True)
output_file_path = os.path.join(output_folder, "Analysed_KNN_Imputed_Dataset.xlsx")
imputed_data.to_excel(output_file_path, index=False)
print(f"\nImputed dataset saved to: {output_file_path}")

# Notes for Students:
# 1. KNN Imputation uses neighboring data points to estimate missing values, ensuring they align with patterns in the data.
# 2. Categorical variables must be encoded into numerical values for KNN to work.
# 3. Always review the imputed dataset to ensure the results make sense in the context of the problem.
# 4. The highlighted imputed values help to understand where and how KNN filled the gaps.
# 5. Adjust the number of neighbors (n_neighbors) to see how it impacts the imputation.

# IMPORTANT: Ensure scikit-learn is correctly installed. Use 'pip install scikit-learn' instead of 'pip install sklearn'.
# The 'sklearn' package is deprecated and will result in an installation error.
# If you encounter issues, refer to https://github.com/scikit-learn/sklearn-pypi-package for detailed guidance.