import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load the dataset
# Load the dataset containing numerical and categorical data.
# Ensure the file path points to the correct location of your dataset.
file_path = "Lecture 1/Outlier Detection/Outlier_Detection_Dataset.xlsx"  # Replace with the correct path if needed
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Create a folder to save the output files, such as plots and labeled datasets.
output_folder = "Lecture 1/Outlier Detection/output/Box Plots and IQR"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Function to identify and label outliers using IQR and boxplots
def identify_outliers(column):
    """
    Identify outliers in a numerical column using the IQR method.

    Parameters:
        column (str): The column name to analyze.

    Returns:
        outliers (DataFrame): Rows identified as outliers.
        lower_bound (float): Lower threshold for outliers.
        upper_bound (float): Upper threshold for outliers.
    """
    # Calculate the first and third quartiles (Q1 and Q3)
    Q1 = data[column].quantile(0.25)  # First quartile (25%)
    Q3 = data[column].quantile(0.75)  # Third quartile (75%)
    IQR = Q3 - Q1  # Interquartile range

    # Define outlier bounds
    lower_bound = Q1 - 1.5 * IQR  # Any value below this is an outlier
    upper_bound = Q3 + 1.5 * IQR  # Any value above this is an outlier

    # Identify rows that are outliers
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]

    # Add a column to label whether each row is an outlier or normal
    data[f"{column}_Outlier"] = data[column].apply(
        lambda x: "Outlier" if (x < lower_bound or x > upper_bound) else "Normal"
    )

    # Return the outliers and bounds for reference
    return outliers, lower_bound, upper_bound

# Step 4: Analyze columns with numerical data for outliers
# Select numerical columns for analysis, excluding identifiers like "ID"
numerical_columns = [col for col in data.select_dtypes(include=["float64", "int64"]).columns if col != "ID"]

for column in numerical_columns:
    print(f"Analyzing column: {column}")

    # Identify outliers in the column
    outliers, lower, upper = identify_outliers(column)

    # Save the outlier data to a CSV file
    outliers_file = os.path.join(output_folder, f"{column}_Outliers.csv")
    outliers.to_csv(outliers_file, index=False)

    # Print bounds to the console for reference
    print(f"Outlier detection for {column}: Lower Bound = {lower}, Upper Bound = {upper}")

    # Plot a boxplot with labeled outliers
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x=column, showmeans=True, palette="pastel")

    # Annotate the outliers on the boxplot
    for i in range(outliers.shape[0]):
        plt.text(outliers[column].iloc[i], 0, f"ID {outliers['ID'].iloc[i]}",
                 color="red", fontsize=9, ha="center", va="bottom")

    # Add titles and labels to the boxplot
    plt.title(f"Boxplot for {column} with Outliers")
    plt.xlabel(column)

    # Save the boxplot as a PNG file
    plt.savefig(os.path.join(output_folder, f"{column}_Boxplot.png"))
    plt.close()

    # Write information about the outliers to the report
    print(f"Outliers for {column} saved to {outliers_file}")

# Step 5: Save the dataset with labeled outliers
# Save the full dataset, including outlier labels, to an Excel file
labeled_file = os.path.join(output_folder, "Labeled_Dataset.xlsx")
data.to_excel(labeled_file, index=False)

print(f"Labeled dataset with outlier flags saved to {labeled_file}")
print("Outlier analysis complete. Results saved in the Lecture 1\Outlier Detection\output\Box Plots and IQR.")