import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## loading the clean .csv file - patients_cleaned.csv

df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_3_eda/main/datasets/processed/Hospitalization_Discharge_Rates.csv')

df.columns

# Display the first few rows of the dataset
df.head()

# Calculate measures of central tendency
mean = df['Diabetes'].mean()
median = df['Diabetes'].median()
mode = df['Diabetes'].mode().values[0]

# Calculate measures of central tendency
mean = df['Hypertensi'].mean()
median = df['Hypertensi'].median()
mode = df['Hypertensi'].mode().values[0]

# Calculate measures of spread
range_val = df['Diabetes'].max() - df['Diabetes'].min()
variance = df['Diabetes'].var()
std_deviation = df['Diabetes'].std()
iqr = df['Diabetes'].quantile(0.75) - df['Diabetes'].quantile(0.25)

# Calculate measures of spread
range_val = df['Hypertensi'].max() - df['Hypertensi'].min()
variance = df['Hypertensi'].var()
std_deviation = df['Hypertensi'].std()
iqr = df['Hypertensi'].quantile(0.75) - df['Hypertensi'].quantile(0.25)

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

# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(df['Hypertensi'], bins=20, color='navy', edgecolor='black')
plt.title('Distribution of Hypertension')
plt.xlabel('Hypertension')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot for Diabetes vs. Discharges
plt.figure(figsize=(8, 6))
plt.scatter(df['Diabetes'], df['Discharges'], alpha=0.5, color='blue')
plt.title('Scatter Plot: Diabetes vs. Discharges')
plt.xlabel('Diabetes')
plt.ylabel('Discharges')
plt.grid(True)
plt.show()

# Scatter plot for Hypertensi vs. Discharges
plt.figure(figsize=(8, 6))
plt.scatter(df['Hypertensi'], df['Discharges'], alpha=0.5, color='red')
plt.title('Scatter Plot: Hypertension vs. Discharges')
plt.xlabel('Hypertension')
plt.ylabel('Discharges')
plt.grid(True)
plt.show()

# Compute correlation matrix for numerical variables
correlation_matrix = df.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Plot a heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()