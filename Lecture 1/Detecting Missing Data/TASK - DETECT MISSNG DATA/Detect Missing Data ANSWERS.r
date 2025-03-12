# =========================
# 🛠 COMPLETE HANDLING MISSING DATA SCRIPT - SwiftyRetail (WITH SAVED OUTPUTS)
# =========================
# This script will:
# 1. Install and load required libraries
# 2. Load a dataset (You need to update the file path!)
# 3. Check and summarize missing data
# 4. Visualize missing data using a heatmap and bar charts
# 5. Save outputs (CSV files, images) in an "output" folder
# =========================

# ========== Step 1: Install Required Libraries ==========
# 📌 In RStudio, run the following **one by one** in the Console:
# ---------------------------------
# install.packages("readxl")    # For reading Excel files
# install.packages("ggplot2")   # For data visualization
# install.packages("dplyr")     # For data manipulation
# install.packages("reshape2")  # For reshaping data
# install.packages("Amelia")    # For missing data heatmap
# ---------------------------------

# Load required libraries
library(readxl)   # Reading Excel files
library(ggplot2)  # Data visualization
library(dplyr)    # Data manipulation
library(reshape2) # Reshaping data
library(Amelia)   # Heatmap for missing data

# ========== Step 2: Set Working Directory ==========
# 📌 Ensure the correct working directory is set in RStudio.
# Use `getwd()` to check and `setwd("your_directory")` to change if needed.
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
# ✅ Update the file path below with the actual location of your dataset

file_path <- "Lecture 1/Detecting Missing Data/TASK - DETECT MISSNG DATA/swiftyretail_inventory_sales.xlsx"  # 🔧 FIX ME: Update this!

# Load the dataset using readxl
data <- read_excel(file_path)  # ✅ If the file is missing, RStudio will display an error.
cat("✅ Dataset loaded successfully!\n")

# ========== Step 5: Explore Dataset Structure ==========
# 🔍 Save dataset information to a text file

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
# 🔥 Heatmap of missing values

png(file.path(output_folder, "missing_data_heatmap.png"))
missmap(data, col = c("yellow", "black"), legend = TRUE)
title("Heatmap of Missing Data")
dev.off()

cat("🖼 Heatmap saved to:", file.path(output_folder, "missing_data_heatmap.png"), "\n")

# ========== Step 9: Bar Chart of Missing Values ==========
# 📊 Bar chart showing missing data counts

missing_data_df <- data.frame(Column = names(missing_summary), Missing_Count = missing_summary)

png(file.path(output_folder, "missing_data_count.png"))
ggplot(missing_data_df, aes(x = reorder(Column, -Missing_Count), y = Missing_Count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Count of Missing Values per Column", x = "Columns", y = "Number of Missing Entries") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
dev.off()

cat("🖼 Bar Chart (Count) saved to:", file.path(output_folder, "missing_data_count.png"), "\n")

# ========== Step 10: Bar Chart of Missing Percentages ==========
# 📊 Bar chart showing missing data percentages

missing_percentage_df <- data.frame(Column = names(missing_percentage), Missing_Percentage = missing_percentage)

png(file.path(output_folder, "missing_data_percentage.png"))
ggplot(missing_percentage_df, aes(x = reorder(Column, -Missing_Percentage), y = Missing_Percentage)) +
  geom_bar(stat = "identity", fill = "darkorange") +
  labs(title = "Percentage of Missing Values per Column", x = "Column", y = "Percentage (%)") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
dev.off()

cat("🖼 Bar Chart (Percentage) saved to:", file.path(output_folder, "missing_data_percentage.png"), "\n")

# =========================
# ✅ SCRIPT COMPLETED SUCCESSFULLY! ALL OUTPUTS SAVED.
# =========================
