# Load necessary libraries
library(readxl)   # For reading Excel files
library(ggplot2)  # For visualization
library(Amelia)   # For heatmap of missing data

# Step 1: Load the dataset
# Replace the file path with the actual location of your dataset file.
file_path <- "Lecture 1/Detecting Missing Data/Large_Business_Dataset_Missing_Values.xlsx"  # Update with your file path

# Read data from the Excel file
data <- read_excel(file_path)

# Step 2: Display basic information about the dataset
cat("\nDataset Info:\n")
str(data)  # Displays structure (similar to Python's data.info())

# Step 3: Summarize missing data
# Calculate the total number of missing values for each column
cat("\nMissing Data Summary:\n")
missing_summary <- colSums(is.na(data))
print(missing_summary)

# Step 4: Calculate percentage of missing values per column
# Helps to understand the proportion of missing data relative to total rows
cat("\nPercentage of Missing Values:\n")
missing_percentage <- (missing_summary / nrow(data)) * 100
print(missing_percentage)

# Step 5: Visualize missing data with a heatmap
# The heatmap provides a quick visual overview of missing data locations
missmap(data, col = c("yellow", "black"), legend = TRUE, main = "Heatmap of Missing Data")

# Step 6: Visualize missing values as a bar chart (Count per column)
# Bar chart showing total count of missing values per column
missing_data_df <- data.frame(Column = names(missing_summary), MissingCount = missing_summary)

ggplot(missing_data_df, aes(x = reorder(Column, -MissingCount), y = MissingCount)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Count of Missing Values per Column", x = "Columns", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Step 7: Visualize missing values as a bar chart (Percentage per column)
# Bar chart showing percentage of missing values per column
missing_percentage_df <- data.frame(Column = names(missing_percentage), MissingPercentage = missing_percentage)

ggplot(missing_percentage_df, aes(x = reorder(Column, -MissingPercentage), y = MissingPercentage)) +
  geom_bar(stat = "identity", fill = "darkorange") +
  labs(title = "Percentage of Missing Values per Column", x = "Columns", y = "Percentage (%)") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Notes for Students:
# 1. Always inspect the dataset using `str()` to understand its structure and identify missing values.
# 2. Use `colSums(is.na(data))` to quantify missing data.
# 3. Use heatmaps (`missmap()`) and bar charts (`ggplot2`) to visualize missing data patterns.
# 4. Understanding missing data is key to choosing appropriate handling strategies (e.g., imputation or removal).
