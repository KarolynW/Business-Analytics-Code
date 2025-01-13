import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Load the dataset
input_path = "Lecture 3/Example Python Visualisations/Data_Visualisation_Tools_Example_Dataset.xlsx"
data = pd.read_excel(input_path)

# Step 2: Create an output directory
output_path = "Lecture 3/Example Python Visualisations/output"
os.makedirs(output_path, exist_ok=True)

# Step 3: Preprocess data (Group by Region and sum Sales)
sales_by_region = data.groupby("Region")[["Sales"]].sum().reset_index()

# Step 4: Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(sales_by_region["Region"], sales_by_region["Sales"], color="skyblue", edgecolor="black")
plt.title("Total Sales by Region", fontsize=16)
plt.xlabel("Region", fontsize=14)
plt.ylabel("Total Sales", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Step 5: Save the chart
output_chart_path = os.path.join(output_path, "Total_Sales_By_Region.png")
plt.savefig(output_chart_path)
plt.close()

print(f"Bar chart saved to {output_chart_path}")