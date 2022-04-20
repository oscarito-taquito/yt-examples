# modules
import pandas as pd
import os
from modules.config import data_path

filename = os.path.join(data_path(), 'age_income.csv')
df = pd.read_csv(filename)
df['rn'] = df.sort_values(['Name', 'Age']).groupby('Marital Status').cumcount() + 1
print(df.sort_values(by=['Marital Status', 'Name', 'Age']))