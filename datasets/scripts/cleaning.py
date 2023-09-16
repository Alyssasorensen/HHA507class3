# Univariate Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## loading the clean .csv file - patients_cleaned.csv

df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_3_eda/main/datasets/processed/Hospitalization_Discharge_Rates.csv')

df.columns

# Display the first few rows of the dataset
df.head()

# Hospitalization Discharge Rates in Lake County, Illinois. Explanation of field attributes:
# Anxiety disorders are characterized by excessive fear or stress that is difficult to control and negatively and substantially impacts daily functioning. This is a rate per 100,000. Mood disorders are characterized by the elevation or lowering of a person's mood, such as depression or bipolar disorder. This is a rate per 100,000. Alcohol rehabilitation is a term for the medical and/or psychotherapeutic treatment for dependency on alcohol. This is a rate per 100,000. Diabetes is a chronic disease in which blood sugar (glucose) levels are above normal. This is a rate per 100,000. Hypertension is a chronic disease in which blood pressure (the force of the blood flowing blood vessels) is consistently high. This is a rate per 100,000. Asthma is a condition in which airways narrow, swell, and produce extra mucus leading to difficulty in breathing. This is a rate per 100,000. Senior falls refers to individuals who are 65 years or older who have a fall and injure themselves. This is a rate per 100,000. Hospital discharge is defined as the release of a patient who has stayed at least one night in hospital. This is a rate per 100,000. Mental health conditions/ or mental illnesses refer to disorders generally characterized by dysregulation of mood, thought, and/or behavior. This is a rate per 100,000. Ambulatory Care Sensitive Conditions (ACSCs) are defined as conditions where effective community care and case management can help prevent the need for hospital admission. This is a rate per 100,000.

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

# Bivariate Analysis
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

# Strong Correlations
# For computing the correlation coefficients, I decided to use a heatmap. This allows me to visually observe the correlation coefficients and it is much easier to read. It also helps me identify patterns and associations between variables. Positive correlations are indicated by warmer colors and negative correlations are indicated by cooler colors. From this heatmap, we can see that there are strong correlations of discharges between anxiety disorders and diabetes, anxiety disorders and asthma, anxiety disorders and mental health conditions, mood disorders and mental health conditions, alcohol and mental health conditions, diabetes and asthma, and hypertension and mental health conditions.   

#Handling Outliers
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Select the variable of interest
variable_of_interest = 'Diabetes'

# Calculate the IQR (Interquartile Range)
Q1 = df[variable_of_interest].quantile(0.25)
Q3 = df[variable_of_interest].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = df[(df[variable_of_interest] < lower_bound) | (df[variable_of_interest] > upper_bound)]

# Visualize outliers using a boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x=variable_of_interest, data=df, palette='Set3')
plt.title(f'Boxplot: {variable_of_interest}')
plt.xlabel(variable_of_interest)
plt.grid(True)
plt.show()

# Display the identified outliers
print("Identified Outliers:")
print(outliers)
# Observation 
# We can see from this boxplot that there are no outliers. If there were outliers, then they would appear outside of the green box. I inputted 1.5 to find the lower and upper bounds for the outliers. I also inputted 2 and 3 to find the lower and upper bounds and there were no outliers displayed. 

# Select the variable of interest
variable_of_interest = 'Hypertensi'

# Calculate the IQR (Interquartile Range)
Q1 = df[variable_of_interest].quantile(0.25)
Q3 = df[variable_of_interest].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = df[(df[variable_of_interest] < lower_bound) | (df[variable_of_interest] > upper_bound)]

# Visualize outliers using a boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x=variable_of_interest, data=df, palette='Set3')
plt.title(f'Boxplot: {variable_of_interest}')
plt.xlabel(variable_of_interest)
plt.grid(True)
plt.show()

# Display the identified outliers
print("Identified Outliers:")
print(outliers)
# Observation
# From this boxplot, we can see that there are two outliers for the amount of discharges for hypertension. This includes one at 77.90589 and one at 142.28546. The identified outliers are also shown below the boxplot, ensuring we have an accurate representation of the boxplot. To identify the lower and upper bounds, I used the number 1.5. Below the boxplot, the other columns' outliers are also shown based on the hypertension values.

# Select the variable of interest
variable_of_interest = 'Anxiety_Di'

# Calculate the IQR (Interquartile Range)
Q1 = df[variable_of_interest].quantile(0.25)
Q3 = df[variable_of_interest].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = df[(df[variable_of_interest] < lower_bound) | (df[variable_of_interest] > upper_bound)]

# Visualize outliers using a boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x=variable_of_interest, data=df, palette='Set3')
plt.title(f'Boxplot: {variable_of_interest}')
plt.xlabel(variable_of_interest)
plt.grid(True)
plt.show()

# Display the identified outliers
print("Identified Outliers:")
print(outliers)
# Observation
# From this boxplot, we can see that there are two outliers for the amount of discharges for anxiety disorders. This includes one at 530.465048 and one at 509.524881. The identified outliers are also shown below the boxplot, ensuring we have an accurate representation of the boxplot. To identify the lower and upper bounds, I used the number 1.5. Below the boxplot, the other columns' outliers are also shown based on the anxiety disorder values.  

# Approach to Handling These Outliers
# I believe we could retain the outliers that appeared in two of the boxplots above. Since the data points represent the number of discharges for certain diagnoses in different zip codes, this means that some zip codes have a higher amount of discharges for certain diagnoses. It is important to retain these outliers so that we can observe how some conditions are more or less prevalent in an area compared to other areas. 
