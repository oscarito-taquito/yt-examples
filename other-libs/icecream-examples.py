import pandas as pd
import numpy as np
from icecream import ic

ic.configureOutput(prefix='🤖 ',
                   includeContext=True)
# read in sample data
df = pd.read_csv('../data/age_income.csv')
ic(df.head())


def my_func(x):
    x = x * (1 + np.random.normal(
        0,
        0.1)
             )
    return x


df['Adj Income'] = df['Income'].apply(my_func)
cols = ['Age', 'Income', 'Adj Income']
ic(df[cols].head())
