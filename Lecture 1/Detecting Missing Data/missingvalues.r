# Load necessary library
library(readxl)

# Step 1: Load the dataset
# Replace the file path with the actual location of your dataset file.
file_path <- "Lecture 1/Detecting Missing Data/Large_Business_Dataset_Missing_Values.xlsx"  # Update with your file path

# Read data from the Excel file
data <- read_excel(file_path)

# Step 2: Display basic information about the dataset
# This shows the structure of the dataset, including column names and data types.
cat("\nDataset Info:\n")
str(data)

# Step 3: Summarize missing data
# Calculate the total number of missing values for each column.
cat("\nMissing Data Summary:\n")
missing_summary <- colSums(is.na(data))
print(missing_summary)

# Step 4: Calculate percentage of missing values per column
# This helps to understand the proportion of missing data relative to the total number of rows.
cat("\nPercentage of Missing Values:\n")
missing_percentage <- (missing_summary / nrow(data)) * 100
print(missing_percentage)

# Step 5: Create a combined summary table
# Combine the count and percentage of missing values for better insights.
missing_summary_table <- data.frame(
  "Missing Count" = missing_summary,
  "Missing Percentage" = missing_percentage
)

# Display the summary table
cat("\nMissing Data Summary Table:\n")
print(missing_summary_table)

# Notes for Students:
# 1. `is.na(data)` identifies missing values.
# 2. `colSums(is.na(data))` calculates the number of missing entries in each column.
# 3. Calculating percentages helps understand how significant the missing data is.
# 4. A summary table makes it easier to interpret and share insights.
