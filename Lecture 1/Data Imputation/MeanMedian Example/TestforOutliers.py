import pandas as pd
import numpy as np

# Step 1: Load the dataset
# Replace the file path with the actual location of your dataset file.
file_path = "Lecture 1/Data Imputation/MeanMedian Example/Median_FreshFlow_Sales_Imputation_Dataset.xlsx"  # Update with the correct file path

data = pd.read_excel(file_path)

# Step 2: Display basic information about the dataset
# Provides an overview of the dataset structure, including column names, data types, and non-null counts.
print("\nDataset Info:")
data.info()

# Step 3: Describe the dataset
# Use the describe() method to calculate summary statistics, such as mean, median, min, max, and percentiles.
print("\nSummary Statistics:")
descriptive_stats = data["SalesRevenue"].describe()
print(descriptive_stats)

# Step 4: Check for missing values
# Summarize missing data to understand its extent in the dataset.
print("\nMissing Data Count:")
missing_count = data["SalesRevenue"].isnull().sum()
print(f"Missing values in SalesRevenue: {missing_count}")

# Step 5: Detect extreme values (outliers)
# Calculate the Interquartile Range (IQR) to identify potential outliers.
Q1 = data["SalesRevenue"].quantile(0.25)  # First quartile (25th percentile)
Q3 = data["SalesRevenue"].quantile(0.75)  # Third quartile (75th percentile)
IQR = Q3 - Q1  # Interquartile range

# Define bounds for identifying outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Count the number of outliers
outliers = data[(data["SalesRevenue"] < lower_bound) | (data["SalesRevenue"] > upper_bound)]
print("\nOutlier Detection:")
print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
print(f"Number of Outliers: {len(outliers)}")

# Step 6: Analyze the suitability of mean vs. median
# If there are significant outliers, the mean will be heavily influenced, and median is preferred.
if len(outliers) > 0:
    print("\nRecommendation:")
    print("The dataset contains significant outliers. Median imputation is recommended as it is more robust to extreme values.")
else:
    print("\nRecommendation:")
    print("The dataset does not contain significant outliers. Mean imputation can be used for this dataset.")

# Step 7: Output the mean and median for reference
mean_value = data["SalesRevenue"].mean()
median_value = data["SalesRevenue"].median()

print("\nMean and Median Values:")
print(f"Mean SalesRevenue: {mean_value}")
print(f"Median SalesRevenue: {median_value}")

# Notes for Students:
# 1. Outliers can distort the mean significantly, making the median a better choice for imputation.
# 2. Use IQR to identify the range of typical values and detect extreme deviations.
# 3. Always inspect summary statistics and outlier counts before deciding on the imputation method.
# 4. Missing value analysis helps gauge the extent of data cleaning required.
