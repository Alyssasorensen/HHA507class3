# Automated Analysis

!pip install pandas-profiling

import pandas as pd
from pandas_profiling import ProfileReport

# Load your dataset
data = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_3_eda/main/datasets/processed/Hospitalization_Discharge_Rates.csv')

# Generate the EDA report
report = ProfileReport(data)
report.to_file('eda_report.html')

# Analyzation 
# The Pandas Profiling Report begins with an overview of the dataset statistics. This includes number of variables, number of observations, missing cells, missing cells (%), duplicate rows, duplicate rows (%), total size in memory, and average record size in memory. It also displays the variable types which includes numeric and categorical. The next part shows the variable section. This section displays specific characteristics of each column. This includes distinct variables, missing variables, infinite variables, mean, maximum, minimum, zeros, zeros (%), negative variables, negative (%) variables, and memory size. The next part is interactions. This part displays a scatter plot of all of the variables from the columns. The next part shows correlations and this is shown through a heatmap. The cooler colors represent a positive correlation and the warmer colors represent a negative correlation. The next table in the Pandas Profiling Report displays missing values from the dataset. The last table in the report displays a sample of the dataset that was used.  