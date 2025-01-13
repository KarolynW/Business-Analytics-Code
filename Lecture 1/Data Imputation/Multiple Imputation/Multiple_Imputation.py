import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer  # Needed to use IterativeImputer
from sklearn.impute import IterativeImputer
from colorama import Fore, Style
import os

# Step 1: Load the dataset
# Replace the file path with the actual location of your dataset file.
file_path = "Lecture 1/Data Imputation/Multiple Imputation/RetailCo_Aligned_Imputation_With_Pricing.xlsx"  # Update with the correct file path

data = pd.read_excel(file_path)

# Step 2: Display an overview of the dataset
print(Fore.BLUE + "\nOriginal Dataset:\n" + Style.RESET_ALL)
print(data.head())

# Step 3: Check for missing values
print(Fore.YELLOW + "\nMissing Data Summary:\n" + Style.RESET_ALL)
missing_summary = data.isnull().sum()
print(missing_summary)

# Step 4: Encode categorical variables
# Multiple Imputation works with numerical data, so categorical variables must be encoded.
data_encoded = data.copy()

# Encoding 'Region', 'Month', and 'Product' using label encoding
# This transforms categorical data into numeric representations.
categorical_columns = ["Region", "Month", "Product"]
for column in categorical_columns:
    data_encoded[column] = data_encoded[column].astype("category").cat.codes

print(Fore.GREEN + "\nEncoded Dataset (Ready for Imputation):\n" + Style.RESET_ALL)
print(data_encoded.head())

# Step 5: Initialize the Iterative Imputer (for Multiple Imputation)
# IterativeImputer models each missing value as a function of other features.
iterative_imputer = IterativeImputer(max_iter=10, random_state=42)

# Step 6: Apply Multiple Imputation
print(Fore.CYAN + "\nStarting Multiple Imputation...\n" + Style.RESET_ALL)

# Impute missing values in the dataset
imputed_array = iterative_imputer.fit_transform(data_encoded)

# Convert the imputed data back to a DataFrame
imputed_data = pd.DataFrame(imputed_array, columns=data_encoded.columns)

# Decode the categorical columns back to their original categories
for column in categorical_columns:
    imputed_data[column] = imputed_data[column].round().astype("int").map(
        dict(enumerate(data[column].astype("category").cat.categories))
    )

# Step 7: Highlight the changes (showing imputed values)
print(Fore.MAGENTA + "\nImputed Values:\n" + Style.RESET_ALL)
for column in data.columns:
    if data[column].isnull().sum() > 0:
        print(Fore.YELLOW + f"Column: {column}" + Style.RESET_ALL)
        original_missing = data[column].isnull()
        for idx in data[original_missing].index:
            original_value = data.loc[idx, column]
            imputed_value = imputed_data.loc[idx, column]
            print(f"Row {idx + 1}: Original: {original_value} -> Imputed: {imputed_value}")

# Step 8: Save the imputed dataset
output_folder = "Lecture 1/Data Imputation/Multiple Imputation/output"
os.makedirs(output_folder, exist_ok=True)
output_file_path = os.path.join(output_folder, "Multiple_Imputed_Dataset.xlsx")
imputed_data.to_excel(output_file_path, index=False)

print(Fore.GREEN + f"\nImputed dataset saved to: {output_file_path}\n" + Style.RESET_ALL)

# Notes for Students:
# 1. Multiple Imputation uses iterative modeling to fill missing values, preserving variability and relationships.
# 2. Categorical variables must be encoded for the imputation process.
# 3. Review the imputed values to understand how the imputer filled the gaps.
# 4. IterativeImputer builds multiple models during imputation, making it more robust than simpler techniques.
# 5. Outputs are verbose to explain every step and show exactly how missing values are handled.
