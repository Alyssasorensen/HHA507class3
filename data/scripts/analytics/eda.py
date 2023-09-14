import pandas as pd

## loading the clean .csv file - patients_cleaned.csv

df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/HHA507class3/main/data/processed/lab_result.csv')
df.columns

df['lab_result_num_val']
df.dtypes

df.lab_result_num_val.describe()

temp = df.groupby('units_of_measure').lab_result_num_val.describe()
temp.to_csv('https://raw.githubusercontent.com/Alyssasorensen/HHA507class3/main/data/processed/lab_result.csv')

temp_code = df.groupby('code').lab_result_num_val.describe()
temp_code.to_csv('https://raw.githubusercontent.com/Alyssasorensen/HHA507class3/main/data/processed/lab_result.csv')

### lets explore smoking lab results
smoking = df[df['code'] == '72166-2']
smoking['lab_result_num_val']
smoking['lab_result_text_val']
smoking.columns

###Glucose [Mass/volume] in Blood
glucose = df[df['code'] == '2339-0']
glucose.to_csv(csv file here)
glucose['lab_result_num_val'].describe()


