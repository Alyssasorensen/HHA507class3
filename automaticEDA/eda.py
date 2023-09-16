# Automated Analysis

!pip install pandas-profiling

import pandas as pd
from pandas_profiling import ProfileReport

# Load your dataset
data = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_3_eda/main/datasets/processed/Hospitalization_Discharge_Rates.csv')

# Generate the EDA report
report = ProfileReport(data)
report.to_file('eda_report.html')