import pandas as pd
import os

# Step 1: Load the dataset
# Replace with the correct file path to the dataset
file_path = "Lecture 1/Data Consistency/Data_Inconsistencies_Dataset.xlsx"
data = pd.read_excel(file_path)

# Step 2: Create an output folder
# Define the output directory for resolved data
output_folder = "Lecture 1/Data Consistency/output"
os.makedirs(output_folder, exist_ok=True)

# Step 3: Function to standardize dates
# This function ensures all dates are in the UK format DD/MM/YYYY
def standardize_dates_to_uk(date_column):
    """
    Standardize date formats to DD/MM/YYYY for UK standards.

    Parameters:
        date_column (Series): The column containing dates.

    Returns:
        Series: Standardized dates.
    """
    standardized_dates = pd.to_datetime(date_column, errors='coerce', dayfirst=True)
    return standardized_dates.dt.strftime('%d/%m/%Y')

# Step 4: Function to convert currencies to GBP
# Assuming a simple fixed conversion rate for demonstration
conversion_rates = {"USD": 0.80, "GBP": 1}  # Example rates

def convert_currency_to_gbp(sales_column, unit_column):
    """
    Convert all sales amounts to GBP using a fixed conversion rate.

    Parameters:
        sales_column (Series): The column with sales amounts.
        unit_column (Series): The column with currency units.

    Returns:
        Series: Sales amounts converted to GBP.
    """
    converted_sales = sales_column * unit_column.map(conversion_rates)
    return converted_sales

# Step 5: Function to unify weight units to kilograms
# Conversion rate: 1 lb = 0.453592 kg
weight_conversion = {"kg": 1, "lb": 0.453592}

def convert_weights_to_kg(weight_column, unit_column):
    """
    Convert all weights to kilograms for UK standards.

    Parameters:
        weight_column (Series): The column with weights.
        unit_column (Series): The column with weight units.

    Returns:
        Series: Weights converted to kilograms.
    """
    converted_weights = weight_column * unit_column.map(weight_conversion)
    return converted_weights

# Step 6: Apply corrections
# Standardize dates to UK format
data["StandardizedDate"] = standardize_dates_to_uk(data["Date"])

# Convert sales amounts to GBP
data["SalesAmountGBP"] = convert_currency_to_gbp(data["SalesAmount"], data["Unit"])

# Convert weights to kilograms
data["ProductWeightKG"] = convert_weights_to_kg(data["ProductWeight"], data["WeightUnit"])

# Step 7: Save corrected data
# Save the cleaned dataset to the output folder
cleaned_file = os.path.join(output_folder, "Cleaned_Data_Inconsistencies_Dataset.xlsx")
data.to_excel(cleaned_file, index=False)

# Generate a summary report
report_file = os.path.join(output_folder, "Data_Cleanup_Report.txt")
with open(report_file, "w") as report:
    report.write("Data Cleanup Report\n")
    report.write("=" * 50 + "\n\n")

    # Report on date standardization
    invalid_dates = data["StandardizedDate"].isnull().sum()
    report.write(f"Date Standardization:\n")
    report.write(f"- Invalid dates found: {invalid_dates}\n")
    report.write(f"- All valid dates standardized to DD/MM/YYYY format.\n\n")

    # Report on currency conversion
    report.write(f"Currency Conversion:\n")
    report.write(f"- Sales amounts converted to GBP using fixed rates.\n")
    for currency, rate in conversion_rates.items():
        report.write(f"  * {currency} to GBP rate: {rate}\n")
    report.write(f"\n")

    # Report on weight conversion
    report.write(f"Weight Conversion:\n")
    report.write(f"- Product weights converted to kilograms.\n")
    report.write(f"  * Conversion rates: lb to kg = {weight_conversion['lb']}\n")

print(f"Cleaned dataset saved to: {cleaned_file}")
print(f"Data cleanup report saved to: {report_file}")