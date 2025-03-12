# =========================
# 🛠 HANDLING MISSING DATA TASK - SwiftyRetail (RStudio Version)
# =========================
# This script will guide you step by step through:
# 1. Installing required libraries
# 2. Loading a dataset (You need to fix the file path!)
# 3. Checking for missing data
# 4. Summarizing missing values
# 5. Visualizing missing data using a heatmap and bar charts
# 6. Saving outputs to an "output" folder
# 
# 🚀 YOUR TASK: Identify and fix the missing parts of this script!
# =========================

# ========== Step 1: Install Required Libraries ==========
# 📌 In RStudio, run the following commands **one by one** in the **Console**:
# ---------------------------------
# install.packages("readxl")   # For reading Excel files
# install.packages("ggplot2")  # For data visualization
# install.packages("dplyr")    # For data manipulation
# install.packages("reshape2") # For reshaping data
# install.packages("Amelia")   # For missing data heatmap
# ---------------------------------

# Load required libraries
library(readxl)   # For reading Excel files
library(ggplot2)  # For data visualization
library(dplyr)    # For data manipulation
library(reshape2) # For reshaping data
library(Amelia)   # For missing data heatmap

# ========== Step 2: Set Working Directory ==========
# 📌 Ensure your working directory is correctly set.
# In RStudio, use `getwd()` to check and `setwd("your_directory")` to change if needed.
# Example:
# setwd("C:/Users/YourName/Documents")  # Windows
# setwd("/Users/YourName/Documents")    # Mac

# ========== Step 3: Create an Output Folder ==========
# ✅ Ensure that an "output" folder is created to store saved files.

output_folder <- "output"
if (!dir.exists(output_folder)) {
  dir.create(output_folder)  # Creates the folder if it doesn't exist
  cat("📂 Created output folder:", output_folder, "\n")
}

# ========== Step 4: Load the Dataset ==========
# 🔴 TASK: Replace "your_path_here" with the correct location of your dataset file.

file_path <- "your_path_here/swiftyretail_inventory_sales.xlsx"  # 🔧 FIX ME: Update this!

# Load the dataset using readxl
data <- read_excel(file_path)  # ✅ No error handling needed—RStudio will show an error if the file is missing.
cat("✅ Dataset loaded successfully!\n")

# ========== Step 5: Explore Dataset Structure ==========
# 🔍 Save dataset structure to a text file

dataset_info_file <- file.path(output_folder, "dataset_info.txt")
sink(dataset_info_file)  # Redirect output to a file
str(data)  # Display dataset structure
sink()  # Stop redirecting output

cat("\n🔍 Dataset Info saved to:", dataset_info_file, "\n")

# ========== Step 6: Identify Missing Data ==========
# 📊 Count missing values per column
missing_summary <- colSums(is.na(data))
missing_summary <- missing_summary[missing_summary > 0]  # Only show columns with missing values

# Save missing data summary to CSV
missing_summary_file <- file.path(output_folder, "missing_data_summary.csv")
write.csv(data.frame(Column = names(missing_summary), Missing_Count = missing_summary),
          missing_summary_file, row.names = FALSE)

cat("\n🛑 Missing Data Summary saved to:", missing_summary_file, "\n")

# ========== Step 7: Calculate Missing Data Percentage ==========
# 📉 Calculate the percentage of missing values.

missing_percentage <- (missing_summary / nrow(data)) * 100

# Save missing data percentage to CSV
missing_percentage_file <- file.path(output_folder, "missing_data_percentage.csv")
write.csv(data.frame(Column = names(missing_percentage), Missing_Percentage = missing_percentage),
          missing_percentage_file, row.names = FALSE)

cat("\n📉 Percentage of Missing Values saved to:", missing_percentage_file, "\n")

# ========== Step 8: Visualizing Missing Data ==========
# TASK: Fix the commented-out line to show missing values in a different color.

png(file.path(output_folder, "missing_data_heatmap.png"))
missmap(data, col = c("yellow", "black"), legend = TRUE)
title("Heatmap of Missing Data")
dev.off()

cat("🖼 Heatmap saved to:", file.path(output_folder, "missing_data_heatmap.png"), "\n")

# ========== Step 9: Bar Chart of Missing Values ==========
# TASK: Fix the bar chart labels and title for better clarity.

missing_data_df <- data.frame(Column = names(missing_summary), Missing_Count = missing_summary)

png(file.path(output_folder, "missing_data_count.png"))
ggplot(missing_data_df, aes(x = reorder(Column, -Missing_Count), y = Missing_Count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "FIX ME: Missing Values Count", x = "FIX ME: What is on this axis?", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
dev.off()

cat("🖼 Bar Chart (Count) saved to:", file.path(output_folder, "missing_data_count.png"), "\n")

# ========== Step 10: Bar Chart of Missing Percentages ==========
# TASK: Fix the title to better describe what is being shown.

missing_percentage_df <- data.frame(Column = names(missing_percentage), Missing_Percentage = missing_percentage)

png(file.path(output_folder, "missing_data_percentage.png"))
ggplot(missing_percentage_df, aes(x = reorder(Column, -Missing_Percentage), y = Missing_Percentage)) +
  geom_bar(stat = "identity", fill = "darkorange") +
  labs(title = "FIX ME: Percentage of What?", x = "Column", y = "Percentage (%)") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
dev.off()

cat("🖼 Bar Chart (Percentage) saved to:", file.path(output_folder, "missing_data_percentage.png"), "\n")

# =========================
# 🚀 TASKS FOR STUDENTS:
# 1. **Fix the file path** to load the dataset correctly.
# 2. **Fix the heatmap color scale** for better contrast.
# 3. **Update the bar chart titles and axis labels** to make them clearer.
# 4. **Run the script and ensure all outputs are saved in the "output" folder**.
# 5. **Verify that CSV summaries and image files are created correctly**.
# =========================

# =========================
# ✅ CORRECT ANSWERS:
# =========================

# 1. **Fixing the File Path**
# Update this line with the correct location of your dataset:
# file_path <- "C:/Users/YourName/Documents/swiftyretail_inventory_sales.xlsx"

# 2. **Fixing the Bar Chart Titles and Labels**
# - Replace:
# ggplot(missing_data_df, aes(x = reorder(Column, -Missing_Count), y = Missing_Count)) +
#   labs(title = "FIX ME: Missing Values Count", x = "FIX ME: What is on this axis?", y = "Count")
# With:
# ggplot(missing_data_df, aes(x = reorder(Column, -Missing_Count), y = Missing_Count)) +
#   labs(title = "Count of Missing Values per Column", x = "Columns", y = "Number of Missing Entries")

# - Replace:
# ggplot(missing_percentage_df, aes(x = reorder(Column, -Missing_Percentage), y = Missing_Percentage)) +
#   labs(title = "FIX ME: Percentage of What?")
# With:
# ggplot(missing_percentage_df, aes(x = reorder(Column, -Missing_Percentage), y = Missing_Percentage)) +
#   labs(title = "Percentage of Missing Values per Column")

# =========================
# 🎯 FINAL TASK:
# Run your fixed script and check the "output" folder for saved results. 🚀
# =========================
