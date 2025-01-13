import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Step 1: Load the dataset
input_path = "Lecture 3/Example Python Visualisations/Data_Visualisation_Tools_Example_Dataset.xlsx"
data = pd.read_excel(input_path)

# Step 2: Create an output directory
output_path = "Lecture 3/Example Python Visualisations/output"
os.makedirs(output_path, exist_ok=True)

# Step 3: Create a swarm plot for Sales by Region
plt.figure(figsize=(10, 6))
sns.swarmplot(
    x="Region",
    y="Sales",
    data=data,
    palette="muted",
    size=6,
    edgecolor="black",
    linewidth=0.5
)

# Step 4: Customize the plot
plt.title("Sales Distribution by Region", fontsize=16)
plt.xlabel("Region", fontsize=14)
plt.ylabel("Sales", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Step 5: Save the plot
output_chart_path = os.path.join(output_path, "Sales_Swarm_Plot.png")
plt.savefig(output_chart_path)
plt.close()

print(f"Swarm plot saved to {output_chart_path}")


