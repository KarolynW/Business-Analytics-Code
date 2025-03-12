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
# In VS Code, open the terminal and run the following commands:
# ---------------------------------
# pip install pandas
# pip install seaborn
# pip install matplotlib
# pip install scikit-learn
# ---------------------------------

# ========== Step 2: Import Required Libraries ==========
import os  # For creating an output folder
import pandas as pd   # For handling data
import seaborn as sns  # For visualization
import matplotlib.pyplot as plt  # For plotting charts
from sklearn.impute import KNNImputer  # For KNN-based imputation

# ========== Step 3: Create an Output Folder ==========
# ✅ Ensure that an "output" folder is created to store saved files.
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"📂 Created output folder: {output_folder}")

# ========== Step 4: Load the Dataset ==========
# 🔴 TASK: Replace "your_path_here" with the correct location of your dataset file.
file_path = r"your_path_here/olympus_manufacturing_realistic_missing_data.csv"  # 🔧 FIX ME: Update this!

# Load the dataset using pandas
try:
    data = pd.read_csv(file_path)
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ ERROR: The file was not found! Please check the file path and try again.")
    exit()  # Stops execution if the file isn't found

# ========== Step 5: Explore Dataset Structure ==========
# 🔍 Save dataset information to a text file
dataset_info_file = os.path.join(output_folder, "dataset_info.txt")
with open(dataset_info_file, "w") as f:
    data.info(buf=f)

print("\n🔍 Dataset Info saved to:", dataset_info_file)

# ========== Step 6: Identify Missing Data ==========
# 📊 TASK: Use the skills from the previous task to summarize missing values!
# - Count missing values per column
# - Calculate the percentage of missing values

print("\n🛑 Missing Data Summary:")
missing_summary = data.isnull().sum()
print(missing_summary[missing_summary > 0])  # Only show columns with missing values

# 📉 TASK: Calculate the percentage of missing values
missing_percentage = (missing_summary / len(data)) * 100
print("\n📉 Percentage of Missing Values:")
print(missing_percentage[missing_percentage > 0])  # Show only affected columns

# Save missing data summary
missing_summary_file = os.path.join(output_folder, "missing_data_summary.csv")
missing_summary.to_csv(missing_summary_file)
print("\n✅ Missing Data Summary saved to:", missing_summary_file)

# ========== Step 7: Apply Mean/Median Imputation ==========
# 🚀 TASK: Implement Mean/Median Imputation for numerical columns

# Copy the dataset to preserve the original
imputed_data = data.copy()

# 🔧 FIX ME: Choose either mean or median imputation for "Production Cost Per Unit" and "Defect Rate"
imputed_data['Production Cost Per Unit'] = imputed_data['Production Cost Per Unit'].fillna(imputed_data['Production Cost Per Unit'].mean())  # Mean Imputation
imputed_data['Defect Rate'] = imputed_data['Defect Rate'].fillna(imputed_data['Defect Rate'].median())  # Median Imputation

# ========== Step 8: Apply KNN Imputation ==========
# 🚀 TASK: Implement KNN Imputation for missing values in the dataset.

# Initialize KNN Imputer with k=3
imputer = KNNImputer(n_neighbors=3)
knn_imputed_data = pd.DataFrame(imputer.fit_transform(imputed_data), columns=imputed_data.columns)

# Save the KNN-imputed dataset
knn_imputed_file = os.path.join(output_folder, "knn_imputed_data.csv")
knn_imputed_data.to_csv(knn_imputed_file, index=False)
print("\n✅ KNN Imputed Dataset saved to:", knn_imputed_file)

# ========== Step 9: Visualizing Imputation Effects ==========
# 🚀 TASK: Compare the original dataset with the imputed dataset to evaluate the effects.

# 📊 Plot Before and After Imputation for "Production Cost Per Unit"
plt.figure(figsize=(10, 5))
sns.kdeplot(data['Production Cost Per Unit'], label="Before Imputation", fill=True)
sns.kdeplot(knn_imputed_data['Production Cost Per Unit'], label="After Imputation", fill=True)
plt.legend()
plt.title("Distribution of 'Production Cost Per Unit' Before and After Imputation")
plt.savefig(os.path.join(output_folder, "imputation_comparison.png"))
plt.show()

print("\n✅ Imputation comparison plot saved.")

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
# file_path = r"C:\Users\YourName\Documents\olympus_manufacturing_realistic_missing_data.csv"

# 2. **Summarizing Missing Data**
# Use:
# print(data.isnull().sum())

# 3. **Choosing Mean vs. Median Imputation**
# Mean for "Production Cost Per Unit" (as it varies more).
# Median for "Defect Rate" (as it is skewed).

# 4. **Running KNN Imputation**
# KNNImputer(n_neighbors=3) correctly replaces missing values based on similarity.

# 5. **Distribution Comparison**
# Check the KDE plot to see if imputation significantly altered distributions.

# =========================
# 🎯 FINAL TASK:
# Run your fixed script and check the "output" folder for saved results. 🚀
# =================
