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
output_folder = "Lecture 2/Interpreting Descriptive Statistics/output/Step 2"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Calculate Percentiles for Store Segmentation
# Use percentiles to classify stores into performance tiers
data["Percentile"] = data["MonthlySales"].rank(pct=True) * 100

# Segment stores into tiers based on percentiles
data["PerformanceTier"] = pd.cut(
    data["Percentile"],
    bins=[0, 25, 90, 100],
    labels=["Bottom 25%", "Middle Performers", "Top 10%"],
    include_lowest=True
)

# Step 4: Analyze Segments
# Calculate summary statistics for each segment
segment_summary = data.groupby("PerformanceTier").agg(
    AverageSales=("MonthlySales", "mean"),
    AverageFootfall=("CustomerFootfall", "mean"),
    AverageProfitMargin=("ProfitMargin", "mean"),
    StoreCount=("StoreID", "count")
)

# Save segment summary to CSV
segment_summary_file = os.path.join(output_folder, "Segment_Summary.csv")
segment_summary.to_csv(segment_summary_file)

# Identify top 10% and bottom 25% stores
top_performers = data[data["PerformanceTier"] == "Top 10%"]
underperformers = data[data["PerformanceTier"] == "Bottom 25%"]

# Save detailed segment data
top_performers_file = os.path.join(output_folder, "Top_Performers.csv")
top_performers.to_csv(top_performers_file, index=False)
underperformers_file = os.path.join(output_folder, "Underperformers.csv")
underperformers.to_csv(underperformers_file, index=False)

# Step 5: Save the results to a report
report_file = os.path.join(output_folder, "Segment_Analysis_Report.txt")
with open(report_file, "w") as report:
    report.write("Store Segmentation Report\n")
    report.write("=" * 50 + "\n\n")
    report.write("Objective: Classify stores into groups for targeted strategies.\n\n")
    report.write("Key Findings:\n")
    report.write("Top 10% High-Performing Stores:\n")
    for _, row in top_performers.iterrows():
        report.write(f"StoreID: {row['StoreID']}, Monthly Sales: ${row['MonthlySales']:.2f}, Footfall: {row['CustomerFootfall']}, Profit Margin: {row['ProfitMargin']}%\n")
    report.write("\nBottom 25% Underperforming Stores:\n")
    for _, row in underperformers.iterrows():
        report.write(f"StoreID: {row['StoreID']}, Monthly Sales: ${row['MonthlySales']:.2f}, Footfall: {row['CustomerFootfall']}, Profit Margin: {row['ProfitMargin']}%\n")
    report.write("\nSegment Summary:\n")
    report.write(segment_summary.to_string())

# Step 6: Visualize Segments
# Adjusted visualization to handle smaller values like profit margins
fig, ax1 = plt.subplots(figsize=(12, 8))

# Bar chart for Average Sales and Average Footfall
twin_ax = ax1.twinx()
ax1.bar(segment_summary.index, segment_summary["AverageSales"], color="skyblue", label="AverageSales", alpha=0.7, width=0.4, align="edge")
ax1.bar(segment_summary.index, segment_summary["AverageFootfall"], color="lightgreen", label="AverageFootfall", alpha=0.7, width=-0.4, align="edge")

# Line plot for Average Profit Margin
twin_ax.plot(segment_summary.index, segment_summary["AverageProfitMargin"], color="orange", label="AverageProfitMargin", marker="o")

# Titles and labels
ax1.set_ylabel("Average Sales / Footfall", color="black")
twin_ax.set_ylabel("Average Profit Margin (%)", color="orange")
ax1.set_title("Performance Segment Averages")
ax1.set_xlabel("Performance Tier")
ax1.grid(axis="y", linestyle="--", alpha=0.7)

# Legends
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.95), bbox_transform=ax1.transAxes)

# Save the updated plot
segment_plot_path = os.path.join(output_folder, "Segment_Summary_Bar_Line_Plot.png")
plt.savefig(segment_plot_path)
plt.close()

# Step 7: Final Output Message
print(f"Store segmentation analysis completed. Results and visualizations saved in: {output_folder}")