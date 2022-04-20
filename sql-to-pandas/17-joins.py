# modules
import pandas as pd
import os
from modules.config import data_path

age_income = os.path.join(data_path(), 'age_income.csv')
name_children = os.path.join(data_path(), 'name_children.csv')
df1 = pd.read_csv(age_income)
df2 = pd.read_csv(name_children)

df3 = pd.merge(df1, df2, how='inner', on='Name')

print(df3.head())
