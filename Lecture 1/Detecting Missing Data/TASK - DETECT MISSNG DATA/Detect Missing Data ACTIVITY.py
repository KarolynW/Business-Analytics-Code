# =========================
# 🛠 HANDLING MISSING DATA TASK - SwiftyRetail
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
# In VS Code, open the terminal and run the following commands:
# Run each command **one by one** in the terminal:
# ---------------------------------
# pip install pandas
# pip install seaborn
# pip install matplotlib
# pip install openpyxl  # Required for reading Excel files
# ---------------------------------

# ========== Step 2: Import Required Libraries ==========
# Now that you’ve installed the required libraries, let’s import them.

import os  # For creating an output folder
import pandas as pd   # For handling data
import seaborn as sns  # For visualizing missing data
import matplotlib.pyplot as plt  # For plotting charts

# ========== Step 3: Create an Output Folder ==========
# ✅ Ensure that an "output" folder is created to store saved files.

output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # Creates the folder if it doesn't exist
    print(f"📂 Created output folder: {output_folder}")

# ========== Step 4: Load the Dataset ==========
# 🔴 TASK: Replace "your_path_here" with the correct location of your dataset file.

file_path = r"your_path_here\swiftyretail_inventory_sales.xlsx"  # 🔧 FIX ME: Update this!

# 🚀 PRO TIP: If using Windows, use **double backslashes ("\\")** or a raw string (r"") to avoid errors.

# Load the dataset using pandas
try:
    data = pd.read_excel(file_path, engine="openpyxl")  # Ensure 'openpyxl' is used for .xlsx files
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
# 📊 Count missing values per column
missing_summary = data.isnull().sum()
missing_summary = missing_summary[missing_summary > 0]  # Only show columns with missing values

# Save missing data summary to CSV
missing_summary_file = os.path.join(output_folder, "missing_data_summary.csv")
missing_summary.to_csv(missing_summary_file)

print("\n🛑 Missing Data Summary saved to:", missing_summary_file)

# ========== Step 7: Calculate Missing Data Percentage ==========
# 📉 Calculate the percentage of missing values.

missing_percentage = (missing_summary / len(data)) * 100

# Save missing data percentage to CSV
missing_percentage_file = os.path.join(output_folder, "missing_data_percentage.csv")
missing_percentage.to_csv(missing_percentage_file)

print("\n📉 Percentage of Missing Values saved to:", missing_percentage_file)

# ========== Step 8: Visualizing Missing Data ==========
# TASK: Fix the commented-out line to show missing values in a different color.

plt.figure(figsize=(12, 8))
sns.heatmap(data.isnull(), cbar=False, cmap="coolwarm")  # 🔧 FIX ME: Change "viridis" to "coolwarm" for better contrast
plt.title("Heatmap of Missing Data")

heatmap_file = os.path.join(output_folder, "missing_data_heatmap.png")
plt.savefig(heatmap_file)  # Save heatmap as PNG
plt.close()

print("🖼 Heatmap saved to:", heatmap_file)

# ========== Step 9: Bar Chart of Missing Values ==========
# TASK: Fix the bar chart labels and title for better clarity.

plt.figure(figsize=(10, 6))  
missing_summary.plot(kind="bar", color="steelblue")  
plt.title("FIX ME: Missing Values Count")  # 🔧 Update title
plt.ylabel("FIX ME: What is on this axis?")  # 🔧 Update axis label
plt.xticks(rotation=45, ha="right")

missing_count_chart = os.path.join(output_folder, "missing_data_count.png")
plt.savefig(missing_count_chart)  # Save chart as PNG
plt.close()

print("🖼 Bar Chart (Count) saved to:", missing_count_chart)

# ========== Step 10: Bar Chart of Missing Percentages ==========
# TASK: Fix the title to better describe what is being shown.

plt.figure(figsize=(10, 6))  
missing_percentage.plot(kind="bar", color="darkorange")  
plt.title("FIX ME: Percentage of What?")  # 🔧 Update title
plt.ylabel("Percentage (%)")  
plt.xticks(rotation=45, ha="right")

missing_percentage_chart = os.path.join(output_folder, "missing_data_percentage.png")
plt.savefig(missing_percentage_chart)  # Save chart as PNG
plt.close()

print("🖼 Bar Chart (Percentage) saved to:", missing_percentage_chart)

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
# file_path = r"C:\Users\YourName\Documents\swiftyretail_inventory_sales.xlsx"

# 2. **Changing the Heatmap Color**
# Replace:
# sns.heatmap(data.isnull(), cbar=False, cmap="viridis")
# With:
# sns.heatmap(data.isnull(), cbar=False, cmap="coolwarm")

# 3. **Fixing the Bar Chart Titles and Labels**
# - Replace:
# plt.title("FIX ME: Missing Values Count")
# With:
# plt.title("Count of Missing Values per Column")

# - Replace:
# plt.ylabel("FIX ME: What is on this axis?")
# With:
# plt.ylabel("Number of Missing Entries")

# - Replace:
# plt.title("FIX ME: Percentage of What?")
# With:
# plt.title("Percentage of Missing Values per Column")

# =========================
# 🎯 FINAL TASK:
# Run your fixed script and check the "output" folder for saved results. 🚀
# =================