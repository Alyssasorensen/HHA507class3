import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## loading the clean .csv file - patients_cleaned.csv

df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_3_eda/main/datasets/processed/Hospitalization_Discharge_Rates.csv')

df.columns

# Display the first few rows of the dataset
df.head()

# Calculate measures of central tendency
mean = df['Total Charges'].mean()
median = df['Total Charges'].median()
mode = df['Total Charges'].mode().values[0]

# Calculate measures of spread
range_val = df['Diabetes'].max() - df['Diabetes'].min()
variance = df['Diabetes'].var()
std_deviation = df['Diabetes'].std()
iqr = df['Diabetes'].quantile(0.75) - df['Diabetes'].quantile(0.25)

# Print the results
print("Measures of Central Tendency:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print("\nMeasures of Spread:")
print(f"Range: {range_val}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
print(f"IQR (Interquartile Range): {iqr}")

# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(df['Diabetes'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Diabetes')
plt.xlabel('Diabetes')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()