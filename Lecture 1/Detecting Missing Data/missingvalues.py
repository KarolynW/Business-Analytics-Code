import pandas as pd

# Step 1: Load the dataset
# Replace the file path with the actual location of your dataset file.
file_path = r"Lecture 1\Detecting Missing Data\Large_Business_Dataset_Missing_Values.xlsx"  # Use raw string (r"") for Windows paths

# Alternative: Use double backslashes if not using raw string
# file_path = "Lecture 1\\Detecting Missing Data\\Large_Business_Dataset_Missing_Values.xlsx"

# Load Excel file using pandas
data = pd.read_excel(file_path, engine="openpyxl")  # Ensure 'openpyxl' is used for .xlsx files

# Step 2: Display basic information about the dataset
# This will show the structure of the dataset, including column names, data types, and non-null counts.
print("\nDataset Info:")
data.info()

# Step 3: Summarize missing data
# Calculate the total number of missing values for each column.
print("\nMissing Data Summary:")
missing_summary = data.isnull().sum()
print(missing_summary)

# Step 4: Calculate percentage of missing values per column
# This helps to understand the proportion of missing data relative to the total number of rows.
print("\nPercentage of Missing Values:")
missing_percentage = (missing_summary / len(data)) * 100
print(missing_percentage)

# Step 5: Create a combined summary table
# Combine the count and percentage of missing values for better insights.
missing_summary_table = pd.DataFrame({
    "Missing Count": missing_summary,
    "Missing Percentage": missing_percentage
})

# Display the summary table
print("\nMissing Data Summary Table:")
print(missing_summary_table)

# Notes for Students:
# 1. The `isnull().sum()` function helps quantify the number of missing entries in each column.
# 2. Calculating percentages provides context for how significant the missing data is relative to the dataset size.
# 3. Summarizing this information in a table makes it easier to interpret and share insights with others.
