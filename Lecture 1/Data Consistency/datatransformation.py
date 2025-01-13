import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

# Step 1: Load the dataset
# Replace with the correct file path to the dataset
file_path = "Lecture 1/Data Consistency/Scaling_Encoding_Example_Dataset.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Define the output directory for transformed data
output_folder = "Lecture 1/Data Consistency/output"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Min-Max Scaling
# Min-Max Scaling transforms numerical values to a specific range, usually [0, 1]
scaler_minmax = MinMaxScaler()
data["Age_MinMax"] = scaler_minmax.fit_transform(data[["Age"]])
data["Income_MinMax"] = scaler_minmax.fit_transform(data[["Income"]])

# Step 4: Z-Score Standardization
# Z-Score Standardization centers the data around 0 with a standard deviation of 1
scaler_zscore = StandardScaler()
data["Age_ZScore"] = scaler_zscore.fit_transform(data[["Age"]])
data["Income_ZScore"] = scaler_zscore.fit_transform(data[["Income"]])

# Step 5: One-Hot Encoding
# One-Hot Encoding converts categorical data into binary columns
region_dummies = pd.get_dummies(data["Region"], prefix="Region")
data = pd.concat([data, region_dummies], axis=1)

# Step 6: Label Encoding
# Label Encoding assigns a unique integer to each category
label_encoder = LabelEncoder()
data["Satisfaction_LabelEncoded"] = label_encoder.fit_transform(data["Satisfaction"])

# Step 7: Save the transformed dataset
# Save the full dataset with all transformations to an Excel file
transformed_file = os.path.join(output_folder, "Transformed_Data.xlsx")
data.to_excel(transformed_file, index=False)

# Step 8: Generate a summary report
# Create a report summarizing the transformations applied
report_file = os.path.join(output_folder, "Transformation_Report.txt")
with open(report_file, "w") as report:
    report.write("Data Transformation Report\n")
    report.write("=" * 50 + "\n\n")

    # Min-Max Scaling
    report.write("Min-Max Scaling:\n")
    report.write("- Transformed columns: Age, Income\n")
    report.write("- Range: [0, 1]\n\n")

    # Z-Score Standardization
    report.write("Z-Score Standardization:\n")
    report.write("- Transformed columns: Age, Income\n")
    report.write("- Mean = 0, Standard Deviation = 1\n\n")

    # One-Hot Encoding
    report.write("One-Hot Encoding:\n")
    report.write("- Categorical column transformed: Region\n")
    report.write(f"- Created columns: {', '.join(region_dummies.columns)}\n\n")

    # Label Encoding
    report.write("Label Encoding:\n")
    report.write("- Categorical column transformed: Satisfaction\n")
    report.write("- Mapping:\n")
    for i, class_ in enumerate(label_encoder.classes_):
        report.write(f"  {class_}: {i}\n")

print(f"Transformed dataset saved to: {transformed_file}")
print(f"Data transformation report saved to: {report_file}")