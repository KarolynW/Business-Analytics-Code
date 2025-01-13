import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Step 1: Load the dataset
# Replace with the correct file path to the dataset
file_path = "Lecture 2/Interpreting Descriptive Statistics/RetailCo_Analysis_Dataset.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Define the output directory for results
output_folder = "Lecture 2/Interpreting Descriptive Statistics/output/Step 1"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Calculate Descriptive Statistics
# Overall Descriptive Statistics
mean_sales = data["MonthlySales"].mean()
median_sales = data["MonthlySales"].median()
range_sales = data["MonthlySales"].max() - data["MonthlySales"].min()
variance_sales = data["MonthlySales"].var(ddof=0)  # Population variance
std_dev_sales = data["MonthlySales"].std(ddof=0)  # Population standard deviation

# Identify top 5 stores above and below the average
above_average_stores = data.nlargest(5, "MonthlySales")
below_average_stores = data.nsmallest(5, "MonthlySales")

# Save the results to a report
report_file = os.path.join(output_folder, "Sales_Summary_Report.txt")
with open(report_file, "w") as report:
    report.write("Sales Summary Report\n")
    report.write("=" * 50 + "\n\n")
    report.write(f"Mean Monthly Sales: ${mean_sales:.2f}\n")
    report.write(f"Median Monthly Sales: ${median_sales:.2f}\n")
    report.write(f"Range of Monthly Sales: ${range_sales:.2f}\n")
    report.write(f"Variance of Monthly Sales: ${variance_sales:.2f}\n")
    report.write(f"Standard Deviation of Monthly Sales: ${std_dev_sales:.2f}\n\n")

    # Answering the questions
    report.write("Analysis:\n")
    report.write("- Are most stores performing close to the average, or is performance highly variable?\n")
    report.write(f"  The standard deviation of ${std_dev_sales:.2f} indicates {'high' if std_dev_sales > mean_sales * 0.2 else 'low'} variability in sales.\n")
    report.write("  Top 5 stores above and below the average have been identified.\n")
    report.write("- Does the median align with the mean, or is the data skewed by outliers?\n")
    skewness = mean_sales - median_sales
    if abs(skewness) / mean_sales > 0.1:
        report.write(f"  The mean (${mean_sales:.2f}) and median (${median_sales:.2f}) differ significantly, suggesting potential skewness caused by outliers.\n")
    else:
        report.write(f"  The mean (${mean_sales:.2f}) and median (${median_sales:.2f}) are close, indicating minimal skewness.\n\n")

    # List top 5 stores above and below the average
    report.write("Top 5 Stores Above Average:\n")
    for _, row in above_average_stores.iterrows():
        report.write(f"  StoreID: {row['StoreID']}, Monthly Sales: ${row['MonthlySales']:.2f}\n")

    report.write("\nTop 5 Stores Below Average:\n")
    for _, row in below_average_stores.iterrows():
        report.write(f"  StoreID: {row['StoreID']}, Monthly Sales: ${row['MonthlySales']:.2f}\n")

# Step 4: Visualize the Data
# Histogram of Monthly Sales
plt.figure(figsize=(10, 6))
plt.hist(data["MonthlySales"], bins=10, color="skyblue", edgecolor="black")
plt.axvline(mean_sales, color="red", linestyle="dashed", linewidth=1.5, label=f"Mean: ${mean_sales:.2f}")
plt.axvline(median_sales, color="green", linestyle="dashed", linewidth=1.5, label=f"Median: ${median_sales:.2f}")
plt.title("Distribution of Monthly Sales")
plt.xlabel("Monthly Sales ($)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
histogram_path = os.path.join(output_folder, "Monthly_Sales_Distribution.png")
plt.savefig(histogram_path)
plt.close()

# Boxplot of Monthly Sales
plt.figure(figsize=(8, 6))
plt.boxplot(data["MonthlySales"], vert=False, patch_artist=True, boxprops=dict(facecolor="skyblue", color="black"))
plt.title("Boxplot of Monthly Sales")
plt.xlabel("Monthly Sales ($)")
plt.grid(axis="x", linestyle="--", alpha=0.7)
boxplot_path = os.path.join(output_folder, "Monthly_Sales_Boxplot.png")
plt.savefig(boxplot_path)
plt.close()

# Step 5: Final Output Message
print(f"Summary report and visualizations saved in: {output_folder}")