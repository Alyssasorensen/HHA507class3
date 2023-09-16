import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## loading the clean .csv file - patients_cleaned.csv

df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_3_eda/main/datasets/processed/Hospitalization_Discharge_Rates.csv')

df.columns

# Display the first few rows of the dataset
df.head()
