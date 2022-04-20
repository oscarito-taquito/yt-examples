# modules
import pandas as pd
import os
from modules.config import data_path

filename = os.path.join(data_path(), 'age_income.csv')
df = pd.read_csv(filename)
names = ['Gisela', 'Heather', 'Hiroko']
print(df[df.Name.isin(names)])
