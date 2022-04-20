# modules
import pandas as pd
import os
from modules.config import data_path

filename = os.path.join(data_path(), 'age_income.csv')
df = pd.read_csv(filename)


def expert_level(age):
    if age <= 30:
        return 'newbie'
    elif age <= 50:
        return 'intermediate'
    elif age > 50:
        return 'expert'
    else:
        return 'no label'


df['experience_level'] = df['Age'].apply(lambda x: expert_level(x))
print(df.head(10))
