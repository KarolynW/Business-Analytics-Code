import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load the dataset
# Replace with the correct file path to the dataset
file_path = "Lecture 2/Advanced Data Summarization Techniques/Descriptive_Statistics_Demo_Dataset.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Define the output directory for analysis results
output_folder = "Lecture 2/Advanced Data Summarization Techniques/output"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Data Binning
# Group continuous data (e.g., Age) into discrete bins
# Define bins for age groups
age_bins = [18, 25, 35, 45, 55, 65, 75]
age_labels = ["18-25", "26-35", "36-45", "46-55", "56-65", "66-75"]
data["AgeGroup"] = pd.cut(data["Age"], bins=age_bins, labels=age_labels, right=False)

# Save binned data for review
binned_data_file = os.path.join(output_folder, "Binned_Data.xlsx")
data.to_excel(binned_data_file, index=False)

# Step 4: Percentiles and Quantiles
# Calculate percentiles for SpendingScore
percentiles = {
    "5th Percentile": np.percentile(data["SpendingScore"], 5),
    "25th Percentile (Q1)": np.percentile(data["SpendingScore"], 25),
    "50th Percentile (Median)": np.percentile(data["SpendingScore"], 50),
    "75th Percentile (Q3)": np.percentile(data["SpendingScore"], 75),
    "95th Percentile": np.percentile(data["SpendingScore"], 95),
}

# Save percentiles to a report
percentile_report_file = os.path.join(output_folder, "Percentile_Report.txt")
with open(percentile_report_file, "w") as report:
    report.write("Percentiles for SpendingScore:\n")
    report.write("=" * 50 + "\n\n")
    for name, value in percentiles.items():
        report.write(f"{name}: {value:.2f}\n")

# Step 5: Skewness and Kurtosis
# Calculate skewness and kurtosis for AnnualIncome and SpendingScore
skewness_kurtosis = {
    "AnnualIncome": {
        "Skewness": data["AnnualIncome"].skew(),
        "Kurtosis": data["AnnualIncome"].kurtosis(),
    },
    "SpendingScore": {
        "Skewness": data["SpendingScore"].skew(),
        "Kurtosis": data["SpendingScore"].kurtosis(),
    },
}

# Save skewness and kurtosis to the report
with open(percentile_report_file, "a") as report:
    report.write("\nSkewness and Kurtosis:\n")
    report.write("=" * 50 + "\n\n")
    for column, stats in skewness_kurtosis.items():
        report.write(f"{column}:\n")
        report.write(f"- Skewness: {stats['Skewness']:.2f}\n")
        report.write(f"- Kurtosis: {stats['Kurtosis']:.2f}\n\n")

# Step 6: Visualization
# Histogram for Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data["Age"], bins=age_bins, kde=False, color="blue")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig(os.path.join(output_folder, "Age_Distribution.png"))
plt.close()

# Cumulative Distribution Plot for SpendingScore
plt.figure(figsize=(10, 6))
sns.ecdfplot(data["SpendingScore"], color="green")
plt.title("Cumulative Distribution of SpendingScore")
plt.xlabel("SpendingScore")
plt.ylabel("Cumulative Probability")
plt.savefig(os.path.join(output_folder, "Cumulative_Distribution_SpendingScore.png"))
plt.close()

# Boxplot for AnnualIncome
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="Region", y="AnnualIncome", palette="Set2")
plt.title("Annual Income by Region")
plt.xlabel("Region")
plt.ylabel("Annual Income")
plt.savefig(os.path.join(output_folder, "Annual_Income_Boxplot.png"))
plt.close()

# Density Plot for AnnualIncome and SpendingScore
plt.figure(figsize=(10, 6))
sns.kdeplot(data["AnnualIncome"], fill=True, color="orange", label="Annual Income")
sns.kdeplot(data["SpendingScore"], fill=True, color="purple", label="Spending Score")
plt.title("Density Plot for Annual Income and Spending Score")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.savefig(os.path.join(output_folder, "Density_Plot.png"))
plt.close()

# Skewness Visualization
plt.figure(figsize=(10, 6))
sns.histplot(data["AnnualIncome"], kde=True, color="orange", bins=30)
plt.title("Annual Income Distribution (Skewness)")
plt.xlabel("Annual Income")
plt.ylabel("Frequency")
plt.savefig(os.path.join(output_folder, "AnnualIncome_Skewness.png"))
plt.close()

plt.figure(figsize=(10, 6))
sns.histplot(data["SpendingScore"], kde=True, color="purple", bins=30)
plt.title("Spending Score Distribution (Skewness)")
plt.xlabel("Spending Score")
plt.ylabel("Frequency")
plt.savefig(os.path.join(output_folder, "SpendingScore_Skewness.png"))
plt.close()

# Kurtosis Visualization
plt.figure(figsize=(10, 6))
sns.kdeplot(data["AnnualIncome"], color="orange", fill=True, label="Annual Income")
plt.axvline(data["AnnualIncome"].mean(), color="red", linestyle="--", label="Mean")
plt.title("Annual Income Distribution (Kurtosis)")
plt.xlabel("Annual Income")
plt.ylabel("Density")
plt.legend()
plt.savefig(os.path.join(output_folder, "AnnualIncome_Kurtosis.png"))
plt.close()

plt.figure(figsize=(10, 6))
sns.kdeplot(data["SpendingScore"], color="purple", fill=True, label="Spending Score")
plt.axvline(data["SpendingScore"].mean(), color="red", linestyle="--", label="Mean")
plt.title("Spending Score Distribution (Kurtosis)")
plt.xlabel("Spending Score")
plt.ylabel("Density")
plt.legend()
plt.savefig(os.path.join(output_folder, "SpendingScore_Kurtosis.png"))
plt.close()

# Final Output Messages
print(f"Analysis complete. Results saved in: {output_folder}")
print(f"Binned data saved to: {binned_data_file}")
print(f"Percentiles and skewness/kurtosis report saved to: {percentile_report_file}")