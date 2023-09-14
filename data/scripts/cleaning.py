### Loading in packages 
import pandas as pd 

### Load in data 
df_patients['patient_id'].nunique()

### Look for missingness
df_patients.sample(10)
df_patients.isnull()
df_patients.isnull().sum()

percentmissing = pd.DataFrame(df_patients.isnull().sum()).reset_index()
percentmissing.rename(columns = {'index': 'variable', 0:'count_missing'}, inplace = true)
percentmissing['missing_percent'] = percentmissing['count_missing']/df_patients.shape[0])*100 

### Look for outliers 

df_patients.describe()

### Variables that we have identified that need conversion: year_of_birth, month_year_death
### If missing values you'll get an error 
df_patients['year_of_birth'] = df_patients['year_of_birth'].astype(float).apply(np, round)
df_patients['month_year_death'] = df_patients['month_year_death'].str.replace('.0', '')

### Univariate descriptives: (descriptives, frequencies, histograms, etc.)


### Bivariate descriptives: (correlations, covariances)

df_patients.to_csv('https://raw.githubusercontent.com/Alyssasorensen/HHA507class3/main/patient.csv')