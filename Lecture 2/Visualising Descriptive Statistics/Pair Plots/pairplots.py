import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Step 1: Load the dataset
# Replace with the correct file path to the dataset
file_path = "Lecture 2/Visualising Descriptive Statistics/Pair Plots/Pair_Plot_Demo_Dataset.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Define the output directory for results
output_folder = "Lecture 2/Visualising Descriptive Statistics/Pair Plots/output"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Generate Pair Plots
# Pair plots allow us to explore relationships between multiple variables in the dataset

# Select numerical columns for pair plots
numerical_columns = ["Age", "AnnualIncome", "SpendingScore", "PurchaseFrequency"]

# Generate pair plot for numerical columns
pairplot_path = os.path.join(output_folder, "Numerical_Pair_Plot.png")
sns.pairplot(data[numerical_columns], diag_kind="kde", plot_kws={"alpha": 0.6, "s": 40, "edgecolor": "k"})
plt.suptitle("Pair Plot for Numerical Variables", y=1.02)
plt.savefig(pairplot_path)
plt.close()

# Generate pair plot with hue for categorical variable "Region"
pairplot_hue_path = os.path.join(output_folder, "Pair_Plot_With_Hue.png")
sns.pairplot(data, hue="Region", diag_kind="kde", plot_kws={"alpha": 0.6, "s": 40, "edgecolor": "k"})
plt.suptitle("Pair Plot with Hue by Region", y=1.02)
plt.savefig(pairplot_hue_path)
plt.close()

# Step 4: Generate a Report
# Summarize the pair plot analysis in a report
report_file = os.path.join(output_folder, "Pair_Plot_Report.txt")
with open(report_file, "w") as report:
    report.write("Pair Plot Visualization Report\n")
    report.write("=" * 50 + "\n\n")
    report.write("Pair plots have been created for the following numerical variables:\n")
    for column in numerical_columns:
        report.write(f"- {column}\n")
    report.write("\n")
    report.write("Additionally, a pair plot with hue has been generated to visualize relationships across regions.\n")
    report.write(f"\nVisualizations have been saved in the output folder: {output_folder}\n")

# Step 5: Final Output Message
print(f"Pair plot visualizations and report saved in: {output_folder}")