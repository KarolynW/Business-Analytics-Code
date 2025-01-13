#Libraries required for this code - libraries can be installed using pip install <library_name>
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
# Replace the file path with the actual location of your dataset file.
# Ensure the dataset contains missing values for meaningful analysis.
# Watch the file format (Excel, CSV, etc.) while using the read function. 
file_path = "Lecture 1/Detcting Missing Data/Large_Business_Dataset_Missing_Values.xlsx"  # Update with your file path

data = pd.read_excel(file_path)

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

# Step 5: Visualize missing data with a heatmap
# The heatmap provides a quick visual overview of where missing values are located in the dataset.
plt.figure(figsize=(12, 8))  # Set the figure size for better readability
sns.heatmap(data.isnull(), cbar=False, cmap="viridis")  # Use a color map to highlight missing values
plt.title("Heatmap of Missing Data")  # Add a title for context
plt.show()

# Step 6: Visualize missing values as a bar chart (Count per column)
# This bar chart shows the total count of missing values for each column.
plt.figure(figsize=(10, 6))  # Adjust the figure size for clarity
missing_summary.plot(kind="bar", color="steelblue")  # Use bar plot to represent counts
plt.title("Count of Missing Values per Column")  # Title to explain the visualization
plt.ylabel("Count")  # Label for y-axis
plt.xlabel("Columns")  # Label for x-axis
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.tight_layout()  # Ensure everything fits within the figure
plt.show()

# Step 7: Visualize missing values as a bar chart (Percentage per column)
# This bar chart shows the percentage of missing values for each column.
plt.figure(figsize=(10, 6))  # Adjust the figure size for clarity
missing_percentage.plot(kind="bar", color="darkorange")  # Use bar plot to represent percentages
plt.title("Percentage of Missing Values per Column")  # Title to explain the visualization
plt.ylabel("Percentage (%)")  # Label for y-axis
plt.xlabel("Columns")  # Label for x-axis
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.tight_layout()  # Ensure everything fits within the figure
plt.show()

# Notes for Students:
# 1. Always inspect the dataset using methods like `info()` to understand its structure and identify missing values.
# 2. Use summary statistics (`isnull().sum()`) to quantify missing data.
# 3. Visualizations like heatmaps and bar charts are powerful tools for identifying patterns in missing data.
# 4. Understanding missing data is the first step in determining the appropriate strategy for handling it (e.g., imputation or removal).