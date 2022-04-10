# %%
import pandas as pd
# %%
emp = pd.read_csv(
    'http://kuberlu.com/data/employees.csv'
    )
emp[['first','last','dept']].head()
# %%
dept = pd.read_csv(
    'http://kuberlu.com/data/departments.csv'
)
dept.head()

# %%
merged = pd.merge(emp, dept, how='inner', on='dept')
# %%
merged.head()

# %%
