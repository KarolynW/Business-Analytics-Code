# =========================
# 🏭 DATA IMPUTATION TASK - Olympus Manufacturing
# =========================
# This script will guide you through:
# 1. Loading the dataset (You need to fix the file path!)
# 2. Summarizing missing values (Use what you learned in the previous task!)
# 3. Applying different imputation techniques
# 4. Saving the imputed dataset for analysis
#
# 🚀 YOUR TASK: Identify and fix the missing parts of this script!
# =========================

# ========== Step 1: Install Required Libraries ==========
# In RStudio, run these commands in the console **one by one** to install missing libraries:
# ---------------------------------
# install.packages("dplyr")   # For data manipulation
# install.packages("ggplot2") # For visualization
# install.packages("VIM")     # For KNN-based imputation
# install.packages("mice")    # For multiple imputation
# ---------------------------------

# ========== Step 2: Load Required Libraries ==========
library(dplyr)  # For data manipulation
library(ggplot2)  # For visualization
library(VIM)  # For KNN Imputation
library(mice)  # For Multiple Imputation

# ========== Step 3: Create an Output Folder ==========
# ✅ Ensure that an "output" folder is created to store saved files.
output_folder <- "output"
if (!dir.exists(output_folder)) {
  dir.create(output_folder)
  print(paste("📂 Created output folder:", output_folder))
}

# ========== Step 4: Load the Dataset ==========
# 🔴 TASK: Replace "your_path_here" with the correct location of your dataset file.
file_path <- "your_path_here/olympus_manufacturing_realistic_missing_data.csv"  # 🔧 FIX ME: Update this!

# Load the dataset using read.csv()
data <- tryCatch(
  read.csv(file_path, stringsAsFactors = FALSE),
  error = function(e) {
    print("❌ ERROR: The file was not found! Please check the file path and try again.")
    quit(save = "no")
  }
)
print("✅ Dataset loaded successfully!")

# ========== Step 5: Explore Dataset Structure ==========
# 🔍 Save dataset structure to a text file
dataset_info_file <- file.path(output_folder, "dataset_info.txt")
sink(dataset_info_file)  # Redirect output to file
str(data)  # Show dataset structure
sink()  # Stop redirecting output

print(paste("\n🔍 Dataset Info saved to:", dataset_info_file))

# ========== Step 6: Identify Missing Data ==========
# 📊 TASK: Use the skills from the previous task to summarize missing values!
# - Count missing values per column
# - Calculate the percentage of missing values

print("\n🛑 Missing Data Summary:")
missing_summary <- colSums(is.na(data))
print(missing_summary[missing_summary > 0])  # Only show columns with missing values

# 📉 TASK: Calculate the percentage of missing values
missing_percentage <- (missing_summary / nrow(data)) * 100
print("\n📉 Percentage of Missing Values:")
print(missing_percentage[missing_percentage > 0])  # Show only affected columns

# Save missing data summary
missing_summary_file <- file.path(output_folder, "missing_data_summary.csv")
write.csv(data.frame(Column = names(missing_summary), Missing_Count = missing_summary, Missing_Percentage = missing_percentage), missing_summary_file, row.names = FALSE)
print(paste("\n✅ Missing Data Summary saved to:", missing_summary_file))

# ========== Step 7: Apply Mean/Median Imputation ==========
# 🚀 TASK: Implement Mean/Median Imputation for numerical columns

# Copy the dataset to preserve the original
imputed_data <- data

# 🔧 FIX ME: Choose either mean or median imputation for "Production Cost Per Unit" and "Defect Rate"
imputed_data$Production_Cost_Per_Unit[is.na(imputed_data$Production_Cost_Per_Unit)] <- mean(imputed_data$Production_Cost_Per_Unit, na.rm = TRUE)  # Mean Imputation
imputed_data$Defect_Rate[is.na(imputed_data$Defect_Rate)] <- median(imputed_data$Defect_Rate, na.rm = TRUE)  # Median Imputation

# ========== Step 8: Apply KNN Imputation ==========
# 🚀 TASK: Implement KNN Imputation for missing values in the dataset.

# Perform KNN imputation with k=3
knn_imputed_data <- kNN(imputed_data, k = 3)

# Save the KNN-imputed dataset
knn_imputed_file <- file.path(output_folder, "knn_imputed_data.csv")
write.csv(knn_imputed_data, knn_imputed_file, row.names = FALSE)
print(paste("\n✅ KNN Imputed Dataset saved to:", knn_imputed_file))

# ========== Step 9: Visualizing Imputation Effects ==========
# 🚀 TASK: Compare the original dataset with the imputed dataset to evaluate the effects.

# 📊 Plot Before and After Imputation for "Production Cost Per Unit"
ggplot() +
  geom_density(aes(x = data$Production_Cost_Per_Unit, color = "Before Imputation"), na.rm = TRUE) +
  geom_density(aes(x = knn_imputed_data$Production_Cost_Per_Unit, color = "After Imputation"), na.rm = TRUE) +
  labs(title = "Distribution of 'Production Cost Per Unit' Before and After Imputation") +
  theme_minimal()

# Save the plot
imputation_comparison_file <- file.path(output_folder, "imputation_comparison.png")
ggsave(imputation_comparison_file)
print(paste("\n✅ Imputation comparison plot saved."))

# =========================
# 🚀 TASKS FOR STUDENTS:
# 1. **Fix the file path** to load the dataset correctly.
# 2. **Summarize missing values using previous task methods.**
# 3. **Choose between mean and median imputation for different columns.**
# 4. **Run KNN imputation and save the dataset.**
# 5. **Compare before-and-after distributions to validate imputation.**
# =========================

# =========================
# ✅ CORRECT ANSWERS:
# =========================

# 1. **Fixing the File Path**
# Update this line with the correct location of your dataset:
# file_path <- "C:/Users/YourName/Documents/olympus_manufacturing_realistic_missing_data.csv"

# 2. **Summarizing Missing Data**
# Use:
# colSums(is.na(data))

# 3. **Choosing Mean vs. Median Imputation**
# Mean for "Production Cost Per Unit" (as it varies more).
# Median for "Defect Rate" (as it is skewed).

# 4. **Running KNN Imputation**
# kNN(data, k = 3) correctly replaces missing values based on similarity.

# 5. **Distribution Comparison**
# Check the ggplot density plot to see if imputation significantly altered distributions.

# =========================
# 🎯 FINAL TASK:
# Run your fixed script and check the "output" folder for saved results. 🚀
# =================