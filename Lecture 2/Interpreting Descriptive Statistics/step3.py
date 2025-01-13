import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load the dataset
file_path = "Lecture 2/Interpreting Descriptive Statistics/RetailCo_Analysis_Dataset.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
output_folder = "Lecture 2/Interpreting Descriptive Statistics/output/Step 3"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Boxplots to compare sales by region
plt.figure(figsize=(10, 6))
sns.boxplot(x="Region", y="MonthlySales", data=data, palette="Set2")
plt.title("Boxplot of Monthly Sales by Region")
plt.ylabel("Monthly Sales")
plt.xlabel("Region")
plt.grid(axis="y", linestyle="--", alpha=0.7)
boxplot_path = os.path.join(output_folder, "Sales_By_Region_Boxplot.png")
plt.savefig(boxplot_path)
plt.close()

# Step 4: Heatmap to visualize correlations between metrics
# Calculate the correlation matrix
correlation_matrix = data[["MonthlySales", "CustomerFootfall", "AdvertisingSpend", "ProfitMargin"]].corr()

# Generate the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Metrics")
heatmap_path = os.path.join(output_folder, "Metrics_Correlation_Heatmap.png")
plt.savefig(heatmap_path)
plt.close()

# Step 5: Generate a report
report_path = os.path.join(output_folder, "Visual_Analysis_Report.txt")
with open(report_path, "w") as report:
    report.write("Visual Analysis Report\n")
    report.write("=" * 50 + "\n\n")
    report.write("Objective: Make patterns and trends visible for better interpretation.\n\n")
    report.write("Key Findings:\n")

    # Boxplot insights
    report.write("1. Boxplot Analysis:\n")
    for region in data["Region"].unique():
        region_data = data[data["Region"] == region]
        min_sales = region_data["MonthlySales"].min()
        max_sales = region_data["MonthlySales"].max()
        report.write(f"   - {region}: Min Sales = ${min_sales}, Max Sales = ${max_sales}\n")
    report.write("\n")

    # Correlation insights
    report.write("2. Correlation Analysis:\n")
    report.write("Correlation matrix between metrics:\n")
    report.write(correlation_matrix.to_string())
    report.write("\n\n")
    report.write("   - High correlation values indicate strong relationships, e.g., between Advertising Spend and Monthly Sales.\n")
    report.write("   - Weak or negative correlations highlight areas with little or no relationship.\n")

# Step 6: Print completion message
print(f"Step 3 analysis completed. Results saved in {output_folder}")
