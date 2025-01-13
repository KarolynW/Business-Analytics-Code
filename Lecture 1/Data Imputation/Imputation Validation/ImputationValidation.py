import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load Before and After Imputation Datasets
# Replace these with the actual file paths
before_file_path = "Lecture 1/Data Imputation/KNN Example/KNN_Imputation_Dataset.xlsx"
after_file_path = "Lecture 1/Data Imputation/KNN Example/output/Analysed_KNN_Imputed_Dataset.xlsx"

before_data = pd.read_excel(before_file_path)
after_data = pd.read_excel(after_file_path)

# Step 2: Encode Categorical Variables
# Convert categorical columns to numeric for correlation analysis
categorical_columns = before_data.select_dtypes(include=['object', 'category']).columns
before_encoded = before_data.copy()
after_encoded = after_data.copy()

for column in categorical_columns:
    before_encoded[column] = before_encoded[column].astype("category").cat.codes
    after_encoded[column] = after_encoded[column].astype("category").cat.codes

# Step 3: Check Distributions
# Compare distributions of columns with missing values
output_folder = "Lecture 1/Data Imputation/Imputation Validation/output"
os.makedirs(output_folder, exist_ok=True)
report_file = os.path.join(output_folder, "Verification_Report.txt")

with open(report_file, "w") as report:
    report.write("Imputation Verification Report\n")
    report.write("=" * 50 + "\n\n")

    for column in before_data.columns:
        if before_data[column].isnull().sum() > 0:
            # Check distribution before and after
            plt.figure(figsize=(10, 6))
            sns.histplot(before_data[column], kde=True, color="blue", label="Before Imputation")
            sns.histplot(after_data[column], kde=True, color="orange", label="After Imputation")
            plt.title(f"Distribution Comparison for {column}")
            plt.legend()
            plt.savefig(os.path.join(output_folder, f"{column}_distribution_comparison.png"))
            plt.close()

            # Add text summary to report
            before_mean = before_data[column].mean()
            after_mean = after_data[column].mean()
            before_median = before_data[column].median()
            after_median = after_data[column].median()

            report.write(f"Column: {column}\n")
            report.write(f"- Missing values before: {before_data[column].isnull().sum()}\n")
            report.write(f"- Mean before: {before_mean}, After: {after_mean}\n")
            report.write(f"- Median before: {before_median}, After: {after_median}\n\n")

# Step 4: Correlation Analysis
# Compare correlation matrices
before_corr = before_encoded.corr()
after_corr = after_encoded.corr()

plt.figure(figsize=(14, 10))
sns.heatmap(before_corr, annot=True, fmt=".2f", cmap="Blues")
plt.title("Correlation Matrix Before Imputation")
plt.savefig(os.path.join(output_folder, "Correlation_Before.png"))
plt.close()

plt.figure(figsize=(14, 10))
sns.heatmap(after_corr, annot=True, fmt=".2f", cmap="Oranges")
plt.title("Correlation Matrix After Imputation")
plt.savefig(os.path.join(output_folder, "Correlation_After.png"))
plt.close()

# Save correlation differences
correlation_diff = (after_corr - before_corr).abs()
correlation_diff.to_csv(os.path.join(output_folder, "Correlation_Differences.csv"))

with open(report_file, "a") as report:
    report.write("Correlation Analysis\n")
    report.write("- Correlation matrices saved as images.\n")
    report.write("- Differences in correlation saved as CSV.\n\n")

# Step 5: Document Outliers
# Compare boxplots to identify potential outliers introduced by imputation
for column in before_data.columns:
    if before_data[column].isnull().sum() > 0:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=pd.DataFrame({"Before Imputation": before_data[column].dropna(),
                                       "After Imputation": after_data[column]}),
                    showmeans=True)
        plt.title(f"Outlier Comparison for {column}")
        plt.savefig(os.path.join(output_folder, f"{column}_outlier_comparison.png"))
        plt.close()

        with open(report_file, "a") as report:
            report.write(f"Outlier Analysis for {column}: Boxplot saved as image.\n")

# Finalize Report
with open(report_file, "a") as report:
    report.write("\nVerification Process Completed.\n")
    report.write(f"All outputs are saved in the folder: {output_folder}\n")

print(f"Verification process complete. Report and visualizations saved in {output_folder}")