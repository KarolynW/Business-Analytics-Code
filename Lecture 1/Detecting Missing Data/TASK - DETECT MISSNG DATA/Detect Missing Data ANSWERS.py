# =========================
# 🛠 COMPLETE HANDLING MISSING DATA SCRIPT - SwiftyRetail (WITH SAVED OUTPUTS)
# =========================

# ========== Step 1: Install Required Libraries ==========
# In VS Code, open the terminal and run the following commands if you haven't installed them yet:
# ---------------------------------
# pip install pandas
# pip install seaborn
# pip install matplotlib
# pip install openpyxl  # Required for reading Excel files
# ---------------------------------

# ========== Step 2: Import Required Libraries ==========
import os  # For handling file paths
import pandas as pd   # For handling data
import seaborn as sns  # For visualizing missing data
import matplotlib.pyplot as plt  # For plotting charts

# ========== Step 3: Create Output Folder ==========
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # Creates the folder if it doesn't exist
    print(f"📂 Created output folder: {output_folder}")

# ========== Step 4: Load the Dataset ==========
# ✅ Update the file path below with the actual location of your dataset
file_path = r"Lecture 1\Detecting Missing Data\TASK - DETECT MISSNG DATA\swiftyretail_inventory_sales.xlsx"  # Change this to your correct path

# ✅ Load the dataset using pandas
try:
    data = pd.read_excel(file_path, engine="openpyxl")  # Ensure 'openpyxl' is used for .xlsx files
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ ERROR: The file was not found! Please check the file path and try again.")
    exit()  # Stops execution if the file isn't found

# ========== Step 5: Explore Dataset Structure ==========
# 🔍 Display dataset information and save it to a text file
dataset_info_file = os.path.join(output_folder, "dataset_info.txt")
with open(dataset_info_file, "w") as f:
    data.info(buf=f)

print("\n🔍 Dataset Info saved to:", dataset_info_file)

# ========== Step 6: Identify Missing Data ==========
# 📊 Count missing values per column
missing_summary = data.isnull().sum()
missing_summary = missing_summary[missing_summary > 0]  # Only keep columns with missing values

# Save missing data summary to CSV
missing_summary_file = os.path.join(output_folder, "missing_data_summary.csv")
missing_summary.to_csv(missing_summary_file)
print("\n🛑 Missing Data Summary saved to:", missing_summary_file)

# ========== Step 7: Calculate Missing Data Percentage ==========
# 📉 Calculate the percentage of missing values
missing_percentage = (missing_summary / len(data)) * 100

# Save missing data percentage to CSV
missing_percentage_file = os.path.join(output_folder, "missing_data_percentage.csv")
missing_percentage.to_csv(missing_percentage_file)
print("\n📉 Percentage of Missing Values saved to:", missing_percentage_file)

# ========== Step 8: Visualizing Missing Data ==========
# 🔥 Heatmap of missing values
plt.figure(figsize=(12, 8))
sns.heatmap(data.isnull(), cbar=False, cmap="coolwarm")
plt.title("Heatmap of Missing Data")
heatmap_file = os.path.join(output_folder, "missing_data_heatmap.png")
plt.savefig(heatmap_file)  # Save heatmap as PNG
plt.close()
print("🖼 Heatmap saved to:", heatmap_file)

# ========== Step 9: Bar Chart of Missing Values ==========
# 📊 Bar chart showing missing data counts
plt.figure(figsize=(10, 6))  
missing_summary.plot(kind="bar", color="steelblue")
plt.title("Count of Missing Values per Column")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
missing_count_chart = os.path.join(output_folder, "missing_data_count.png")
plt.savefig(missing_count_chart)  # Save bar chart as PNG
plt.close()
print("🖼 Bar Chart (Count) saved to:", missing_count_chart)

# ========== Step 10: Bar Chart of Missing Percentages ==========
# 📊 Bar chart showing missing data percentages
plt.figure(figsize=(10, 6))  
missing_percentage.plot(kind="bar", color="darkorange")
plt.title("Percentage of Missing Values per Column")
plt.ylabel("Percentage (%)")
plt.xticks(rotation=45, ha="right")
missing_percentage_chart = os.path.join(output_folder, "missing_data_percentage.png")
plt.savefig(missing_percentage_chart)  # Save bar chart as PNG
plt.close()
print("🖼 Bar Chart (Percentage) saved to:", missing_percentage_chart)

# =========================
# ✅ SCRIPT COMPLETED SUCCESSFULLY! ALL OUTPUTS SAVED.
# =========================

